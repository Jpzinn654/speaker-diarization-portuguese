from bot.whisper import whisperTranscriber
from secret.hf_token import *

def run_whisper():

    whisperTranscriber(hf_token_api).speaker_diarization()

if __name__ == '__main__':
    run_whisper()