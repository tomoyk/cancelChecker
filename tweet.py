#!/usr/bin/env python

from twitter import *

def tweet(message):

    TOKEN=''
    TOKEN_SECRET=''
    CONSUMER_KEY=''
    CONSUMER_SECRET=''

    t = Twitter(auth=OAuth(TOKEN, TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
    t.statuses.update(status=message)


if __name__ == '__main__':

    tweet("hello world")
