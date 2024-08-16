#!/usr/bin/python3
"""
1-top_ten
"""
import requests


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
    params = {"limit": 10}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data.get('data', {}).get('children', [])
        for i, post in enumerate(posts[:10]):
            if post.get('kind', '') == 't3':
                print(post.get('data', {}).get('title', ''))
    else:
        print('None')
