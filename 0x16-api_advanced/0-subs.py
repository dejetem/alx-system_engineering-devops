#!/usr/bin/python3
'''Get number of channel subscribers in reddit'''

import requests

BASE = 'http://reddit.com/r/{}/about.json'


def number_of_subscribers(subreddit):
    '''Gets number of subscribers'''
    headers = {'User-agent': 'Unix:0-subs:v1'}
    response = requests.get(BASE.format(subreddit),
                            headers=headers)
    if response.status_code != 200:
        return 0
    return response.json().get('data', {}).get('subscribers', 0)
