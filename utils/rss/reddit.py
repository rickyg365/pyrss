import os
import requests

"""
Reddit
    Append .rss at the end of a URL:

    Front page: https: //reddit .com/.rss
    Subreddit:
        reddit.com/r/{subreddit}.rss
        reddit.com/r/LifeProTips/top.rss
"""

def get_front_page():
    return

def get_subreddit(subreddit_name: str, sort: str):
    valid_sort = [
        "top",
        "new",
        "hot"
    ]
    return


if __name__ == "__main__":
    f_feed = get_front_page()
    sub_feed = get_subreddit("pokemon", "hot")
    
    results = f"""
Front Page: 
{f_feed}


Subreddit: 
{sub_feed}    
"""
    print(results)
