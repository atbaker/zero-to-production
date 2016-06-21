from twilio.rest import TwilioRestClient

import os, sys


TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER')

# Helpful link content
FLASK = """
Some helpful links:

- Flask: http://bit.ly/1eU7R5M
- twilio-python: http://bit.ly/1pKlW3E
- Ngrok: https://ngrok.com/"""

TESTING = """
Interested in testing?

- py.test http://bit.ly/1UdIVR1
- coverage.py http://bit.ly/1MERWLa
- Unit testing web apps http://bit.ly/1UOSyEJ"""

CI = """
Continuous Integration (CI) and Travis resources:

- CI overview http://bit.ly/28LwM2A
- Travis http://bit.ly/28MY5Nt
- Coveralls https://coveralls.io/"""

HEROKU = """
Deployment and Heroku:

- Deploying http://bit.ly/28Ob0Nr
- Heroku http://bit.ly/28Ni1h9"""

CONTACT = """
Thanks for coming out tonight! Helpful links:

- Repo http://bit.ly/28LJgrM
- My Twitter https://twitter.com/andrewtorkbaker
- My email abaker@twilio.com"""

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

def send_helpful_links(section):
    """Sends some helpful links to the audience for a section in the presentation"""
    # Get the audience numbers
    numbers = get_audience_numbers()

    # Yes, this is dangerous and foolish
    body = eval(section.upper())

    for number in numbers:
        client.messages.create(
            to=number,
            from_=TWILIO_NUMBER,
            body=body,
        )

    print('Sent helpful links to {} people'.format(len(numbers)))

if __name__ == '__main__':
    send_helpful_links(sys.argv[1])
