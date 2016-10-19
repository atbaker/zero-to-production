# Zero to Production Notes

## Section 0: Intro

### Today

1. A quick but complete tour of how I would put an app in production
1. We're going to hit a lot of areas quickly, but we'll have time for questions
1. Take notes on "what" and "why," but don't bother with "how"
1. Don't take it as gospel - you'll need to make your own choices

## Section 1: Flask

### Set up Flask
1. Flask website
1. `mkvirtualenv -p python3 zero-to-production`
1. `pip install Flask`
1. Create `app.py`
1. `python app.py`
1. Check http://localhost:5000/

### Set up Twilio
1. Twilio website
1. Buy a phone number
1. `pip install twilio`
1. twilio-python docs
1. Create `/reply` view

    ```python
    @app.route('/reply', methods=['GET', 'POST'])
    def reply():
        """Replies to text messages our Twilio number receives"""

        response = twiml.Response()
        response.message('Welcome to the talk!')

        return str(response)
    ```
1. Run server, check http://localhost:5000/reply

### Set up Ngrok
1. Talk about webhooks
1. Talk about ngrok
1. Start ngrok, webserver
1. Update Twilio number webhook
1. Invite everyone to send a text message to the number

### Links
1. Add phone number to `.env`
1. `source .env`
1. `python links.py flask`

### Cleanup
1. `pip freeze > requirements.txt`
1. `git add -A .`
1. `git commit -m "Section one"`

**Pause for one or two questions**

## Section 2: Testing

### Stub test
1. *Briefly* mention why testing is important
    1. Testing my own code GIF
    1. Testing in production GIF
    1. Somewhat religious subject
    1. My philosophy: "Any tests are better than no tests"
1. py.test website, quickstart
1. `pip install pytest pytest-cov`
1. `touch test_app.py`

    ```python
    def test_reply_view():
        pass
    ```
1. `py.test --cov`
1. `coverage html`
1. `open htmlcov/index.html`

### Real test
1. Add `from app import reply`
1. Write test with pdb

    ```
    def test_reply_view():
        response = reply()

        import pdb; pdb.set_trace()
    ```
1. `py.test --cov`
1. Debug response, check assert statement
1. Remove pdb and add
    ```python
    assert '<Body>Welcome to the talk!</Body>' in response
    ```
1. `py.test --cov`
1. `coverage html`
1. Look at coverage report again

### Links
1. `python links.py testing`

### Cleanup
1. `pip freeze > requirements.txt`
1. `git add -A .`
1. `git commit -m "Section two"`

**Pause for one or two questions**

## Section 3: Continuous Integration

### Travis CI

1. Travis website (incognito)
1. Anti-voicemail repo
1. Add repo "zero-to-production"
1. Travis Python docs
1. `touch .travis.yml`

    ```yml
    language: python
    python:
      - '3.5'
    install:
      - pip install -r requirements.txt
    script: 
      - py.test --cov
    ```
1. `git add .travis.yml`
1. `git commit -m "Adding travis.yml"`
1. `git push origin sf-python`
1. Open https://travis-ci.org/atbaker/zero-to-production/builds
1. While building, grab the badge

### Coveralls

1. Coveralls website
1. Add repo "zero-to-production"
1. In `.travis.yml`

    ```yml
    install:
      - pip install coveralls
    after_success:
      - coveralls
    ```
1. `git add .travis.yml`
1. `git commit -m "Adding coveralls"`
1. `git push origin sf-python`
1. Open Travis builds
1. While building, grab coveralls badge

### Links
1. `python links.py ci`

**Pause for one or two questions**

## Section 4: Heroku

### Heroku
1. Heroku website
    - Lots of ways to deploy apps, but Heroku's a good one
1. Heroku Python getting started guide
1. Heroku command line tool
1. 

### Procfile
1. `heroku create`
1. `pip install gunicorn`
1. `pip freeze > requirements.txt`
1. `gunicorn app:app`
1. `touch Procfile`

    ```
    web: gunicorn app:app --log-file -
    ```
1. Update view to say: `'Now deployed on Heroku!'
1. `git add .`
1. `git commit -m "Configuring for Heroku"`
1. `git push origin sf-python`
1. `git push heroku sf-python:master`
1. `heroku open`

### Update our Twilio number
1. Go to number in console
1. Replace Messaging URL with Heroku URL
1. Send a quick text message to test
1. `heroku logs -t`

### Links
1. `python links.py heroku`

## Section 4.1: Fix the build

1. Look at Travis CI badge - it's broken
1. We need to go back and fix our test!
1. Fix the test
1. `git add .`
1. `git commit -m "Fixing test"`
1. `git push origin sf-python`

## Section 5: Wrap-up

- This is just one way to do things
- Hopefully you got something out of it

`python links.py contact`
