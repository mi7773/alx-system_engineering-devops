#!/usr/bin/python3
"""
1-top_ten
"""
import requests
import json


def top_ten(subreddit):
    """
    queries Reddit API and prints the titles
    of the first 10 hot posts listed for
    a given subreddit.

    Args:
        subreddit (str): The subreddit.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Custom'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        # d = json.dumps(data, indent=4)
        for i in range(10):
            d = data.get('data', {}).get('children')[i].\
                         get('data', {}).get('title', '')
            print(d)
    else:
        print('None')
