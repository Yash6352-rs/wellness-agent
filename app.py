from flask import Flask, render_template, request, send_file, redirect, url_for
from agent_logic import run_agent
import os

app = Flask(__name__)
current_session = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    form = request.form.to_dict()
    result = run_agent(form)

    current_session['category'] = result.get("category", "")
    current_session['summary'] = result.get("status_summary", "")
    current_session['advice'] = result.get("response", "")
    current_session['final_tip'] = result.get("final_tip", "")

    return render_template("result.html",
        category=current_session['category'],
        summary=current_session['summary'],
        advice=current_session['advice'],
        final_tip=current_session['final_tip']
    )

@app.route('/download')
def download_summary():
    os.makedirs("logs", exist_ok=True)
    path = "logs/session_summary.txt"
    with open(path, 'w') as f:
        f.write(f"Category: {current_session['category']}\n\n")
        f.write(f"Summary:\n{current_session['summary']}\n\n")
        f.write(f"Advice:\n{current_session['advice']}\n\n")
        f.write(f"Next Step:\n{current_session['final_tip']}\n")
    return send_file(path, as_attachment=True)

@app.route('/start-over')
def start_over():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
