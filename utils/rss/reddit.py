import os
import requests

"""
Reddit
    Append .rss at the end of a URL:

    Front page: https: //reddit .com/.rss
    Subreddit:
        reddit.com/r/{subreddit}.rss
        reddit.com/r/LifeProTips/top.rss
        reddit.com/r/{subreddit}/{sort}.rss
"""

def get_reddit_front_page():
    response = requests.get("https://reddit.com/.rss")
    if response.status_code != 200:
        # Or Raise Error
        # raise ConnectionError
        return None
    return response

def get_subreddit(subreddit_name: str, sort: str=None):
    valid_sort = [
        "top",
        "new",
        "hot"
    ]

    built_url = f"reddit.com/r/{subreddit_name}.rss"

    if sort in valid_sort and sort is not None:
        built_url = f"reddit.com/r/{subreddit_name}/{sort}.rss"

    response = requests.get(f"https://{built_url}")
    if response.status_code != 200:
        # Or Raise Error
        # raise ConnectionError
        return None
    return response


if __name__ == "__main__":
    f_feed = get_reddit_front_page()
    sub_feed = get_subreddit("pokemon", "hot")
    
    results = f"""
Front Page: 
{f_feed}


Subreddit: 
{sub_feed}    
"""
    print(results)
