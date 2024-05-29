
#from flask import Flask, request, render_template
#import subprocess

#app = Flask(__name__)

#@app.route('/')
#def index():
    #return render_template('index.html')

#@app.route('/search', methods=['POST'])
#def search():
    #query = request.form['query']
    #result = subprocess.run(['./search.sh', query], capture_output=True, text=True)
    #return f'<pre>{result.stdout}</pre>'

#if __name__ == '__main__':
    #app.run(debug=True)

#---------------------------------------

import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

def search(query):
    # 'grep'コマンドを使用してテキストファイル内でクエリを検索する
    result = subprocess.run(['grep', query, 'data.txt'], capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout
    else:
        return "No results found."

@app.route('/search', methods=['GET'])
def perform_search():
    query = request.args.get('query')
    if query:
        result = search(query)
        return jsonify({'result': result})
    else:
        return jsonify({'error': 'Query parameter is missing'}), 400

if __name__ == '__main__':
    app.run(debug=True)
