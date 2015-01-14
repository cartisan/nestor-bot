# coding: utf8

from pattern.web import URL, Twitter
from botlicense import distressedbotrwlicense

# This script can be used to post new tweets on Twitter.

class Tweeter:

    def tweetmessage(self, message):

        if len(message) <= 140:
            # Tweet to post:
            tweet = message
            #"@distressedbot Don't worry! You'll soon be creative! #codecampcc"

            # The API for posting is described here:
            # # https://dev.twitter.com/rest/reference/post/statuses/update
            url = URL("https://api.twitter.com/1.1/statuses/update.json", method="post", query={"status": tweet})

            # We'll use the Twitter._authenticate() method to authenticate ourselves 
            # as @ccpattern (so the new tweet will appear on @ccpattern's page):
            twitter = Twitter(license=distressedbotrwlicense)
            url = twitter._authenticate(url)

            try:
                # Send the post request.
                url.open()
            except Exception as e:
                print e
                print e.src
                print e.src.read()
                
    def post_tweet(self, tweet):
        if len(tweet) <= 140:
            from pattern.web import URL, Twitter
            import json

            url = URL("https://api.twitter.com/1.1/statuses/update.json", method="post", query={"status": tweet})

            twitter = Twitter(license=distressedbotrwlicense)
            url = twitter._authenticate(url)

            try:
                # Send the post request.
                data = url.open().read()
            except Exception as e:
                print e
                print e.src
                print e.src.read()
                return None

            data = json.loads(data)
            return int(data[u'id'])

    
    def reply_tweet(self, tweet, reply_id, reply_user="@DistressedBot"):
        if len(tweet) <= 140:
            from pattern.web import URL, Twitter

            tweet = reply_user + " " + tweet
            url = URL("https://api.twitter.com/1.1/statuses/update.json", method="post", query={"status": tweet, "in_reply_to_status_id": reply_id})

            twitter = Twitter(license=distressedbotrwlicense)
            url = twitter._authenticate(url)

            try:
                # Send the post request.
                url.open()
            except Exception as e:
                print e
                print e.src
                print e.src.read()

    def get_replies(reply_id):
	import json
	from pattern.web import URL, Twitter

	reply_id = reply_id - 1
	url = URL("https://api.twitter.com/1.1/statuses/mentions_timeline.json", method="get", query={"since_id":reply_id})

	twitter = Twitter(license=distressedbotrwlicense)
	url = twitter._authenticate(url)

	user_replies = {}
	bot_replies = {}
	try:
	    data = json.loads(url.open().read())
	    for reply in data:
	    	name = reply["user"]["name"].encode('utf-8').strip()
	    	text = reply["text"].replace("@BotsVsQuotes","").strip()
	    	if name == "BotsVsQuotes":
	    		#bot quotes
	    		text = text.split(":") 
	    		char_name = text[0]
	    		bot_replies[char_name] = "".join(text[1:]).strip()
	    	else:
	    		#user quotes
	    		user_replies[name] = text 
	except Exception as e:
	    print e
	    print e.src
	    print e.src.read()
	    return {}, {}
	return bot_replies, user_replies



    if __name__ == '__main__':
	import json
	from pattern.web import URL, Twitter

	# Tweet to post:
	tweet = "test tweet"

	url = URL("https://api.twitter.com/1.1/statuses/update.json", method="post", query={"status": tweet})

	twitter = Twitter(license=distressedbotrwlicense)

	url = twitter._authenticate(url)


#	try:
#	    # Send the post request.
#	    a = json.loads(url.open().read())
#	    reply_id = a["id"]
#	    print reply_id
#	except Exception as e:
#	    print e
#	    print e.src
#	    print e.src.read()
