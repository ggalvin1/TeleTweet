#!/usr/local/bin/python3
# coding: utf-8

# TeleTweet - config.py
# 10/22/20 16:20
#

__author__ = "Benny <benny.think@gmail.com>"

import os

BOT_TOKEN = os.getenv("TOKEN", "6673930030:AAG1adRoR3aYidm0ObyFNO81G_MM1HIEwsY")
APP_ID = int(os.getenv("APP_ID", "24530167"))
APP_HASH = os.getenv("APP_HASH", "e18b721e80d4009c1666d70273add22b")

CONSUMER_KEY = os.getenv("CONSUMER_KEY", "deVgn98BHbgMZeU6gCSb7jrEk")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET", "vdcDW8Ft4BMZNqktgXz90avdPqiORi6mCr3qPgE3xbIEAYmNnw")

tweet_format = "https://twitter.com/{screen_name}/status/{id}"
