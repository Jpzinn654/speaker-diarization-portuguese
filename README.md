# Portuguese Speaker Diarization with Flask UI

## Overview

This project implements **speaker diarization** for Portuguese-language audio files, using **WhisperX** for transcription and **Speaker-Diarization 3.1** from **PyAnotAudio** for identifying and separating speakers. The project also includes a **Flask UI**, which allows users to easily upload audio files, perform transcription, and view speaker diarization results. Additionally, it automatically detects the gender of the speakers (Male or Female).

## Interface Screenshots

### UI without Transcription
![image](https://github.com/user-attachments/assets/6718624b-bf2c-48c8-9883-94e7f4b52a32)

### UI with Transcription
![image](https://github.com/user-attachments/assets/56e38836-116d-4b0e-b7e8-23cad26ad463)

## Features

- **Audio Transcription**: Utilizes WhisperX for high-quality transcription of Portuguese audio.
- **Speaker Diarization**: Uses PyAnotAudio's Speaker-Diarization 3.1 to distinguish between multiple speakers.
- **Flask Web Interface**: A user-friendly interface to upload audio files and view transcription and diarization results.
- **Automatic Gender Detection**: Automatically identifies and labels speakers as Male or Female.

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/Jpzinn654/speaker-diarization-portuguese
    cd speaker-diarization-portuguese
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Install PyAnotAudio (if not already installed):
    ```bash
    pip install pyanotaudio
    ```

4. Install WhisperX model (follow instructions from the official WhisperX repository for setup).

5. Start the Flask application:
    ```bash
    python app.py
    ```

6. Open your browser and visit:
    ```
    http://localhost:5000
    ```

## Usage

1. Upload an audio file in Portuguese.
2. Wait for the transcription process to complete.
3. The system will process the diarization and show the transcription along with labeled speakers.
4. Optionally, you can set the gender (Male/Female) for each speaker segment automatically.

## Technologies Used

- **WhisperX**: For transcribing Portuguese audio into text.
- **PyAnotAudio**: For speaker diarization.
- **Flask**: Web framework for building the UI.
- **Tailwind CSS**: For styling the web interface.
- **HTML/JavaScript**: For frontend development.

## Contributing

Feel free to fork the repository, make changes, and submit pull requests. If you're adding new features or fixing bugs, make sure to include relevant tests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for more details.
