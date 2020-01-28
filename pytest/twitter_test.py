import pytest
import requests
from twitter import Twitter
from unittest.mock import patch
from unittest.mock import Mock, MagicMock


class ResponseGetMock:
    def json(self):
        return {"avatar_url": "test"}


@pytest.fixture(params=[None, "Python"])
def username(request):
    return request.param

# scope: "function","session", "module
@pytest.fixture(scope="function", params=["list", "backend"], name="twitter")
def fixture_twitter(backend, username, request, monkeypatch):
    if request.param == "list":
        twitter = Twitter(username=username)
    elif request.param == "backend":
        twitter = Twitter(backend=backend, username=username)

    return twitter


def test_twitter_initialization(twitter):
    assert twitter


@patch.object(requests, 'get', return_value=ResponseGetMock())
def test_tweet_single_message(avatar_mock, twitter):
    twitter.tweet("Test")
    assert twitter.tweet_messages == ["Test"]


def test_tweet_long_single_message(twitter):
    with pytest.raises(Exception):
        twitter.tweet("Test" * 42)
    assert twitter.tweet_messages == []


@pytest.mark.parametrize("message, expected", (
    ("Test #first", ["first"]),
    ("#first test", ["first"]),
    ("#FIRST test", ["FIRST"]),
    ("Test #first test", ["first"]),
    ("Test #first test #second", ["first", "second"]),
))
def test_tweet_with_hastag(twitter, message, expected):
    assert twitter.find_hashtags(message) == expected


def test_initialize_two_twitter_classes(backend):
    twitter1 = Twitter(backend=backend)
    twitter2 = Twitter(backend=backend)

    twitter1.tweet("Test 1")
    twitter1.tweet("Test 2")

    assert twitter2.tweet_messages == ["Test 1", "Test 2"]


@patch.object(requests, 'get', return_value=ResponseGetMock())
def test_tweet_with_username(avatar_mock, twitter):
    if not twitter.username:
        pytest.skip()

    twitter.tweet("Test message")
    assert twitter.tweets == [
        {"message": "Test message", "avatar": "test", "hashtags": []}]
    avatar_mock.assert_called()  # test if mock was called


@patch.object(requests, 'get', return_value=ResponseGetMock())
def test_tweet_with_hashtag_mock(avatar_mock, twitter):
    twitter.find_hashtags = Mock()
    twitter.find_hashtags.return_value = ['first']
    twitter.tweet('Test #second')
    assert twitter.tweets[0]["hashtags"] == ['first']
    twitter.find_hashtags.assert_called_with('Test #second')


def test_twitter_version(twitter):
    twitter.version = MagicMock()
    twitter.version.__eq__.return_value = '2.0'
    assert twitter.version == '2.0'
