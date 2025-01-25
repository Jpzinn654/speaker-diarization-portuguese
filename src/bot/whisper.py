import whisperx
import gc 

class whisperTranscriber():

    def __init__(self):
        self.device = device = "cpu" 
        self.audio = r"C:\Users\DELL\Documents\speaker-diarization-portuguese\src\audio\temp.wav"
        self.batch_size = 16 # reduce if low on GPU mem
        self.compute = compute_type = "float32" # change to "int8" if low on GPU mem (may reduce accuracy)

        self.model = whisperx.load_model("base", device, compute_type=compute_type, language='pt')

        self.transcriber()

    def transcriber(self):
    
        audio = whisperx.load_audio(self.audio)
        result = self.model.transcribe(audio, batch_size=self.batch_size)

        model_a, metadata = whisperx.load_align_model(language_code=result["language"], device=self.device)
        result = whisperx.align(result["segments"], model_a, metadata, audio, self.device, return_char_alignments=False)

    def speaker_diarization():
        pass