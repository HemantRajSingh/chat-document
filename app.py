from flask import Flask, render_template, request, session
import PyPDF2
from dotenv import load_dotenv
import os
from werkzeug.utils import secure_filename
import openai

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}


app = Flask(__name__)
app.config['UPLOADS_DEFAULT_DEST'] = UPLOAD_FOLDER

print("Current working directory:", os.getcwd())
print("UPLOADS_DEFAULT_DEST:", app.config['UPLOADS_DEFAULT_DEST'])


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    print('here check')
    if 'pdf' in request.files:
        pdf = request.files['pdf']
        if pdf.filename == '':
            return 'No selected file'
        if pdf:
            pdf_path = os.path.join(app.config['UPLOADS_DEFAULT_DEST'], pdf.filename)
            pdf.save(pdf_path)
            # Process the PDF file, extract text, etc.
            # You can use PyPDF2 or other libraries to handle PDFs
            process_pdf_and_save_text(pdf_path)
            return 'File uploaded successfully'
    return 'No PDF file uploaded'

def process_pdf_and_save_text(pdf_file):
    text = ''
    try:
        reader = PyPDF2.PdfReader(pdf_file)
    except Exception as e:
        print(e)

    num_pages = len(reader.pages)
    for page_num in range(num_pages):
        page = reader.pages[page_num]
        text += page.extract_text()
    # Save text to session
    session['pdf_text'] = text
    print(text)
    return text

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
    app.run()
