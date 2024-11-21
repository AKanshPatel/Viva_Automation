from config import Config

# Simplified API key mapping for Groq (response) and Deepgram (transcription, TTS)
API_KEY_MAPPING = {
    "transcription": Config.DEEPGRAM_API_KEY,
    "response": Config.GROQ_API_KEY,
    "tts": Config.DEEPGRAM_API_KEY
}

def get_api_key(service):
    """
    Retrieve the API key for the specified service.
    
    Args:
        service (str): The service for which the API key is required ('transcription', 'response', 'tts').

    Returns:
        str: The API key for the specified service.
    """
    return API_KEY_MAPPING.get(service)

def get_transcription_api_key():
    """
    Get the API key for transcription (Deepgram).
    
    Returns:
        str: The Deepgram API key.
    """
    return get_api_key("transcription")

def get_response_api_key():
    """
    Get the API key for response generation (Groq).
    
    Returns:
        str: The Groq API key.
    """
    return get_api_key("response")

def get_tts_api_key():
    """
    Get the API key for text-to-speech (Deepgram).
    
    Returns:
        str: The Deepgram API key.
    """
    return get_api_key("tts")
