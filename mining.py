# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 17:52:18 2014

@author: cauerswald
"""

from pattern.web import *
import urllib2
w=Wikipedia()
from bs4 import BeautifulSoup

def remove_repeats(l):
    newlist = []
    for item in l:
        if newlist.count(item)==0:
            newlist.append(item)
    return newlist

def find_all_hits(start_year, end_year):
    """
    this function finds all of the billboard hot 100 hits from each year from start_year to end_year
    inputs:
        start_year - the first year you want to look at
        end_year - the last year you want to look at
    output:
        all_hits - list of lists of hit songs from each year, the first list in all_hits being the hits from start_year and the last list in all_hits being the hits from end_year
    """
    all_hits=[]
    for year in range(start_year, end_year+1):
        if year>1958:
            page =  w.search('List of Billboard Hot 100 number-one singles of '+str(year)) 
        elif year == 1958:
            page =  w.search('List of Billboard number-one singles of '+str(year)) 
        elif year<1958 and year>=1940:
            page =  w.search('List of Billboard number-one singles of '+str(year)) 
        if page.sections[0].tables!=[]:
            page_html = page.sections[0].html
        else:
            page_html = page.sections[1].html
        soup = BeautifulSoup(page_html)
        tables = soup.find_all('table') #find all the tables in chart history section, could be table of hits or table of hits preceded by a key        
        for t in tables:
            if t.findAll('th')!=[]:
                table =t
        cols = table.findAll('td')
        hits = [] #create empty list to hold song titles
        for td in cols: #check all of the td tags
            if  len(td.text)>0 and td.text[0]=='"': #look only at the ones that contain song titles
                if str(td.text).count('"')==2:
                    song_title = re.findall(r'"(.*?)"', td.text)[0] #parse out only the part of the string that is in quotations, so only the title of the song
                    hits.append(str(song_title)) #append song onto list
            #print "out"
        hits = remove_repeats(hits) #some songs show up twice because they peaked twice or something, so get rid of any duplicates                       
        all_hits.append(hits)
        if hits==[]:
            print year
    
    return all_hits


def get_lyric(song_name):
    """This function takes the song name and 
    finds the lyrics to the song using Google"""
    g = Google()
    search_phrase = 'azlyrics ' + song_name
    for result in g.search(search_phrase, type=SEARCH, start=1, count=1):
       song_website = urllib2.urlopen(result.url) #Open and read the url
       song_page = song_website.read() #Save it into a string       
       #Find the start and end
       start_song = song_page.find("<!-- start of lyrics -->")
       end_song = song_page.find("<!-- end of lyrics -->")
       print song_page[start_song:end_song].replace("<br />","").replace(">","").replace("<","")

def count_words(words):
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1
    return word_count



        
    
'''
function that takes a list of song names and turns that into list of words
function that takes a list of words and counts how frequently each one appears

'''



