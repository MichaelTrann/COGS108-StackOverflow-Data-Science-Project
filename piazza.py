import pandas as pd
import json
import numpy as np
from piazza_api import Piazza 

df_user = pd.read_json('config.json', typ="series");

p = Piazza()
p.user_login(df_user["user"], df_user["pass"])
cogs108 = p.network(df_user["network"])
posts = cogs108.iter_all_posts(limit=None)

dict_posts = []
follow_ups = []

for post in posts:
	#if you would like to pretty print the data
	#the built in program already anonymizes all user names to a default: "no"
	#print(json.dumps(post, indent=4, sort_keys=True))

  if post['status'] != 'private':
    dict_post1 = {'content': post['history'][0]['content']}
    dict_posts.append(dict_post1)
    follow_ups.append(len(post['children']))

data = {
	"posts": dict_posts,
    "follow-ups": follow_ups
}

with open('posts.json', 'w') as outfile:
    json.dump(data, outfile)


with open('posts.json', 'r') as handle:
	parsed = json.load(handle)

print(json.dumps(parsed, indent=4, sort_keys=True))