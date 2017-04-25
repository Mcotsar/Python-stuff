#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy

#argfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'tWluAAfKlP016Lxr5i5VBEXqW'
CONSUMER_SECRET = 'nHuHFbOtcVIdG5zb10vyvGzJFQWcYtbdj2wt5pX8ugyIRmpiEU'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '464762135-DscitZQ5TBaJyVw825EIIifSfc7AUTqHMIq6fQpb'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'lC0oxakHVb4edxtw8ulIcas9pkdAaSw02Zpv1Mu5ndZBM'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

api.update_status('testing a bot robot, hi simon')

#filename=open(argfile,'r')
#f=filename.readlines()
#filename.close()
 
#for line in f:
    #api.update_status(line)
    #time.sleep(900)#Tweet every 30 minutes
