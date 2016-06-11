from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from pymongo import MongoClient
import json

consumer_key = "MtHsM6e0jpbeRNTNOwKOjcBUF"
consumer_secret = "kvhhRaI0b1DpjMm6HPxJCFpdL0ihwCCfLMKas4UQA6qvm13K5K"
access_token = "115246381-w1E4EqjndQ0LAnCotvldnRGiXWZdk0GbN5QftQQB"
access_token_secret = "dc1vaGAVAxnwL8UcZJR9A05Y232DGZXw16SioE7l3yDYK"

client = MongoClient('localhost', 27017)
db = client['twitter_db']
collection = db['tw_france']

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        tweet = json.loads(data)
        print (tweet['text'])
        collection.insert(tweet)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)

    stream.filter(locations=[-3.544998,43.253929,9.310981,50.706172])#lng,lat