#!/usr/bin/python3
'''Get ALL all hot titles for a subreddit'''

import requests

BASE = 'http://reddit.com/r/{}/hot.json'


def recurse(subreddit, hot_list=[], after=None):
    '''Get ALL all hot titles for a subreddit'''
    headers = {'User-agent': 'Unix:0-subs:v1'}
    params = {'limit': 100}
    if isinstance(after, str):
        if after != "STOP":
            params['after'] = after
        else:
            return hot_list
    response = requests.get(BASE.format(subreddit),
                            headers=headers, params=params)
    if response.status_code != 200:
        return None
    data = response.json().get('data', {})
    after = data.get('after', 'STOP')
    if not after:
        after = "STOP"
    hot_list = hot_list + [post.get('data', {}).get('title')
                           for post in data.get('children', [])]
    return recurse(subreddit, hot_list, after)
