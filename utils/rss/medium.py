import os

"""
Medium
    User: medium.com/feed/@{username}
    Tag: medium.com/feed/tag/{tag_name}
    
    can also sort by 
    latest, top
    and top has options for
    time: year, all-time, month, day

    Ex 1: medium.com/feed/tag/{tag_name}/top/year
    Ex 2: medium.com/feed/tag/{tag_name}/latest
    
"""

def get_medium_user(username: str):
    return

def get_medium_tag(tag: str):
    return

if __name__ == "__main__":
    username = ""
    tag = ""
    
    u = get_medium_user(username)
    t = get_medium_tag(tag)

    results = f"""
User: 
{u}

Tag: 
{t} 
"""
    print(results)
