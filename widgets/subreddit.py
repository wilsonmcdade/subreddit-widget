"""
Subreddit widget for Kindhub
Author: Wilson McDade
"""
import requests
import json
from __main__ import app, enabled_widgets
from flask import render_template

@app.route('/subreddit')
def subreddit():
    sub = enabled_widgets['subreddit']

    valid_tops = ["hour", "day", "week", "month", "year", "all"]

    if sub['top'] in valid_tops:
        top = sub['top']

    url = "https://www.reddit.com/r/"+sub['subreddit']+"/top/.json?t="+top

    r = requests.get(url = url)

    data = r.json()

    img = data['data']['children'][0]['data']['url']
    title = data['data']['children'][0]['data']['title']
    user = data['data']['children'][0]['data']['author']

    return render_template('xkcd.html',widgets=enabled_widgets,img=img,title=title,user=user)
