#!/usr/bin/env python

import urllib2
import sys
import json
from bs4 import BeautifulSoup, NavigableString
import re
import csv
import datetime
import os
import time
import random
from HTMLParser import HTMLParser
import urlparse, urllib
import string
import urllib2,cookielib
import math


class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


def removeTags(html, *tags):
    soup = BeautifulSoup(html)
    for tag in tags:
        for tag in soup.findAll(tag):
            tag.replaceWith("")

    return soup
    
base = "http://fivethirtyeight.com/tag/significant-digits/page/10"
base= "https://fivethirtyeight.com/contributors/walt-hickey/"
def download_articlesUrls(baseUrl):
    print baseUrl
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}
    req = urllib2.Request(baseUrl)
    try:
        page = urllib2.urlopen(req)
        print "page", page
    except urllib2.HTTPError, e:
        print "error "
        pass
        #print e.fp.read()
    print "reading"
    content = page.read()
    print "content",content
    soup = BeautifulSoup(content)
    print "soup",soup
   # main = soup.find_all("div",{"class":"a-to-z list"})
    for div in soup.find_all("div",{"class":"article-title"}):
        a = div.find_all('a')
        for link in a:     
            print link
            
download_articlesUrls(base)