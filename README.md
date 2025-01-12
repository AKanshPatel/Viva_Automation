# Project Overview!

## Info: 
The ‘Viva Automation System’ aims to revolutionize oral assessments by automating the question selection, candidate interaction, and evaluation process. Utilizing the Llama 3 8b model for real-time question generation and response evaluation, along with Nova-2 APIs for Speech-to-Text (STT) and Text-to-Speech (TTS), the system provides a seamless, interactive assessment experience. Candidates select topics, answer questions in spoken format, and receive immediate feedback based on their responses. The system adjusts the difficulty of subsequent questions dynamically, ensuring personalized testing aligned with each candidate's knowledge level. The project leverages a user-friendly Streamlit interface, offering a scalable solution for oral assessments. Future enhancements, such as transitioning to a Django-based frontend, adding multilingual support, and integrating with educational platforms, will further improve its accessibility, scalability, and interactivity, making it a versatile tool for educational and professional use. 


## WorkFlow

![System Flow](https://github.com/AKanshPatel/Viva_Automation/blob/4b334272a3ed25cfd190b5957890f8b480b7d506/Documents/System%20Flow.png)
![Flow Diagram](https://github.com/AKanshPatel/Viva_Automation/blob/4b334272a3ed25cfd190b5957890f8b480b7d506/Documents/Flow%20Chart.png)
## Folder Structure

```plaintext
VivaAutomation/
│
├── app.py                      # Main entry point for running the app
├── backend/                    # Contains all backend logic and models
│   ├── __init__.py
│   ├── deepgram_stt_tts.py     # Deepgram STT and TTS model
│   ├── prompt.py               # Prompts(Question Generation and Evaluation) to be passed in groq api
│   ├── groq_api_llm.py         # Utility for making Groq and Deepgram API calls
│   ├── database.py             # Manages interactions with the database (scores, feedback)
│
├── frontend/                   # Contains all frontend logic and UI components
│   ├── navigation.py           # This File will handle the navigation between the pages
│   └── pages
│        ├── home_page.py            # UI for the home page
│        ├── topic_selection.py      # UI for selecting topics
│        ├── question_answer.py      # UI for question display, audio, and mic recording and also the main program
│        └── score.py                # UI for showing the score and feedback
│
├── utils/
│    ├── audio.py              # To record and play audio
│    ├── fetch_questions.py    # Generate the selected topics qb
│    └── global_vareiable.py    # File paths
│       
├── data/                       # Contains data files, such as question bank and scores
│   ├── question_bank.json      # The file containing the units, topics, and questions
│   └── scores.db               # Database for storing scores and feedback
│     
├── documents/                  # Documentation assets
│
├── requirements.txt            # List of dependencies required for the project
├── README.md                   # Project documentation
└── main.py                 # Test all the models and files
```

## Setup 