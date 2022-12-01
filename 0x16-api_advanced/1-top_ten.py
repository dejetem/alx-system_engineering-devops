#!/usr/bin/python3
'''Get top 10 latest post in hot listing'''

import requests

BASE = 'http://reddit.com/r/{}/hot.json'


def top_ten(subreddit):
    '''Get top 10 latest post in hot listing'''
    headers = {'User-agent': 'Unix:0-subs:v1'}
    response = requests.get(BASE.format(subreddit),
                            headers=headers)
    data = response.json().get('data', {}).get('children', {})
    if response.status_code != 200 or not data:
        return print("None")
    for post in data[0:10]:
        print(post.get('data', {}).get('title'))
