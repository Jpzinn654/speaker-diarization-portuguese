import whisperx
import gc 

class whisperTranscriber():

    def __init__(self, hf_token_api):
        self.device = "cpu" 
        self.audio = r"C:\Users\DELL\Documents\speaker-diarization-portuguese\src\audio\temp.wav"
        self.batch_size = 6 # reduce if low on GPU mem
        self.compute = "float32" # change to "int8" if low on GPU mem (may reduce accuracy)
        self.hf_token_api = hf_token_api
        self.model = whisperx.load_model("base", self.device, compute_type=self.compute, language='pt')

        self.transcriber()


    def transcriber(self):
    
        audio = whisperx.load_audio(self.audio)
        result = self.model.transcribe(audio, batch_size=self.batch_size)

        model_a, metadata = whisperx.load_align_model(language_code=result["language"], device=self.device)
        result = whisperx.align(result["segments"], model_a, metadata, audio, self.device, return_char_alignments=False)

        print(result['word_segments'])
        
    def speaker_diarization(self):
        diarize_model = whisperx.DiarizationPipeline(use_auth_token=self.hf_token_api, device=self.device)
        print(diarize_model)

if __name__ == '__main__':
    whisperTranscriber().speaker_diarization()