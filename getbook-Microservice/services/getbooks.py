from flask import Flask, jsonify
import os
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True, origins='*', allow_headers=['Content-Type', 'Authorization'])
app.config['SECRET_KEY'] = os.urandom(24)
port = int(os.environ.get('PORT', 5001))

# File path for the books JSON file
BOOKS_FILE = os.path.join(os.path.dirname(__file__), 'books.json')

@app.route("/")
def home():
    return "Hello, this is a Flask Microservice for Books"

@app.route('/books', methods=['GET'])
def get_books():
    try:
        with open(BOOKS_FILE, 'r') as f:
            books_data = json.load(f)
        return jsonify(books_data), 200
    except FileNotFoundError:
        return jsonify({'error': 'Books file not found'}), 404
    except json.JSONDecodeError:
        return jsonify({'error': 'Error decoding JSON file'}), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=port)
