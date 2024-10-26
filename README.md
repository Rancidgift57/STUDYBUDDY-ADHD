# STUDYBUDDY-ADHD
Through this project we have aimed to create an educational platform for ADHD students. Currently we have added two features. 
1. A  chatbot using llama 3 model for doubt solving . 
2. A youtube video summarizer that would summarize the youtube videos helping in converting the youtube study material to a concise format helping the adhd students by helping them study in less time. Being impulsive they are not able to spend much time with concentration on studying . Thus this helps.

### Main Files and Structure
1. Python Scripts:
   - `chat1.py`, `chat2.py`, and `llama.py`: Likely related to chatbot functionality using Llama AI.
   - `model1.py`: Possibly a model script for generating responses or managing interactions.
   - `server.py`: Likely the main server file handling HTTP requests.
   - `summarizer.py`: Script dedicated to summarizing YouTube transcripts.

2. Static Assets:
   - Images: `static/back.jpg` – Background image for the website.
   - JavaScript: `static/script1.js` – Likely controls interactivity or functionality in the web app.
   - CSS Stylesheets: Multiple stylesheets (`style.css`, `style2.css`, etc.) for styling different parts of the interface.

3. HTML Templates:
   - Web Pages: HTML templates in `Templates` folder for `chatbot.html`, `contact.html`, `course.html`, `login.html`, `signup.html`, `summary.html`.

4. Others:
   - Facial-expression-recognition: A folder containing `.git` version control data, possibly for an additional or experimental feature.
   - Compiled Python Cache: The `__pycache__` folder with compiled Python files.

# YouTube Transcript Summarizer and ADHD-Optimized Chatbot

This project is designed specifically to support ADHD students by offering a user-friendly web interface with two main features:
1. A Chatbot powered by Llama AI to help users engage in informative conversations.
2. A YouTube Transcript Summarizer to provide concise summaries of video content, making it easier to grasp and retain information.

The design features ADHD-friendly colors and layouts, optimizing engagement and usability.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
- [File Structure](#file-structure)
- [Usage](#usage)
- [Contributing](#contributing)

## Features
1. Chatbot (Llama AI): Enables users to interact with a supportive AI assistant designed to aid with general queries and support ADHD students' learning needs.
2. YouTube Transcript Summarizer: A tool to summarize YouTube transcripts, providing ADHD students with quick and accessible insights from lengthy videos.

## Getting Started
To run this project locally, you’ll need Python 3.8+ and a few dependencies. Install them by running:
```bash
pip install -r requirements.txt
```

After installation, start the server by running:
```bash
python server.py
```

Then, open your web browser and navigate to `http://localhost:5000` to access the interface.

## File Structure
### Main Files
- chat1.py, chat2.py, llama.py: Files responsible for the chatbot functionality using the Llama AI model.
- model1.py: Provides data handling or processing logic shared by the chatbot and summarizer.
- server.py: The main server file. Routes requests for the chatbot and YouTube summarizer and serves the web interface.
- summarizer.py: Handles fetching and summarizing YouTube transcripts based on user-provided URLs.

### Templates
- Templates/chatbot.html: Web interface for the chatbot.
- Templates/summary.html: Page where users can input a YouTube URL and receive a summarized transcript.
- Templates/contact.html, course.html, login.html, signup.html: Additional pages that help complete the website's structure.

### Static
- static/back.jpg: Background image for an ADHD-friendly visual appeal.
- static/script1.js: JavaScript for added page interactivity.
- static/style.css, style2.css, style3.css, style4.css: Style sheets that customize the appearance of different sections to enhance ADHD accessibility.

## Usage
1. Chatbot: Navigate to the Chatbot page, where you can interact with the Llama AI-powered assistant.
2. YouTube Summarizer: Go to the summarizer page, input a YouTube URL, and receive a concise summary for easy understanding.

## Contributing
Feel free to submit pull requests to improve the design, usability, or functionality, especially if you have insights on optimizing for ADHD support.



Let me know if you would like to customize any parts further!
