import bs4 as bs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

# Import nltk package 
#   PennTreeBank word tokenizer 
#   English language stopwords
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from sklearn.svm import SVC
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, precision_recall_fscore_support
from sklearn.cluster import MiniBatchKMeans

from collections import OrderedDict, Counter
#Download MLTK English tokenizer/stopwords 
nltk.download('punkt')
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

#read in dataset
df_questions = pd.read_csv('pythonquestions/Questions.csv', 
				encoding= 'ISO-8859-1', nrows=5000)  #encoding was weird, use this for the
														#stackoverflow dataset
# nrows = 50000

#print out questions template 
print(df_questions.head())
print()

#for every question, parse HTML to actual text
#place in new column
def convert_body(body):
	return bs.BeautifulSoup(body, 'lxml').get_text()

df_questions["pBody"] = pd.Series(df_questions["Body"].apply(convert_body), 
						index = df_questions.index)

#print out results of method
print(df_questions.head())
print()


#create TfidfVectorizer object
tfidf = TfidfVectorizer(sublinear_tf=True, analyzer='word', 
						max_features=500, tokenizer=word_tokenize, max_df=0.8)


print("Transforming dataset")

#Transform pBody data
tf_pBody = tfidf.fit_transform(df_questions["pBody"])
tf_pBody = tf_pBody.toarray() #transformed vectors into a matrix


#Check if dataset shape lines up: for this case should be 10000 and 1000
print(tf_pBody.shape)


print("plotting datapoints on grid")
#Plot data on a 2 dimensional grid just for visualization purposes
pca = PCA(n_components=2).fit(tf_pBody)
data2D = pca.transform(tf_pBody) #data2D = number of posts * 2
#plt.show()  

print("plotting k-means analysis")
#use K-means on data and plot means on PCA graph 
kmeans = MiniBatchKMeans(n_clusters=10).fit(tf_pBody) #default threshold
centers2D = pca.transform(kmeans.cluster_centers_)

plt.hold(True)

#plt.show()              


#convert clusters back into text
clusters = kmeans.cluster_centers_
#print(clusters)
questions_clusters = tfidf.inverse_transform(X=clusters)
for i in range(2):
	print(questions_clusters[i])
print()
#print(tfidf.get_feature_names())
tfidf_dict = tfidf.vocabulary_
print(kmeans.labels_)#color each label

plt.scatter(data2D[:, 0], data2D[:, 1], c=kmeans.labels_)
plt.scatter(centers2D[:,0], centers2D[:,1], 
	marker='x', s=200, linewidths=3, c='r')

print("all plotted")


#sort sentences based on label/tfidf
df_questions["label"] = pd.Series(kmeans.labels_, index = df_questions.index)

print(df_questions.head())

string_dict = []
top30_dict = []

def getStrings(input_df):
	output = ""
	for string in input_df:
		output = output + " " +string
	return output.lower()

#bow = CountVectorizer(stop_words='english')

for i in range(10):
	string_dict.append(getStrings(df_questions[df_questions["label"] == i]["pBody"]))
	word_tokens = word_tokenize(string_dict[i])
	filtered_sentence = [w for w in word_tokens if not w in stop_words]
	filtered_punct = [w for w in filtered_sentence if not w in punkt]
	#split_it = filtered_sentence.split()
	cnt = Counter(filtered_punct)
	#bow.fit_transform(string_dict[i])
	#ordered =sorted(bow.vocabulary_.items(), key=lambda v:v[1], reverse=True)
	top30_dict.append(cnt.most_common(30))
	print(top30_dict[i])



	#cnt = Counter(bow.vocabulary_).most_common(20)
	#top10_dict.append(cnt)
	#print(cnt)
	print()


questions_dict = [df_questions[df_questions['label'] == i] for i in range(10)]

print(questions_dict[0].head())

plt.show()
