# TODO List

## 1. Improve `utils.audio`
- [ ] Enhance the audio recording functionality to ensure proper recording quality.
- [ ] Test recording for different input devices and environments.
- [ ] Optimize audio file formats and storage options for performance.

## 2. Work with Scoring Strategy
- [ ] Develop a comprehensive scoring algorithm.
- [ ] Incorporate feedback from Groq API evaluation into scoring logic.
- [ ] Test scoring against various sample answers to ensure fairness and consistency.

## 3. Add Streamlit Frontend
- [ ] Finalize the UI design for topic selection and question-answer interaction.
- [ ] Integrate the `question_answer` page with Groq and Deepgram API functionalities.
- [ ] Ensure smooth navigation between pages using the Streamlit framework.

## 4. Add Database and Its Code
- [ ] Design the database schema for storing user scores and interactions.
- [ ] Implement CRUD operations for managing candidate data.
- [ ] Connect the database with the backend logic.
- [ ] Test database integration with sample datasets.

## 5. Problem: Same Question
- [ ] Investigate and resolve the issue of repetitive questions being asked.
- [ ] Implement logic to track and avoid duplicate question prompts.
- [ ] Add logging to monitor question selection and ensure diversity.

## 6. Provide Context for Evaluation
- [ ] Define a structure for passing subject name as context to Groq API.
- [ ] Modify the prompt generation logic to include the subject-specific context.
- [ ] Test the context handling with different subjects to validate performance.
