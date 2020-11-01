#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 12:13:19 2020

@author: tech

Scrape the Hacker News web site
"""

import requests#allows us to initially download the HTML
from bs4 import BeautifulSoup #allows us to us HTML and grab the data
import pprint

res = requests.get("https://news.ycombinator.com/news")#url we want to grab data from
#this is the url to hacker news
soup = BeautifulSoup(res.text,'html.parser')#creates a soup object

#print(res.text)#returns a string
#prin#t(soup.body.contents)#converts from a string to an object
#print(soup.find('a'))#finds first a tag
#print(soup.find(id='up_24940810'))

# another good method is the 'select' method which allows us to grab a piece
# of data from the soup object we create using a css selector
# '.' = class,  '#' = id
#print(soup.select('.score'))#class score

#we will grab a story with a score > 100######################33
#print(soup.select('.storylink')[0])
links = soup.select('.storylink')
#print(links)
subtext = soup.select('.subtext')
#votes = soup.select('.score')
#print(votes[0])
#with BeautifulSoup you can chain. e.g., votes[0].get('id')or
#votes.[0].get('id').select ... 

def sort_stories_by_votes(hnlist):
    #this is  a common pattern when sorting dictionaries, so remember it
    #you will sort by key
    return sorted(hnlist, key=lambda k:k['votes'], reverse = True)

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        
        title = item.getText()
        href = item.get('href', None)#return None if link is missing
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points',''))
            if points > 99:
                hn.append({'title:':title,'link':href, 'votes':points})
    
    return sort_stories_by_votes(hn)

#create_custom_hn(links, subtext)
pprint.pprint(create_custom_hn(links, subtext))