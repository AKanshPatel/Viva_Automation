#TODO Fix the subsequent and feedback prompts

from utils.global_variables import GlobalVariable
import json

class PromptGenerator:
    def __init__(self):
        self.question_bank = GlobalVariable.filtered_questionbank 
        GlobalVariable.promt_first = None
        GlobalVariable.promt_second = None
        
    def generate_first_question_prompt(self):
        """
        Generates the prompt for the first question.
        The prompt selects an easy-level question from the question bank.
        """
        prompt_first = f"""
        You are the Viva_Question Selector for an oral exam system. Your task is to select 
        one easy, introductory-level question from the list below. The selected question will be 
        the first question in the viva and should be simple, clear, and suitable for a candidate 
        at the start of their oral exam. Return only the selected question, with no additional context or details.

        Question bank: {json.dumps(self.question_bank)}
        """
        GlobalVariable.promt_first = prompt_first   
        
    def generate_subsequent_question_prompt(self, previous_question, candidate_answer):
        """
        Generates the prompt for subsequent questions based on the feedback from the previous answer.
        It adjusts the difficulty or relevance of the next question.
        The next question should either increase in difficulty or align with the candidate's response.
        """
        prompt_second = f"""
        You are the Viva_Question Selector. The candidate just answered the following question:
        "{previous_question}"
        Their answer: "{candidate_answer}"
        Based on this, generate the next question that is appropriate in terms of complexity and relevance.
        The next question should either increase in difficulty or align with the candidate's response. 
        Return only the question with no additional context or details.

        Question bank: {json.dumps(self.question_bank)}
        """
        GlobalVariable.promt_second = prompt_second


    def generate_feedback_prompt(self, question, candidate_answer):
        """
        Generates the evaluation feedback prompt.
        The model evaluates the candidate's answer and provides a score and feedback.
        """
        prompt_feedback = f"""
        The candidate answered the following question:
        "{question}"
        Their answer: "{candidate_answer}"
        Please evaluate the answer based on the following criteria:
        1. Relevance to the question
        2. Completeness of the answer
        3. Clarity and correctness
        Assign a score from 1 to 10 based on these criteria.
        Provide brief feedback explaining the score.
        Return only the score and feedback, with no other context or details.
        """
        GlobalVariable.prompt_feedback = prompt_feedback
        
