from flask_testing import TestCase
from app import create_app
from app.models import Tweet
from app.db import tweet_repository

class TestTweetViews(TestCase):
    def create_app(self):
        app = create_app()
        app.config['TESTING'] = True
        return app

    def setUp(self):
        tweet_repository.tweets.clear() # Make sure each test starts with an empty database
        tweet_repository.next_id = 1

    def test_tweet_show(self):
        tweet_repository.tweets.clear()
        first_tweet = Tweet("First tweet")
        tweet_repository.add(first_tweet)
        response = self.client.get("/api/v1/tweets/1")
        response_tweet = response.json
        self.assertEqual(response_tweet["id"], 1)
        self.assertEqual(response_tweet["text"], "First tweet")
        self.assertIsNotNone(response_tweet["created_at"])

    def test_201_when_creating_tweet(self):
        tweet_repository.tweets.clear()
        response = self.client.post('/api/v1/tweets/', data=dict(text='Mon tweet en francais'))
        self.assertEquals(response.status_code,201)
        response_tweet = response.json
        self.assertEqual(response_tweet["text"], "Mon tweet en francais")
        self.assertIsNotNone(response_tweet["created_at"])

    def test_422_if_empty(self):
        tweet_repository.tweets.clear()
        response = self.client.post('/api/v1/tweets/', data=dict(text=''))
        self.assertEquals(response.status_code,422)
        response = self.client.post('/api/v1/tweets/')
        self.assertEquals(response.status_code,422)

