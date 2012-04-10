#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import twitter
from xml.dom import minidom
import urllib
import nltk
import random
from nltk.corpus import brown
from nltk.corpus import gutenberg
from nltk.corpus import webtext
from nltk.corpus import movie_reviews

def generateSentence():
    corpus = random.randint(0,3)
    if corpus == 0:
        text = brown.words()
    elif corpus == 1:
        text = gutenberg.words()
    elif corpus == 2:
        text = webtext.words()
    elif corpus == 3:
        text = movie_reviews.words()
    tweetString = ''
    lengthOfTweet = random.randint(0,20)
    len(text)
    firstRun = True
    blank = ' '
    startOfWord = ''
    startOfWordIndex = 0
    startingWord = random.randint(0, (len(text) - 40))
    punctuation = [".", ",", '"', ";", ":", "?", "!", ")", "(", "*", "[", "]", "‘", "“", "#"]

    for x in xrange(startingWord,(startingWord + len(text))):
        startOfWord = text[x]
        if startOfWord ==".":
                startOfWordIndex = x
                break

    for x in xrange(startOfWordIndex + 1, startOfWordIndex+lengthOfTweet):
        if text[x] in punctuation:
            tweetString = tweetString + text[x]

        elif text[x] not in punctuation:
            tweetString = tweetString + blank + text[x]
    return tweetString


#fill in your own details here
API = twitter.Api(consumer_key = '##################',
                  consumer_secret = '##################',
                  access_token_key = '##################-##################',
                  access_token_secret = '##################')

def prepareTweet():
    #This method composes the tweet
    tweet = generateSentence()
    if len(tweet) < 141:        #remember: tweets can only be 140 chars long
        return tweet

def makeTweet():
    #This method actually sends the tweet
    print 'Tweeting'
    tweet = prepareTweet()
    try:
        API.PostUpdate(tweet)
    except Exception, e:
        time.sleep(10)
        main()
    print 'Tweet successful!'
    return True

def main():
    makeTweet()

if __name__ == '__main__':
    main()

