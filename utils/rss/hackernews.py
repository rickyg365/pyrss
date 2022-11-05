import os
import requests

"""
Hacker News
    Front page: news.ycombinator.com/rss
    Show HN: news.ycombinator.com/showrss

    hnrss is an open-source project that provides RSS feeds for various HN resources. 
    Some examples:
        New threads w/ keyword:  hnrss.org/newest?q={keyword}
        New posts by user:  hnrss.org/submitted?id={user}
        New posts w/ upvotes and comments:  hnrss.org/show?points={int}&comments={int}

"""

def get_hackernews_home():
    return


if __name__ == "__main__":
    hnh = get_hackernews_home()
    print(hnh)
