import re
import os
import time
from backend.prompt import PromptGenerator
from backend.groq_api_llm import GroqApi
from backend.deepgram_stt_tts import DeepgramAPI
from utils.audio import record_audio, play_audio


class VivaAutomationApp:
    def __init__(self):
        self.question_no = 1
        self.prompt_generator = PromptGenerator()
        self.groq_api = GroqApi()
        self.deepgram_api = DeepgramAPI()
        self.current_question = None
        self.current_answer = None
        self.evaluation_feedback = None
        self.total_score = 0
        self.max_questions = 2  # Set the maximum number of questions
        self.sleep_duration = 1  # Sleep duration after asking a question

    def generate_question(self):
        """
        Generates the first question or a subsequent question using the PromptGenerator module.
        """
        if self.question_no == 1:
            prompt = self.prompt_generator.generate_first_question_prompt()
        else:
            prompt = self.prompt_generator.generate_subsequent_question_prompt(
                self.current_question, self.current_answer, self.evaluation_feedback
            )
        self.current_question = self.groq_api.api_calls(prompt)

    def synthesize_and_play_question(self, question_text, output_file):
        """
        Converts text to speech and saves the audio file.

        Args:
            question_text (str): The question text to be converted to speech.
            output_file (str): Path where the audio file will be saved.
        """
        self.deepgram_api.text_to_speech(
            text=question_text, output_file_path=output_file
        )

    def record_answer(self, output_file):
        """
        Records the candidate's response and saves it as an audio file.

        Args:
            output_file (str): Path where the recorded answer will be saved.
        """
        print("Recording answer for 5 seconds...")
        record_audio(file_path=output_file)
        time.sleep(5)  # Wait for 5 seconds while recording

    def transcribe_answer(self, audio_file):
        """
        Converts recorded speech to text.

        Args:
            audio_file (str): Path of the recorded answer audio file.

        Returns:
            str: Transcribed text of the answer.
        """
        return self.deepgram_api.transcribe_audio(audio_file_path=audio_file)

    def evaluate_answer(self, question, answer):
        """
        Evaluates the candidate's answer using Groq API.

        Args:
            question (str): The question text.
            answer (str): The candidate's answer.

        Returns:
            dict: A dictionary containing feedback and score.
        """
        feedback_prompt = self.prompt_generator.generate_feedback_prompt(
            question, answer
        )
        evaluation = self.groq_api.api_calls(feedback_prompt)

        if isinstance(evaluation, str):
            score_match = re.search(r"score:\s*(\d+)", evaluation)
            feedback_match = re.search(r'feedback:\s*"(.*?)"', evaluation, re.DOTALL)

            if score_match and feedback_match:
                score = int(score_match.group(1))
                feedback = feedback_match.group(1)
                self.total_score += score
                return {"score": score, "feedback": feedback}
            else:
                print("Error: Unable to parse the evaluation response:", evaluation)
                return {"score": 0, "feedback": "Error in evaluation"}
        elif isinstance(evaluation, dict):
            self.total_score += evaluation.get("score", 0)
            return evaluation
        else:
            print("Error: Groq API returned an unexpected response:", evaluation)
            return {"score": 0, "feedback": "Error in evaluation"}
