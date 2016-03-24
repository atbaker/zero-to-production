from app import reply_to_sms

def test_reply_to_sms():
    # Simulate a request to our view
    response = reply_to_sms()

    # Make sure the response looks right
    assert '<Response>' in response
    assert 'Welcome to Zero' in response
