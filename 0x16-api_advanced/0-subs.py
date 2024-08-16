#!/usr/bin/python3
"""
0-subs
"""
import requests


def number_of_subscribers(subreddit):
    """
    queries Reddit API and returns the number of
    subscribers (not active users, total subscribers)
    for a given subreddit.

    Args:
        subreddit (str): The subreddit.
    Returns:
        int: The number of subscribers.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'Custom'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    else:
        return 0
