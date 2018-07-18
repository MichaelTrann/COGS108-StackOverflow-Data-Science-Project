import bs4 as bs
import pandas as pd
import numpy as np
import json
from piazza_api import Piazza 



df_user = pd.read_json('config.json', typ='Series');

p = Piazza()
p.user_login(df_user["user"], df_user["pass"])
cogs108 = p.network(df_user["network"])
posts = cogs108.iter_all_posts(limit=3)

dict_posts = []
# pd.DataFrame(columns=('id', 'content', 'num_favorites', 'tags', 'unique_views'))

for post in posts:
	#create a method to extract information from posts
	#add information to a datatable
	#clean information
	#export for analysis
	#print (json.dumps(post, indent=4, sort_keys=True))

	"""print("id: " + str(post['id']))
	print()
	print(post['history'][0]['content'])
	print()
	print("number of favorites: "+str(post['num_favorites']))
	print()
	print("tags: "+str(post['tags']))
	print()
	print("unique views: "+str(post['unique_views']))
	print()"""

	dict_post1 = {'content': post['history'][0]['content'], 'id': post['id'],
	'num_favorites': post['num_favorites'], 'tags': post['tags'], 
	'unique_views': post['unique_views']}

	dict_post1.update()
	dict_posts.append(dict_post1)


	'''df_post = pd.DataFrame(str(post['id']), str(post['history'][0]['content']), 
		str(post['num_favorites']), post['tags'], str(post['unique_views'])'''
df_posts = pd.DataFrame(data=dict_posts)
df_posts.columns = ['content', 'id', 'num_favorites', 'tags', 'unique_views']

df_posts.to_json('piazzaposts.json')

print(df_posts.head())




#sauce = urllib.request.urlopen('https://piazza.com/class/jbocgn8rmq2434?cid=495').read()
#soup = bs.BeautifulSoup(page.content, 'lxml')

#print(soup)
