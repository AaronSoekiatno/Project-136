from data import Dict
from flask import Flask, jsonify, request

app = Flask(__name__)
@app.route('/')
def index():
    return jsonify({
        "data":Dict,
        "message": "success",
    })

if __name__ == '__main__':
    app.run()
