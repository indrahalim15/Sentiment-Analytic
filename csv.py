import tweepy 
import time 
import re,string 
from tweepy import Stream 
from tweepy.auth import OAuthHandler 
from tweepy.streaming import StreamListener 

ckey='dH7wGLT9ZQp7pA9QBKxq6hBXE'
csecret='U0ZkvQ21dQw8zQ4VnvvOrK0DS5MDKB0gRDyYpyCp8w7FESXqOQ'
atoken='3181521055-tfcxyBJwQ2nHYQIhfbRR0wBvSga2IHfJKlbzKC6'
asecret='Qv6sYaSJ45xL6Tp1jvpSaT5YobH6rGhSVzkfE2r5svALB'

class listener(StreamListener): 
	def on_data(self,data): 
			tweet=data.split(',"text":"')[1].split('","source')[0]
			#remove punctuation
			hapus=set(string.punctuation)
			hasil=''.join(ch for ch in tweet if ch not in hapus)
			print hasil
			#lowering alphabet
			saveThis = hasil.lower()
			#saving in notepad
			simpanFile=open('tweet_27sept.csv','a')
			simpanFile.write(saveThis)
			simpanFile.write('\n')
			simpanFile.close()
			return True
	def on_error(self,status): 
		print status
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["ahok", "anies baswedan", "agus harimurti"])