from flask import Flask
from twilio import twiml

app = Flask(__name__)

@app.route('/reply')
def reply_to_text():
    response = twiml.Response()

    response.message('Welcome to the talk! More soon...')

    return str(response)

if __name__ == '__main__':
    app.run(debug=True)
