import pandas as pd
import numpy as np

df_stack = pd.read_csv('stacksample/Questions.csv', encoding= 'ISO-8859-1') 
df_tag = pd.read_csv('stacksample/Tags.csv', encoding= 'ISO-8859-1') 
print(df_tag.head())


df_tag = df_tag[df_tag["Tag"] == "python"]


print(df_tag.head())
print(len(df_tag))

ids = df_tag.ix[:,0]
print(ids)

df_newstack = df_stack[df_stack['Id'].isin(ids)]
print(df_newstack.head())
print(len(df_newstack))
print(len(df_stack))