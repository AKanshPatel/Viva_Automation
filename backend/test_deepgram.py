import logging
from deepgram_api import transcribe_audio, text_to_speech  # Replace 'your_module_name' with the actual filename

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Deepgram API credentials
DEEPGRAM_API_KEY = "cd7a0bfc96550fb849faf7345a8c556f85a2e752"

# File paths
AUDIO_FILE_PATH = "backend/test_audio.mp3"  # Input audio file for transcription
OUTPUT_AUDIO_FILE_PATH = "output_audio.wav"  # Output file for synthesized speech

def main():
    try:
        logging.info("Starting transcription test...")

        # Step 1: Transcribe the audio file
        transcribed_text = transcribe_audio(
            model='deepgram',
            api_key=DEEPGRAM_API_KEY,
            audio_file_path=AUDIO_FILE_PATH
        )
        logging.info(f"Transcription successful: {transcribed_text}")

        # Step 2: Convert the transcribed text back to speech
        logging.info("Starting text-to-speech conversion...")
        text_to_speech(
            model='deepgram',
            api_key=DEEPGRAM_API_KEY,
            text=transcribed_text,
            output_file_path=OUTPUT_AUDIO_FILE_PATH
        )
        logging.info(f"Text-to-speech conversion successful. Output saved to {OUTPUT_AUDIO_FILE_PATH}")

    except Exception as e:
        logging.error(f"An error occurred during the test: {e}")

if __name__ == "__main__":
    main()
