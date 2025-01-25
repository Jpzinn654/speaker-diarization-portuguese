import whisperx
import gc
import time  
from pyannote.audio.pipelines import SpeakerDiarization
from pyannote.core import Segment

class whisperTranscriber():

    def __init__(self, hf_token_api):
        self.device = "cpu"
        self.audio = r"your_audio_path_here" 
        self.batch_size = 1  # reduz se a memória da GPU for baixa
        self.compute = "float32"  # mude para "int8" se a memória da GPU for baixa (pode reduzir a precisão)
        self.hf_token_api = hf_token_api
        self.model = whisperx.load_model("base", self.device, compute_type=self.compute, language='pt')

        self.diarization = SpeakerDiarization.from_pretrained("pyannote/speaker-diarization-3.1")

    def transcriber(self):
        start_time = time.time()

        # Carregar o áudio
        audio = whisperx.load_audio(self.audio)
        result = self.model.transcribe(audio, batch_size=self.batch_size)

        # Carregar o modelo de alinhamento e alinhar o áudio com a transcrição
        model_a, metadata = whisperx.load_align_model(language_code=result["language"], device=self.device)
        result = whisperx.align(result["segments"], model_a, metadata, audio, self.device, return_char_alignments=False)

        # Executar a diarização de fala
        diarization_result = self.diarization({'uri': 'audio', 'audio': self.audio})

        # Mapeia os segmentos de diarização com os locutores
        speakers = []
        for segment, _, speaker in diarization_result.itertracks(yield_label=True):
            speakers.append({
                'start': segment.start,
                'end': segment.end,
                'speaker': speaker
            })

        # Mapeamento de locutores para "homem" e "mulher"
        speaker_dict = {0: "Homem", 1: "Mulher"}

        # Agora, ajustamos sua transcrição para incluir o locutor
        speaker_transcription = []
        for segment in result['segments']:
            entry_start = segment['start']
            entry_end = segment['end']
            
            # Encontrar o speaker correspondente ao segmento de tempo
            speaker_label = None
            for speaker in speakers:
                if speaker['start'] <= entry_start < speaker['end'] or speaker['start'] < entry_end <= speaker['end']:
                    speaker_label = speaker['speaker']
                    break
            
            if speaker_label is not None:
                speaker_number = int(speaker_label.split('_')[1])

                mapped_speaker = speaker_dict.get(speaker_number, "desconhecido")
                speaker_transcription.append({
                    'speaker': f'{mapped_speaker}', 
                    'start': entry_start,
                    'end': entry_end,
                    'text': segment['text']
                })

        for item in speaker_transcription:
            print(f"{item['speaker']} disse: '{item['text']}'")

        end_time = time.time()  
        elapsed_time = end_time - start_time  
        print(f"Tempo total de transcrição: {elapsed_time:.2f} segundos")

        return result

if __name__ == '__main__':
    whisperTranscriber('hf_token_api').transcriber()
