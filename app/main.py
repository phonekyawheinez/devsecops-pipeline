
from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify({
        "application": "DevSecOps Demo",
        "status": "running",
        "message": "Welcome to our CI/CD pipeline!"
    })


@app.get("/health")
def health():
    return jsonify({
        "status": "healthy"
    }), 200
