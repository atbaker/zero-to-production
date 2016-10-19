from app import reply


def test_reply_view():
    response = reply()

    assert '<Body>Welcome to the talk!</Body>' in response
