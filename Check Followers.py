from tweepy import API, Cursor, OAuthHandler, TweepError
import json
import pandas as pd

consumer_key = 'HMOpnrt95Pcdpsj50J8oADr1U'
consumer_secret = '5L4HLlK0lG9nrhRqrZP3cmnFyeKiW2h9mrvnhQAmYAq7OPyUdi'
access_token = '3410829394-kx7FXWegLDi1nNoHt8ctVll7hdjwPzUpTSW8Kg0'
access_secret = 'rhicCpQjqsCeUeibevbJrEttG42Qa9YqPDq7aGOjHWzrA'

# Authenticate Tweepy connection to Twitter API
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def checkFollow(status,user_screenname):
  for z in user_screenname:
    relations = []
    print("Followers of",z,"UserName")
    for i in status:
      try:
        if z not in i:
          user_relation = api.show_friendship(source_screen_name=z, target_screen_name=i)
          dic = user_relation[0]._json
          dic['following_user_name'] = user_relation[1].screen_name
          relations.append(user_relation[0]._json)
          filename = user_relation[0].screen_name + '.json'
          with open('D:/json/'+filename, 'w') as f:
            json.dump(relations, f)
      except:
        print(i, "User not found")
        continue
  return True

df = pd.read_csv('D:/names.csv')
status = df['name'].unique()

user_screenname = df['name'].unique()

r = checkFollow(status,user_screenname)