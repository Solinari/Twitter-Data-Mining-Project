# Twitter Crawler


import twitter
import json

# storing my keys in a text file on my system for this project
def Oauth_logon():
    '''One would have to set up their developer app through twitter
    to obtain these keys and tokens. I have left these blank since
    those keys and tokens are linked to one of my accounts.
    Twitter does rate limit you after about 15 queries in 15 minutes'''
    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''
    OAUTH_TOKEN = ''
    OAUTH_TOKEN_SECRET = ''

    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                               CONSUMER_KEY, CONSUMER_SECRET)

    # defines twitter api as an object variable
    mytwitter = twitter.Twitter(auth=auth)

    return mytwitter

mytwitter = Oauth_logon()

# this will return a json object that contains a large amount
# of metadata for each post on the user's timeline.
# it would be interesting to make a list of timeline objects(since they are json)
# with another list of known user names I mined, and then query all of their
# timelines as each each element of the list
this_timeline =  mytwitter.statuses.user_timeline(screen_name = 'name_goes_here')


for i in range(len(this_timeline)):
    # return every text in a user's timeline
    # you have to use json.dumps to extract the strings from the json
    print i
    print json.dumps(this_timeline[i]["text"], indent = 1)
    

# next steps:
# 1) continue refining with what I want to extract
# 2) possibilities for data storage: strongly considering pymongo for this
# 3) working with twitter api for oauth 'dance' to keep a bot that moniters and collects data in an ongoing manner

