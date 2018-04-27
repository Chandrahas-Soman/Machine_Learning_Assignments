# twitter sentiment analyser

''' created sentimentAnalyserVersion0 app using Tweeter API apps.twitter.com
	Keys and Access Tokens tab 
	Consumer Key (API Key)	MCMklCxb49WFJdhnkeJ1y9iqW
	Consumer Secret (API Secret)	kXtlYPb6xVTEhHJT3lJzi8cdLoPcrLoyXhYdTL9nCsoCuPdEKU '''

import tweepy
from textblob import TextBlob

consumer_key = 'MCMklCxb49WFJdhnkeJ1y9iqW'
consumer_secret = 'kXtlYPb6xVTEhHJT3lJzi8cdLoPcrLoyXhYdTL9nCsoCuPdEKU'
access_token = '974515717587419137-PKT2vOagEH0PmYTCQTuFximC1VdsN9s'
access_token_secret = 'pPLp4kqIwQp6vLcRfiA6dkUHcgoxvtVzMxWQrmQyBrxI3'

# Authentication

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# now we can create tweets/ delete tweets/ find tweet users

# Retrieve Tweets
public_tweets = api.search('Thanos')

# we can save each Tweet to a CSV file
# and label each one as either 'positive' or 'negative', depending on the sentiment 
# You can decide the sentiment polarity threshold.


for tweet in public_tweets:
    print(tweet.text)
    
    # Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")