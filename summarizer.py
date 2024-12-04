from flask import Flask, render_template, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
import re

app = Flask(__name__)

# Load the summarization pipeline using PyTorch (device=-1 means using CPU)
summarizer = pipeline("summarization", device=-1)

def extract_video_id(youtube_url):
    """Extracts video ID from a YouTube URL."""
    pattern = r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)|youtu\.be\/)([0-9A-Za-z_-]{11})"
    match = re.search(pattern, youtube_url)
    return match.group(1) if match else None

def get_transcript(video_id):
    """Fetches the transcript for a given YouTube video ID."""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = " ".join([entry['text'] for entry in transcript])
        return transcript_text
    except Exception as e:
        print(f"An error occurred while fetching the transcript: {e}")
        return None

def summarize_script(text, max_length=150, min_length=50):
    """Summarizes the YouTube script content."""
    try:
        summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
        summary_text = summary[0]['summary_text']
        return summary_text
    except Exception as e:
        print(f"An error occurred while summarizing the script: {e}")
        return "Error summarizing the script."

@app.route('/')
def index():
    return render_template('summary.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    youtube_url = request.json.get('youtube_url')
    
    video_id = extract_video_id(youtube_url)
    if not video_id:
        return jsonify({'error': 'Invalid YouTube URL'}), 400

    youtube_script = get_transcript(video_id)
    if not youtube_script:
        return jsonify({'error': 'Could not fetch transcript'}), 500

    summary = summarize_script(youtube_script)
    
    return jsonify({'summary': summary})

if __name__ == '__main__':
    app.run(debug=True)