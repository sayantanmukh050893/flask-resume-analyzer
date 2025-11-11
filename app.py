from flask import Flask, render_template, request
from utils.resume_parser import extract_text_from_pdf
from utils.nlp_analyzer import analyze_resume
from utils.job_fetcher import fetch_jobs

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['resume']
    text = extract_text_from_pdf(file)
    skills, summary = analyze_resume(text)
    jobs = fetch_jobs(skills)
    return render_template('result.html', skills=skills, summary=summary, jobs=jobs)

if __name__ == '__main__':
    app.run(debug=True)
