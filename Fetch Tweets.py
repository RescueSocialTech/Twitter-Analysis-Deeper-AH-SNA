import tweepy
from tweepy import API, Cursor, OAuthHandler, TweepError
import json
import pandas as pd
import pickle
import time

consumer_key = 'HMOpnrt95Pcdpsj50J8oADr1U'
consumer_secret = '5L4HLlK0lG9nrhRqrZP3cmnFyeKiW2h9mrvnhQAmYAq7OPyUdi'
access_token = '3410829394-kx7FXWegLDi1nNoHt8ctVll7hdjwPzUpTSW8Kg0'
access_secret = 'rhicCpQjqsCeUeibevbJrEttG42Qa9YqPDq7aGOjHWzrA'

# Authenticate Tweepy connection to Twitter API
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

n =1

def text(status):
  for i in status:
      twtlst = []
      keyword = i
      num = 3000
      text = keyword + ".txt"
      print("UserName",keyword)
      try:
          for tweet in tweepy.Cursor(api.user_timeline, id=keyword).items():
              twtlst.append(tweet)
          with open('D:/json_text/'+text, "wb") as fp:
              pickle.dump(twtlst, fp)
      except:
          continue
          time.sleep(60)
  return True

df = pd.read_csv('D:/names1.csv')
status = df['name'].unique()

r = text(status)