#!/usr/bin/python3

import json
from InstagramAPI import InstagramAPI
with open('./conf.json') as file:
    conf = json.load(file)

def getFollowers(api, user_id):
    followers = []
    next_id = True
    while next_id:
        if next_id is True:
            next_id = ''
        api.getUserFollowers(user_id, maxid=next_id)
        res = api.LastJson
        for user in res.get('users', []):
            followers.append(user['username'])
        next_id = res.get('next_max_id', '')
    return followers

def getFollowings(api, user_id):
    followings = []
    next_id = True
    while next_id:
        if next_id is True:
            next_id = ''
        api.getUserFollowings(user_id, maxid=next_id)
        res = api.LastJson
        for user in res.get('users', []):
            followings.append(user['username'])
        next_id = res.get('next_max_id', '')
    return followings

api = InstagramAPI(conf['username'], conf['password'])
api.login()
user_id = api.username_id

followers = getFollowers(api, user_id)
followings = getFollowings(api, user_id)

print("%s followers (users who follow the account)." % len(followers))
print("%s followings (users subscribed by the account)." % len(followings))
print("\n")

followersOnly = list(set(followers) - set(followings))
followingsOnly = list(set(followings) - set(followers))
print("%i followersOnly : %s\n" % (len(followersOnly), json.dumps(followersOnly)))
print("%i followingsOnly : %s\n" % (len(followingsOnly), json.dumps(followingsOnly)))
