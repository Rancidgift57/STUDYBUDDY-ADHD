from flask import Flask, render_template
from flask import request, jsonify
from langchain_groq import ChatGroq
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
import re
import psycopg2
import logging


app = Flask(__name__)

DB_NAME = 'adhd study'
DB_USER = 'postgres'
DB_PASSWORD = 'root'
DB_HOST = 'localhost'  # or your database host
DB_PORT = '5432'       # or your database port

def connect_to_database():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    return conn

def insert_data(conn, name, email,password):
    cursor = conn.cursor()
    sql = "INSERT INTO adhdtab(name, email,password) VALUES (%s, %s,%s)"
    cursor.execute(sql, (name, email,password))
    conn.commit()
    cursor.close()

@app.route('/submit', methods=['POST'])
def submit_form():
    conn = connect_to_database()

    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    insert_data(conn, name, email,password)
    conn.close()
    return render_template("login.html")



@app.route('/')
def home():
    return render_template('login.html')

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

@app.route('/courses')
def courses():
    return render_template('course.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

# Optional catch-all route for additional pages

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Initialize the ChatGroq model
llm = ChatGroq(
    temperature=0,
    groq_api_key="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",
    model_name="llama-3.1-70b-versatile"
)

@app.route('/send_message', methods=['POST'])
def send_message():
    try:
        user_message = request.json['message']
        logging.debug(f"Received message from user: {user_message}")

        # Use the model to generate a response
        response = llm.invoke(user_message)
        logging.debug(f"Generated response from model: {response.content}")

        return jsonify({'response': response.content})
    except Exception as e:
        logging.error(f"Error in send_message: {e}")
        return jsonify({'response': 'An error occurred while processing your message.'}), 500


def extract_video_id(youtube_url):
    """Extracts video ID from a YouTube URL."""
    pattern = r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)|youtu\.be\/)([0-9A-Za-z_-]{11})"
    match = re.search(pattern, youtube_url)
    return match.group(1) if match else None

summarizer = pipeline("summarization", device=-1)



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
