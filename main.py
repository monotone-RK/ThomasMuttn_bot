#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ******************************************************************************/
# ThomasMuttn_bot by python                   Ver:2.0 Last updated 2022.03.01 */
# Copyright (C) 2013-2022 Ryohei Kobayashi                                    */
# Licensed under MIT. See LICENCE file for more information.                  */
# ******************************************************************************/
import sys
import os
import time
import datetime
import random
import twitter
import urllib
from optparse import OptionParser

optparser = OptionParser()
optparser.add_option("-v", "--version", action="store_true", dest="showversion",
                     default=False, help="Show the version")
(options, args) = optparser.parse_args()

# ** consumer key,secret, oauth token,secret, tweetfile                       **/
# ******************************************************************************/
CONSUMER_KEY = "consumer_key"
CONSUMER_SECRET = "consumer_secret"
OAUTH_TOKEN = "oauth_token"
OAUTH_TOKEN_SECRET = "oauth_token_secret"
TWEET_FILE = "./dic/tweet.txt"

# ** functions                                                                **/
# ******************************************************************************/


def showVersion():
    print("## 2.0   last upated:2022.03.01")


def showUsage():
    print("## ThomasMuttn_bot by python")
    print("## Date:2022.03.01")
    print("## Usage: ./main.py tweet")


# ** process                                                                  **/
# ******************************************************************************/
if options.showversion:
    showVersion()
    sys.exit()

if len(args) == 0:
    showUsage()
    sys.exit()
elif len(args) != 1:
    print("## Error! The number of argument is wrong.")
    sys.exit()

if not os.path.isfile(TWEET_FILE):
    print("## Error! Tweet file is not found!: " + TWEET_FILE)
    sys.exit()

if args[0] == "tweet":
    api = twitter.Api(CONSUMER_KEY, CONSUMER_SECRET,
                      OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    print("get api instance")
    tweet_file = open(TWEET_FILE, "r")
    print("tweet_file open")
    tweet_data = random.choice(tweet_file.readlines())
    # for i,line in enumerate(tweet_file):
    #     if random.randint(1, i+1) == 1:
    #         tweet_data = str(line.rstrip())
    print("get tweet_data")
    tweet_file.close()
    print("tweet_file close")
    try:
        api.PostUpdate("%s" % tweet_data)
        print("postupdate")
        print(tweet_data, len(tweet_data))
        print("=" * 30)
    except(urllib.error.HTTPError, twitter.TwitterError) as e:
        print(e)
else:
    print("## Usage: ./main.py tweet")

# Without using Linux cron
###################################################################################
# if args[0] == "tweet":
#     api = twitter.Api(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
#     print("get api instance")
#     api.PostUpdate(u"ThomasMuttn_bot 起動" + datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
#     print("ThomasMuttn_bot start")
#     # last_updated = 0
#     last_updated = datetime.date.today() - datetime.timedelta(1)
#     tweet_cnt = 1
#     print("=" * 30)
#     try:
#         while True:
#             # last_updated = 0 if last_updated == 23 and datetime.datetime.now().hour == 0 else last_updated
#             # if last_updated < datetime.datetime.now().hour and datetime.datetime.now().hour % 2 == 1:
#             if last_updated < datetime.date.today() and datetime.datetime.now().hour >= 22:
#                 current_str = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
#                 print("tweet count: %d" % tweet_cnt, current_str)
#                 tweet_file = open(TWEET_FILE, "r")
#                 print("tweet_file open")
#                 tweet_data = random.choice(tweet_file.readlines())
#                 # for i,line in enumerate(tweet_file):
#                 #     if random.randint(1, i+1) == 1:
#                 #         tweet_data = str(line.rstrip())
#                 print("get tweet_data")
#                 tweet_file.close()
#                 print("tweet_file close")
#                 try:
#                     api.PostUpdate("%s" % tweet_data)
#                     print("postupdate")
#                     print(tweet_data, len(tweet_data))
#                     # last_updated = datetime.datetime.now().hour
#                     last_updated = datetime.date.today()
#                     tweet_cnt += 1
#                     print("=" * 30)
#                 except(urllib.error.HTTPError, twitter.TwitterError) as e:
#                     print(e)
#             time.sleep(10)
#     finally:
#         api.PostUpdate(u"ThomasMuttn_bot 終了" + datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
#         print("ThomasMuttn_bot finish")
#         sys.exit()
# else: print("## Usage: ./main.py tweet")
