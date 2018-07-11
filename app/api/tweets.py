from flask import Blueprint, jsonify
from app.db import tweet_repository

api = Blueprint('tweets', __name__)

@api.route('/tweets/<int:id>')
def show(id):
    tweet = tweet_repository.get(id)
    return jsonify({
        "id": tweet.id,
        "text": tweet.text,
        "created_at": tweet.created_at
    })
