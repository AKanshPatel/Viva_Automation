from groq import Groq
from dotenv import load_dotenv
import os
# from utils.global_variables import  GlobalVariable

class GroqApi:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("GROQ_API_KEY")
        self.client = Groq(api_key=self.api_key)
        self.prompt = None
        # self.gv = GlobalVariable()
        
    def api_calls(self):
        completion = self.client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {
                    "role": "user",
                    "content": self.prompt
                }
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )
        question = self._stream_response(completion)
        print(question)
        return completion
    
    def _stream_response(self, completion):
        """
        Helper function to handle streaming responses.
        """
        response = ""
        for chunk in completion:
            response += chunk.choices[0].delta.content or ""
        return response
    
if __name__ == "__main__":
    g = GroqApi()
    g.api_calls()
    
