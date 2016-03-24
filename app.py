from flask import Flask
from twilio import twiml

from utils import get_audience_numbers


app = Flask(__name__)

### This is the view I'll code live ... maybe
@app.route('/reply')
def reply_to_sms():
    """Replies to incoming text messages sent to our Twilio number"""
    # Start a new TwiML response
    response = twiml.Response()

    # Describe the message body
    response.message("Welcome to Zero to Production in 15 Minutes! More soon...")
    return str(response)

@app.route('/send/<section>')
def send_helpful_links(section=None): # =None for now
    """Sends helpful links to the audience for a given section in the presentation"""
    # Get the phone numbers that have texted in today
    audience_numbers = get_audience_numbers()

    # Send them all some helpful links
    

if __name__ == '__main__':
    app.run()
