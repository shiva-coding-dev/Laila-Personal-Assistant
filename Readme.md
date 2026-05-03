# LAILA - Voice-Activated Virtual Assistant

LAILA (Layla) is a Python-based, voice-activated virtual assistant created to help automate daily tasks, answer questions, and control your computer using speech recognition and natural language processing. 

It is designed similarly to Alexa or Google Assistant but runs entirely locally on your machine (optimized for macOS), utilizing powerful AI models for conversational understanding.

## Key Features

- **Wake Word Detection:** LAILA constantly listens for the wake word **"Laila"** to activate and start accepting commands.
- **AI Conversational Engine:** Powered by the Groq API (using the `llama3-70b-8192` model), LAILA remembers conversation history and provides short, intelligent responses.
- **Voice Control & Feedback:** Uses `speech_recognition` (Google STT) to transcribe your voice and `pyttsx3` to speak the responses aloud.
- **System Automation (macOS):** Can open local applications directly from voice commands (e.g., "open Safari").
- **Web Browsing:** Can open pre-configured websites on command (e.g., "website google").
- **Music Playback:** Capable of searching and playing predefined songs from your music library map.
- **News Updates:** Fetches and reads the latest top news headlines in India using NewsAPI.
- **Wikipedia Search:** Can listen for a specific topic, search Wikipedia, and read a brief summary out loud.

## Technology Stack & Dependencies

- **Python 3**
- `speech_recognition`: For transcribing microphone audio.
- `pyttsx3`: Text-to-speech conversion.
- `Groq`: For handling natural language generation and AI conversational memory.
- `requests`: To fetch API data (like NewsAPI).
- `python-dotenv`: To manage secure API keys in a `.env` file.
- `wikipedia` (custom `wikipedia_api` wrapper): To fetch Wikipedia summaries.

## Project Structure

- `main.py` - The core engine that handles microphone listening, wake word detection, command routing, and text-to-speech.
- `apps.py` - Contains the mapping dictionary for supported macOS applications.
- `musicLibrary.py` - Contains the mapping for music commands to web links.
- `my_websites.py` - Contains the dictionary for your most-visited web links.
- `wikipedia_api.py` - A helper module to fetch Wikipedia summaries while handling disambiguation and errors.
- `.env` - Stores your API keys securely (excluded from version control).

## Getting Started

### 1. Prerequisites
Make sure you have Python installed. You may also need to install `PyAudio` depending on your OS, which is required by `speech_recognition`.

### 2. Install Dependencies
Run the following command to install the required libraries (preferably inside your `.venv`):
```bash
pip install SpeechRecognition pyttsx3 requests groq python-dotenv wikipedia
```
*(Note: If you are on macOS and run into issues with PyAudio, you might need to run `brew install portaudio` before `pip install pyaudio`)*

### 3. Environment Variables
Create a `.env` file in the root of the project folder and add your API keys:
```env
api_key=your_groq_api_key_here
newsapi=your_newsapi_key_here
```

### 4. Run the Assistant
Simply run the main python script:
```bash
python main.py
```
You will see console logs telling you it is listening. Say **"Laila"** to wake it up, and then speak your command (e.g., "play [song]", "news", "wikipedia", or just ask a general question!).

## How to Stop
To turn the assistant off, just say the command **"switch off"** while it is actively listening for instructions.
