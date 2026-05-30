from flask import Flask, request, jsonify
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

MONGO_URI = os.getenv('MONGO_URI')
client = MongoClient(MONGO_URI)
db = client['Record']
collection = db['users']

# Change 1: Listen on /submit instead of /
@app.route('/submit', methods=['POST'])
def submit_form():
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No data provided"}), 400

    name = data.get('name')
    email = data.get('email')
    
    try:
        collection.insert_one({"name": name, "email": email})
        return jsonify({"message": "Data submitted successfully"}), 201
    except PyMongoError as e:
        return jsonify({"error": "Database error: Could not submit data."}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)