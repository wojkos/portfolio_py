import re
import os
import json
import requests
from urllib.parse import urljoin

USERS_API = 'https://api.github.com/users/'


class Twitter:
    version = '1.0'

    def __init__(self, backend=None, username=None):
        self.__tweets = []
        self.backend = backend
        self.username = username

    def tweet(self, message):
        if len(message) > 160:
            raise Exception('Message too long')
        self.tweets.append({
            "message": message,
            "avatar": self.get_user_avatar(),
            "hashtags": self.find_hashtags(message)
        })
        if self.backend:
            self.backend.write(json.dumps(self.tweets))

    def find_hashtags(self, message):
        return re.findall(r"#(\w+)", message)

    def get_user_avatar(self):
        if not self.username:
            return None

        url = urljoin(USERS_API, self.username)
        resp = requests.get(url)
        return resp.json()["avatar_url"]

    @property
    def tweets(self):
        if self.backend and not self.__tweets:
            backend_text = self.backend.read()
            if backend_text:
                self.__tweets = json.loads(backend_text)
        return self.__tweets

    @property
    def tweet_messages(self):
        return [tweet['message'] for tweet in self.tweets]


t = Twitter(username='python')
t.tweet('Hello')

print(t.tweets)
