from app import reply


def test_reply_view():
    response = reply()

    assert '<Body>Now deployed on Heroku :D</Body>' in response
