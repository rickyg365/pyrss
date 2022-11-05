import os

from typing import List, Dict, Any
from dataclasses import dataclass

# File Handler
from utils.file_handler.json import save_json, load_json

# RSS Feeds
from utils.rss.hackernews import get_hackernews_home
from utils.rss.medium import get_medium_tag, get_medium_user
from utils.rss.reddit import get_front_page, get_subreddit
from utils.rss.twitter import get_twitter_user
from utils.rss.youtube import get_channel, get_playlist


"""
RSS Feed Reader

[ RSS Links ]:
? Hacker News
    Front page: news.ycombinator.com/rss
    Show HN: news.ycombinator.com/showrss

    hnrss is an open-source project that provides RSS feeds for various HN resources. 
    Some examples:
        New threads w/ keyword:  hnrss.org/newest?q={keyword}
        New posts by user:  hnrss.org/submitted?id={user}
        New posts w/ upvotes and comments:  hnrss.org/show?points={int}&comments={int}

? Reddit
    Append .rss at the end of a URL:

    Front page: https: //reddit .com/.rss
    Subreddit:
        reddit.com/r/{subreddit}.rss
        reddit.com/r/LifeProTips/top.rss

? YouTube
    Channel: youtube.com/feeds/videos.xml?channel_id={channel_id}
    Playlist: youtube.com/feeds/videos.xml?playlist_id={playlist_id}

? Medium
    User: medium.com/feed/@{username}
    Tag: medium.com/feed/tag/{tag_name}

? Twitter
    Twitter stopped providing official feeds in 2013. However, you can use nitter.net for this.
    User: nitter.net/{user}/rss

! Instagram
    Not using for now but maybe use instaloader to create my own rss feed for public profiles


[ External dependancies ]:
- typer?


"""


def main():
    return

if __name__ == "__main__":
    main()