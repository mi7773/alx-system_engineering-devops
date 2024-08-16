#!/usr/bin/python3
"""
2-recurse
"""
import json
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """
    queries Reddit API and returns a list containig
    the titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The subreddit.
        hot_list (list): The hot list.
        count (int): The count
        after (str): The after
    Returns:
        list: The list containing the titles.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Custom'}
    params = {"limit": 10, 'count': count, 'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    results = hot_list
    if response.status_code == 200:
        data = response.json()
        temp = [child.get('data', {}).get('title', '')
                for child in data.get('data', {}).get('children', [])]
        results.extend(temp)
        count = len(results)
        after = data.get('data', {}).get('after')
        if not after:
            return results
        return recurse(subreddit, hot_list=results, count=count, after=after)
    else:
        return None
