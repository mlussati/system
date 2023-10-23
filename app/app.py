from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_world():
    return 'Hello, Educative Learner! This is version 2.0'