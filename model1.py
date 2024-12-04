from flask import Flask, render_template, request, jsonify
from langchain_groq import ChatGroq
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Initialize the ChatGroq model
llm = ChatGroq(
    temperature=0,
    groq_api_key="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",
    model_name="llama-3.1-70b-versatile"
)

@app.route('/')
def index():
    return render_template('chatbot.html')

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

if __name__ == '__main__':
    app.run(debug=True)
