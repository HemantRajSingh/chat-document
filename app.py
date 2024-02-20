from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
from werkzeug.utils import secure_filename
import openai

openai.api_key = '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'

UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = {'pdf'}


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'pdf' in request.files:
        pdf = request.files['pdf']
        pdfs.save(pdf)
        # Process PDF and extract text
        # Save text to database
        return "PDF uploaded successfully"
    return "No PDF found in request"

@app.route('/ask', methods=['POST'])
def ask_question():
    request.form['question']
    # Retrieve text from database
    # Use OpenAI embeddings to find answer
    # Return answer
    return "Answer"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(debug=True)
