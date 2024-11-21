import logging
from audio import record_audio, play_audio  # Assuming the original script is saved as record_and_play.py

# Configure logging for the test
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

if __name__ == "__main__":
    try:
        # Path for the recorded audio
        audio_file_path = "test_audio.mp3"

        # Test recording audio
        logging.info("Starting audio recording test...")
        record_audio(
            file_path=audio_file_path,
        )
        logging.info(f"Audio recording saved to {audio_file_path}")

        # Test playing the recorded audio
        logging.info("Starting audio playback test...")
        play_audio(audio_file_path)
        logging.info("Audio playback test completed successfully!")

    except Exception as e:
        logging.error(f"An error occurred during the test: {e}")
