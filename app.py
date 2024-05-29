from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    result = subprocess.run(['./search.sh', query], capture_output=True, text=True)
    return f'<pre>{result.stdout}</pre>'

if __name__ == '__main__':
    app.run(debug=True)
