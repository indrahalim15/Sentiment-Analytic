import tweepy 
import time 
from tweepy import Stream 
from tweepy.auth import OAuthHandler 
from tweepy.streaming import StreamListener 

ckey='LRc5aP74OG7vWQzRzxrEvKr6r'
csecret='WTd0vIhA66gpnaZUuJyJN1WnAOF6XxA85EoSnuUuRIqRJ4Z5ul'
atoken='300128654-lgghXfEXX2xItmnlJkSVlBJshFrwJTaIQBxa7oWq'
asecret='Wo2qcxmPIz4bWHbtbZmTwmfm7VXSdxFeythXMmafXkuJu'

class listener(StreamListener): 
	def on_data(self,data): 
			print data
			simpanFile=open('tweet1.csv','a')
			simpanFile.write(data)
			simpanFile.write('\n')
			simpanFile.close()
			return True
	def on_error(self,status): 
		print status
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["ahok"])