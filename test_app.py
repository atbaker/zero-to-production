from app import reply_to_text

def test_foo():
    response = reply_to_text()
    
    assert 'Welcome to the talk!' in response
