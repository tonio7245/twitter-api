from flask import Flask
from .db import tweet_repository
from .models import Tweet


tweet_repository.add(Tweet("a first tweet"))
tweet_repository.add(Tweet("a second tweet"))

def create_app():
    app = Flask(__name__)

    from .main.controllers import main
    app.register_blueprint(main)

    from .api.tweets import api as tweet_api
    app.register_blueprint(tweet_api, url_prefix = "/api/v1")

    return app
