from flask import Blueprint, jsonify, abort, request
from app.db import tweet_repository
from app.models import Tweet

api = Blueprint('tweets', __name__)

@api.route('/tweets/<int:id>')
def show(id):
    tweet = tweet_repository.get(id)
    return jsonify({
        "id": tweet.id,
        "text": tweet.text,
        "created_at": tweet.created_at
    })

@api.route('/tweets/', methods=['POST'])
def add_tweet():
    try:
        text = request.form['text']
    except:
        abort(422)
    if not text:
        abort(422)
    tweet_repository.add(Tweet(text))
    my_tweet = show(tweet_repository.next_id - 1)
    return (show(tweet_repository.next_id - 1), 201)
