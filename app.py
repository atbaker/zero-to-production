from flask import Flask
from twilio import twiml


app = Flask(__name__)

### This is the view I'll code live ... maybe
@app.route('/reply', methods=['POST'])
def reply_to_sms():
    """Replies to incoming text messages sent to our Twilio number"""
    # Start a new TwiML response
    response = twiml.Response()

    # Describe the message body
    response.message("Welcome to Zero to Production in 15 Minutes! More soon...")

    # Send the response to Twilio
    return str(response)

if __name__ == '__main__':
    app.run()
