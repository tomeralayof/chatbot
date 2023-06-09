#app.py
from flask import Flask
from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbotResponse import getResponse

app = Flask(__name__)
CORS(app)

@app.route("/", methods = ["GET"])
def foo():
    return "HELLO WORLD"

@app.route("/send-message", methods = ["POST"])
def userMessage():
    message = request.json.get("message")
    response = {"message": str(getResponse(message))}
    return jsonify(response)