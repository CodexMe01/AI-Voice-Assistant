# AI-Powered Virtual Voice Assistant

This project is an AI-powered virtual voice assistant designed to perform various tasks, interact with APIs, and provide seamless voice-controlled functionality. The assistant listens for user commands, executes specific actions, and integrates with advanced AI technologies for content generation.

---

# Features

# Core Functionality
- **Voice Command Recognition**: Utilizes the `speech_recognition` library to recognize and process voice commands.
- **Speech Output**: Uses `pyttsx3` for text-to-speech capabilities, enabling the assistant to respond audibly.
- **Task Execution**: Performs a variety of tasks based on voice commands, such as:
  - Opening popular websites (e.g., YouTube, Behance, Instagram, GitHub, and Google).
  - Controlling the system (e.g., shutdown, restart, retrieve system information).
  - Opening applications like Spotify.
  - Playing songs using links from a predefined music library.

# Advanced Features
- **AI-Generated Text**: Integrates with Google Gemini API for generating text based on user-provided prompts.
- **Dynamic Task Processing**: Customizable commands that adapt to various use cases.

---

# Installation

# Prerequisites
1. Python 3.7+
2. Required Libraries:
   - `speech_recognition`
   - `webbrowser`
   - `pyttsx3`
   - `requests`
   - `google-generativeai`
   - `flask`
3. API Key for Google Gemini API

# Setup Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai-voice-assistant.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ai-voice-assistant
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Add your Google Gemini API key:
   - Replace the placeholder API key in the `main()` function with your actual key.

---

# Usage

1. Run the script:
   ```bash
   python main.py
   ```
2. The assistant will greet you with "Command ME Pratyush" and start listening for your commands.
3. Speak a command such as:
   - "Open Behance"
   - "Play [song_name]"
   - "Generate text about [topic]"

4. The assistant will process the command and execute the corresponding task.

---

# Commands and Functionality

| **Command**              | **Action**                                  |
|--------------------------|----------------------------------------------|
| "Open Behance"           | Opens the Behance website in a browser.      |
| "Open YouTube"           | Opens YouTube in a browser.                 |
| "Play [song_name]"       | Plays the specified song from `musicLibrary` |
| "Generate text about..." | Generates text using Google Gemini API.      |
| "Shutdown"               | Shuts down the system.                      |
| "Restart"                | Restarts the system.                        |
| "Info"                   | Displays system information.                |

---

# Code Structure

# `main.py`
The main script for the assistant, containing:
- Command recognition and processing.
- Task execution logic.
- Integration with Google Gemini API.

# `musicLibrary.py`
A module for managing music links. It maps song names to their respective URLs for playback.

---

# Dependencies

- `speech_recognition`: For recognizing and processing voice commands.
- `pyttsx3`: For converting text to speech.
- `webbrowser`: For opening URLs in a web browser.
- `google-generativeai`: For generating AI-based content.
- `flask`: For potential web-based extensions.
- `os`: For system control operations.

---

# Future Improvements

- Add support for more dynamic and personalized commands.
- Enhance integration with other APIs and platforms.
- Improve error handling and fallback mechanisms.
- Build a GUI for user-friendly interaction.

---

# Contributing

Contributions are welcome! Please open an issue or submit a pull request for any bug fixes, feature suggestions, or enhancements.

---

# License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---
# Acknowledgments

Special thanks to the developers of the libraries and APIs used in this project.

---

# Contact

For questions or feedback, please contact Pratyush at pratyushranjanghadai@gmail.com.

