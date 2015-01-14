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
                
