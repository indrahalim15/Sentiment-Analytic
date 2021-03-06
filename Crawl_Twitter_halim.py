import tweepy,sys,jsonpickle

consumer_key = 'LRc5aP74OG7vWQzRzxrEvKr6r'
consumer_secret = 'WTd0vIhA66gpnaZUuJyJN1WnAOF6XxA85EoSnuUuRIqRJ4Z5ul'

qry='Ahok'
maxTweets = 10000 
tweetsPerQry = 100
fName='Hasil_Tweets_Halim3.json'

auth = tweepy.AppAuthHandler(consumer_key,consumer_secret)
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
if (not api):
    sys.exit('Autentikasi gagal, mohon cek "Consumer Key" & "Consumer Secret" Twitter anda')

sinceId=None;max_id=-1;tweetCount=0
print("Mulai mengunduh maksimum {0} tweets".format(maxTweets))
with open(fName,'w') as f:
    while tweetCount < maxTweets:
        try:
            if (max_id <= 0):
                if (not sinceId):
                    new_tweets=api.search(q=qry,count=tweetsPerQry)
                else:
                    new_tweets=api.search(q=qry,count=tweetsPerQry,since_id=sinceId)
            else:
                if (not sinceId):
                    new_tweets=api.search(q=qry,count=tweetsPerQry,max_id=str(max_id - 1))
                else:
                    new_tweets=api.search(q=qry,count=tweetsPerQry,max_id=str(max_id - 1),since_id=sinceId)
            if not new_tweets:
                print('Tidak ada lagi Tweet ditemukan dengan Query="{0}"'.format(qry));break
            for tweet in new_tweets:
                f.write(jsonpickle.encode(tweet._json,unpicklable=False)+'\n')
            tweetCount+=len(new_tweets)
            sys.stdout.write("\r");sys.stdout.write("Jumlah Tweets telah tersimpan: %.0f" %tweetCount);sys.stdout.flush()
            max_id=new_tweets[-1].id
        except tweepy.TweepError as e:
            print("some error : " + str(e));break 
print ('\nSelesai! {0} tweets tersimpan di "{1}"'.format(tweetCount,fName))