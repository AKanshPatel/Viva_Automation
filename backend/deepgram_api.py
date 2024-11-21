import json
import logging
from colorama import Fore
from deepgram import DeepgramClient, PrerecordedOptions, SpeakOptions

def transcribe_audio(model, api_key, audio_file_path):
    """
    Transcribe an audio file using the specified model.
    
    Args:
        model (str): The model to use for transcription ('deepgram').
        api_key (str): The API key for the transcription service.
        audio_file_path (str): The path to the audio file to transcribe.

    Returns:
        str: The transcribed text.
    """
    try:
        if model == 'deepgram':
            return _transcribe_with_deepgram(api_key, audio_file_path)
        else:
            raise ValueError("Unsupported transcription model")
    except Exception as e:
        logging.error(f"{Fore.RED}Failed to transcribe audio: {e}{Fore.RESET}")
        raise Exception("Error in transcribing audio")


def text_to_speech(model, api_key, text, output_file_path):
    """
    Convert text to speech using the specified model.
    
    Args:
        model (str): The model to use for TTS ('deepgram').
        api_key (str): The API key for the TTS service.
        text (str): The text to convert to speech.
        output_file_path (str): The path to save the generated speech audio file.
    
    Returns:
        None
    """
    try:
        if model == 'deepgram':
            _text_to_speech_with_deepgram(api_key, text, output_file_path)
        else:
            raise ValueError("Unsupported TTS model")
    except Exception as e:
        logging.error(f"{Fore.RED}Failed to convert text to speech: {e}{Fore.RESET}")
        raise Exception("Error in text-to-speech conversion")


def _transcribe_with_deepgram(api_key, audio_file_path):
    """
    Helper function to transcribe audio with Deepgram's Speech-to-Text API.
    
    Args:
        api_key (str): The API key for the transcription service.
        audio_file_path (str): The path to the audio file to transcribe.

    Returns:
        str: The transcribed text.
    """
    deepgram = DeepgramClient(api_key)
    try:
        with open(audio_file_path, "rb") as file:
            buffer_data = file.read()

        payload = {"buffer": buffer_data}
        options = PrerecordedOptions(model="nova-2", smart_format=True)
        response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)
        data = json.loads(response.to_json())

        transcript = data['results']['channels'][0]['alternatives'][0]['transcript']
        return transcript
    except Exception as e:
        logging.error(f"{Fore.RED}Deepgram transcription error: {e}{Fore.RESET}")
        raise


def _text_to_speech_with_deepgram(api_key, text, output_file_path):
    """
    Helper function to convert text to speech with Deepgram's Text-to-Speech API.
    
    Args:
        api_key (str): The API key for the TTS service.
        text (str): The text to convert to speech.
        output_file_path (str): The path to save the generated speech audio file.
    
    Returns:
        None
    """
    deepgram = DeepgramClient(api_key)
    try:
        options = SpeakOptions(
            model="aura-arcas-en",  # Choose the appropriate model from Deepgram
            encoding="linear16",    # Audio encoding format
            container="wav"         # Output container format
        )

        # Send the request to convert text to speech
        response = deepgram.speak.v("1").save(
            output_file_path,       # Path to save the generated audio
            {"text": text},         # Text input for conversion
            options                 # TTS options
        )
        logging.info(f"Speech successfully saved to {output_file_path}")
    except Exception as e:
        logging.error(f"{Fore.RED}Deepgram TTS error: {e}{Fore.RESET}")
        raise

