from twilio.rest import TwilioRestClient

import os, sys


TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER')

# Instantiate our Twilio client
client = TwilioRestClient()

def get_audience_numbers():
    """Retrieves the phone numbers of audience members who have texted in"""
    # Get all the messages we've received on our Twilio number
    messages = client.messages.list(To=TWILIO_NUMBER)

    # Extract the 'from' number from each message we have received
    audience_numbers = set()
    for message in messages:
        audience_numbers.add(message.from_)

    return audience_numbers

flask = """
Some helpful links, just for you my friend:

- Flask: http://bit.ly/1eU7R5M
- twilio-python: http://bit.ly/1pKlW3E
- Twilio tutorial: http://bit.ly/1Rk4ywF"""

testing = """
Oh, interested in testing?

- py.test http://bit.ly/1UdIVR1
- coverage.py http://bit.ly/1MERWLa
- Unit testing web apps http://bit.ly/1UOSyEJ
"""


def send_helpful_links(section):
    """Sends some helpful links to the audience for a section in the presentation"""
    # Get the audience numbers
    numbers = get_audience_numbers()

    # Yes, this is dangerous and foolish
    body = eval(section)

    for number in numbers:
        client.messages.create(
            to=number,
            from_=TWILIO_NUMBER,
            body=body,
        )

    print('Sent helpful links to {} people'.format(len(numbers)))

if __name__ == '__main__':
    send_helpful_links(sys.argv[1])
