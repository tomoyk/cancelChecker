#!/usr/bin/env python

from getter import *
from tweet import *
from slack import * 
from calAdd import *
import sys
import time


# Open and Read file
# Return object(dict/list)
def read_json_file(open_file):

    # Read json file
    with open(open_file, 'r') as f:
        posts = f.read()
    
    # Convert json -> list&dict
    posts = json.loads(posts)
    
    # for o in posts:
    #     print(o)

    return posts


# Search new-posts on target from base
# Retrun object(dict/list)
def find_new_posts(target, base):
    diff=[]
    for n in target:
        for o in base:
            # Exist post
            if(n==o):
                break
        else:
            # New post found
            # print(n)
            diff.append(n)

    # print(diff)
    return diff


# Save to file
# Return -
def save2file(save_posts, save_file):

    # Convert list&dict -> json
    dumped_posts = json.dumps(save_posts, ensure_ascii=False, indent=4)
    
    # Store json file
    with open(save_file, 'w') as f:
        f.write( dumped_posts )


def main():
        
    JSON_FILE = 'cancel.json'
    old_posts = read_json_file(open_file=JSON_FILE)
    new_posts = get_updates(BASE_URL='https://inside.teu.ac.jp/hachiouji/hachioji_common/cancel/page/')

    different_posts = find_new_posts(target=new_posts, base=old_posts)
    calAdd(posts=different_posts)

    '''
    for p in different_posts:
        try:
            dept = ', '.join(p['dept'])
            message = p['day'] + " " + p['time'] + "限 " + p['course'] + "(" + p['teacher'] + ", " + dept + ", " + p['grade'] + ", クラス:" + p['class'] + ")"
            print(message)
            tweet(message)
            slack(message)
        except Exception as e:
            print(e)
        time.sleep(3)
    '''

    save2file(save_posts=new_posts, save_file=JSON_FILE)
    # 'day', 'time', 'course', 'teacher', 'dept', 'grade', 'class', 'misc', 'update'


if __name__ == '__main__':
    main()

