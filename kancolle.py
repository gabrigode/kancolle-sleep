import tweepy
import os
from os import environ
import time
import random

#Variables used in array
os.chdir ('images')
count = 1
message = []

#Keys to API
consumer_key = environ['consumer_key']
consumer_secret = environ['consumer_secret']
access_token = environ['access_token']
access_token_secret = environ['access_token_secret']

#Auth to API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)    
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print (user.name)

while True:
    search = api.search(q='@KancolleSleep')
    for tweet in search:
        print (f'UserName: {tweet.user.screen_name}')
        name = tweet.user.screen_name
        if (tweet.id) in message:
            print ("Tweet already answered!")
        else:
            print ("Sending reply...")
            message.insert (count+1, tweet.id)
            print (f'Tweet: {tweet.text}')
            media_ids = []
            image1 = random.choice(os.listdir('.'))
            file = api.media_upload(image1)
            media_ids.append(file.media_id)
            print (image1)
            text = (f'@{name}')
            api.update_status(status=text, media_ids=media_ids, in_reply_to_status_id=tweet.id)
           
    time.sleep(15)
