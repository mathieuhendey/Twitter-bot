import time
import twitter
from xml.dom import minidom
import urllib
#By Mathieu Hendey
#http://www.mathieuhendey.com

#This is a simple template for making a twitter bot. You need to make your own app at dev.twitter.com to generate
#your consumer_key, consumer_secret, access_token_key and access_token_secret.



#fill in your own details here
API = twitter.Api(consumer_key = '2QI0sN6XmHpWtyAOeDoPjA',
                  consumer_secret = 'rU0xTVG2Q0Qn9ARCGxhcwQeZSNCyRRihwYPAnADlN0',
                  access_token_key = '460552349-GpOwibMcie7xHVqUAzS7kXeww5qQIeO57YdTBV9Y',
                  access_token_secret = 'gBhoMTZOLXjdMrxbyuaIOzMoDkGf3H66X2Vko0')

def prepareTweet(target):
    #This method composes the tweet
    tweet = '$USERNAME FUS RO DAH!'        #enter your tweet after $USERNAME, don't delete $USERNAME, just leave one space after it
    tweet = tweet.replace('$USERNAME', '@%s' % target.user.screen_name)
    if len(tweet) < 141:        #remember: tweets can only be 140 chars long
        return tweet

def makeTweet(target):
    #This method actually sends the tweet
    print u'Tweeting @%s' %(target.user.screen_name)
    tweet = prepareTweet(target)
    API.PostUpdate(tweet, in_reply_to_status_id=target.id)
    print 'Tweet successful!'
    return True

def searcher():
    #searches for your query and returns a tweet
    print 'searching...'
    results = API.GetSearch('Skyrim')        #replace query with your search term enclosed in 's
    if results:
        for result in results:
                return result

if __name__ == '__main__':
    #main method, calls other methods and updates a counter to let you know how many tweets you've made
    while True:
            target = searcher()
            counter = 0
            if target:
                result = makeTweet(target)
                counter += 1
                print '#%s Done' % counter
                time.sleep(120)         #This is the time in seconds to wait between each tweet. If you are 
                                        #searching for an obscure-ish term,
                                        #set it to a high number, or you will tweet the same person twice, 
                                        #Twitter will return a duplicate_status error and the script will end.