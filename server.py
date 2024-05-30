from flask import Flask, request, send_from_directory
from search import search_files

app = Flask(__name__)

# Route to serve the radioSearch.html
@app.route('/')
def index():
    return send_from_directory('.', 'radioSearch.html')

# Route to handle search requests
@app.route('/search')
def search():
    search_term = request.args.get('term', '')
    if search_term:
        result = search_files(search_term)
        return result if result else "No matches found."
    else:
        return "No search term provided.", 400

if __name__ == '__main__':
    app.run(debug=True)
