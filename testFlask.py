import json

from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def hello_world():
    return Response(json.dumps({"stado": "Hello world"}), status=200, mimetype="application/")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)