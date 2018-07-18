import bs4 as bs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



#read in dataset: questions
df_questions = pd.read_csv('pythonquestions/Questions.csv', 
				encoding= 'ISO-8859-1')  #encoding was weird, use this for the
														#stackoverflow dataset
#read in dataset: tags
df_tags = pd.read_csv('pythonquestions/Tags.csv', encoding= 'ISO-8859-1')

print(df_questions.head())
print(len(df_tags["Tag"].unique()))
print(df_tags.head())

df_counts = df_tags["Tag"].value_counts(normalize=True)
threshold = 0.008
mask = df_counts > threshold
tail_df_counts = df_counts.loc[~mask].sum()
df_counts = df_counts.loc[mask]
df_counts['other'] = tail_df_counts
df_counts.plot(kind='bar')
plt.xticks(rotation=25)
plt.show()


