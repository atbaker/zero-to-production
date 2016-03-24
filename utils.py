from twilio.rest import TwilioRestClient

import os


def get_audience_numbers():
    """Retrieves the phone numbers of audience members who have texted in"""
    # Instantiate our Twilio client
    client = TwilioRestClient()

    # Get all the messages we've received on our Twilio number
    twilio_number = os.environ.get('TWILIO_NUMBER')
    messages = client.messages.list(To=twilio_number)

    # Extract the 'from' number from each message we have received
    audience_numbers = set()
    for message in messages:
        audience_numbers.add(message.from_)

    return audience_numbers
