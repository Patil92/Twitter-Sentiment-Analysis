import tweepy
from textblob import TextBlob

consumer_key = "JoDlKiDYCyDesex4G5bgWSOnk"
consumer_secrete_key = "SR2oVdrDjG7l8DsvQPZ4GTlSKcy4I9V1jd9YeLB6C7zTXFyG0Q"

access_token = "1085167231481217025-UBxdli8Q9S8XcgxiuuU5BZWAMAYzPb"
access_token_secrete = "Dpsw2okrG3Uk7AUdKmTa6231MLSD6XJ8ta8PdZbLc1eIm"

auth = tweepy.OAuthHandler(consumer_key,consumer_secrete_key)
auth.set_access_token(access_token,access_token_secrete)

api=tweepy.API(auth)

public_tweets=api.search("rahul gandhi")

for tweet in public_tweets:
    print(tweet.text)
    analysis=TextBlob(tweet.text)
    print(analysis.sentiment)
    print("\n\n")
    
    
