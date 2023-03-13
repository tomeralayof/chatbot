#app.py
from flask import Flask
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/send-message", methods = ["POST"])
def userMessage():
    message = request.json.get("message")
    return jsonify(message)