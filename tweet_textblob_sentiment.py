#!usr/bin/env python3
import tweepy
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from  nltk.stem import WordNetLemmatizer
from  nltk.corpus   import  stopwords
from textblob import TextBlob

consumer_key=""
consumer_secret=""
access_key=""
access_secret=""

def get_tweets(topic):
	#authenticating twitter with consumer key and consumer  secret
	auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
	#setting access token
	auth.set_access_token(access_key,access_secret)
	#connecting bssetting access tokenpi
	api=tweepy.API(auth)
	#number_of_tweets=50
	tweets=api.search(q=topic,count=10)
	tmp=[]

	tweets_for_csv=[tweet.text for tweet in tweets]
	for j in tweets_for_csv:
		tmp.append(j)
	print("Extracted tweets:",tmp)
	print("####################################")
	for j in tweets:
		analize=TextBlob(j.text)
		check=analize.sentiment
		print(check)

	
	#lemmatization
'''
	lemma=WordNetLemmatizer()
	for i in range(len(tmp)):
		words=word_tokenize(tmp[i])
		newword=[lemma.lemmatize(word) for word in words]
		tmp[i]=' '.join(newword)
	print(tmp)
	
'''
if __name__=='__main__':
	data=input("Enter topic: ")
get_tweets(data)
'''
import sys
topic=sys.argv(1)  then run using python3 tweet.py virat
'''

