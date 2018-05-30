# instagram_diff

## Description
This script will tell you the users specific to each one of your lists on Instagram : followers & following.

## Requirements
* Python 2.6+
* [Instagram module for Python](https://github.com/LevPasha/Instagram-API-python) (pip install InstagramApi)

## Execution
First, create a conf.json file with you application keys and the tokens of the account you want to treat.
Then, just launch the script diff.py, it will return something like that :
```

5623 followers (users who follow the account).
8422 followings (users subscribed by the account).

528 followersOnly : [ <usernames list> ]

256 followingsOnly : [ <usernames list> ]
```
