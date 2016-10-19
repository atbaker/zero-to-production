from flask import Flask
from twilio import twiml


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/reply', methods=['GET', 'POST'])
def reply():
    """Replies to text messages our Twilio number receives"""
    response = twiml.Response()
    response.message('Welcome to the talk!')

    return str(response)

if __name__ == "__main__":
    app.run()
