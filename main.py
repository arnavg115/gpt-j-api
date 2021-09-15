from flask import Flask,request,jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
@app.route('/')
def main():
    return 'Hello world'

@app.route("/gen",methods=["POST"])
def generate():
    json = request.get_json(True)
    context = json["context"]
    temprature = json["temp"]
    payload = {
        "context": context,
        "token_max_length": 100,
        "temperature": temprature,
        "top_p": 1,
    }
    response = requests.post("http://api.vicgalle.net:5000/generate", params=payload).json()
    return jsonify(response)

if '__main__' == __name__:
    app.run(host="0.0.0.0",port=5000)