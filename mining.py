# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 17:52:18 2014

@author: cauerswald
"""

from pattern.web import *
import urllib2

#def song_list():
#    """this function takes a year and finds the top singles of that year in wikipedia
#    (according to Wikipedia)"""
#    w=Wikipedia()
#    start_year = 2014;
#    top_hits_page =  w.search('List of Billboard Hot 100 number-one singles of 2013')
    #section = WikipediaSection(top_hits_page, title='Notes', start=0, stop=0, level=1)
#    section = top_hits_page.sections
    #table = section.tables
#    table = section[1].tables
#    table1 = WikipediaTable(section[1], title='key', headers=[], rows=[], source='')
#    print table1.n


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

#song_url = result.url
#html = download(song_url, unicode=True)    
#print html
#print result.url
#print plaintext(result.text)

    
if __name__ == '__main__':
    get_lyric("Locked Out of Heaven")