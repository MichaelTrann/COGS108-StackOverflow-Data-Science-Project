import bs4 as bs
import pandas as pd
import numpy as np
import nltk
from nltk.tokenize import word_tokenize

df = pd.read_json("lastyearposts.json", orient='values')

names = ['david', 'harshita', 'ilkay', 'wan', 'tianyu', 'tom', 'novak', 'washington', 'wills', 'kevin', 'gael', 'oscar', 'mengting', 'josh', 'altintas', 'shuai', 'megan', 'martin', 'mande', 'screen_shot_20180128_at_8.32.21_pm.png', 'jim', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'mon', 'tues', 'wed', 'thurs', 'fri', 'sat', 'sun', 'tue', 'thur', '3:00-4:00pm', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december', 'jan', 'feb', 'mar', 'apr', 'jun', 'jul', 'aug', 'sept', 'sep', 'oct', 'nov', 'dec', '14th', 'martin', 'luther', 'king', 'jr.', 'day', 'san', 'diego', 'bradley', '//github.com/cogs108/overview/blob/master/wi18.md', 'adam', '-zachariah', 'nye', 'zjgutier', '3:30-4:30pm', 'nick.jones25', '//github.com/cogs108/tutorials/blob/master/11-testingdistributions.ipynb', 'gmail.com', '//goo.gl/forms/crdl0qjsqxdzacmi2', '//github.com/cogs108/assignments', '27th', 'bill', 'reasonscree_shot_20180128_at_4.35.36_pm.png', '//gihub.com/cogs108/assignments/tree/master/a1', '2016', '2015', '2014', '12:30-1:30pm', 'feb.12', 'dylan', "''screen_shot_20180213_at_10.00.39_pm.png", 'mark', 'bob', 'john', 'voytek', 'screen_shot_20180128_at_9.19.33_pm.png', 'centr', '5th', 'amanda', '//www.facebook.com/events/1867318216823629/', '//github.com/continuumio/anaconda-issues/issues/270', '//goo.gl/forms/7zflcvkpps0lec4n2', 'don', 'gshoreson0', 'kmauzy', '11:45', '3pm', '//github.com/cogs108/lecturematerials/tree/master/geospatial', '/users/erikamorozumi/anaconda/lib/python3.6/site-packages/pandas/core/series.py', '//www.facebook.com/events/120580895186001/', 'm9baker', 'ked', 'justino', 'toady', '12:45', 'shepley', '/users/erikamorozumi/anaconda/lib/python3.6/site-packages/pandas/core/generic.py', 'peon', '//goo.gl/dmujya', 'agau', 'ma', 'jas120', 'mmillmorerb', 'wo', 'estelita', 'bayano', '1/2/12', '10:30am', 'keelari_mauzy', '//github.com/cogs108/sectionmaterials', '5/30/17', '858', '17:22;00', '2013-08-01', '28th', '3-5', '7pm', '10:00', '11th', 'geog', 'dharmadi', '4/27', 'tony', '2017.', 'tichner', 'larry', '878', '//docs.google.com/forms/d/e/1faipqlsdpp_1gzz2pj4dw69vgrxn_z48addlwavxcig6da1qtwqaa0q/viewform', 'leddn', '7:00', '2-2:50', '08:14:37', '10:50', '//www.eventbrite.com/e/cognition-at-work-conference-2017-tickets-31019192239', 'kennith', '4-4:50', 'andharma', 'grant', 'taylor', 'tichner', '5-6pm']

def convert_body(body):
  body = str(body).lower()
  body = body[11:len(body) - 1]
  body = body.replace('\\n', ' ')
  body = body.replace('\\xa0', ' ')

  for name in names:
    body = body.replace(name, ' ')

  return bs.BeautifulSoup(body, 'lxml').get_text()

df.columns = ['followup', 'pBody']
df['pBody'] = df['pBody'].apply(convert_body)

total = ""

for body in df['pBody']:
  total = total + body

total = word_tokenize(total)
print(set(total))
