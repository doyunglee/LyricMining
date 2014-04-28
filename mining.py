# As projects get larger and have multiple modules.
# it becomes helpful to add a nice little comment
# up here to let a reader know what the file is
# meant to do. On examination, my understanding is
# that mining.py and mining2.py are in fact the same
# thing. It might be nice to either clean
# that up by deleting one, or to explain the
# difference up here.

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 17:52:18 2014

@author: cauerswald
"""

from pattern.web import *
import urllib2
w=Wikipedia()
from bs4 import BeautifulSoup


def create_song_dictionary():
    songs = open('songs.txt', 'r')
    songs_text = songs.read()
    songs_list =songs_text.split('///')
    all_songs = {}
    for song in songs_list:
        if len(song.split('**'))==3:
            title= song.split('**')[1].lower()
            print title
            all_songs[title] = song.split('**')[2].lower()
    return all_songs
    
all_songs = create_song_dictionary()

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
            # I'm curious as to what makes this different than the below elif statement and why you
            # didn't roll this into the below elif as year<=1958 and year>=1940
        elif year<1958 and year>=1940:
            page =  w.search('List of Billboard number-one singles of '+str(year)) 
        if page.sections[0].tables!=[]:
            page_html = page.sections[0].html
        else:
            page_html = page.sections[1].html
        soup = BeautifulSoup(page_html)
        # Consider breaking this up with some whitespace here! This block of
        # solid code is really hard for a reader to visually process!
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
                    hits.append(str(song_title).lower()) #append song onto list
            #print "out"
        hits = remove_repeats(hits) #some songs show up twice because they peaked twice or something, so get rid of any duplicates                       
        all_hits.append(hits)
        if hits==[]:
            print year
    
    return all_hits

# This entire function a bit convoluted and hard to follow: I understand it might take all of this to
# extract the data you care about from all of the wrapping information, but it could possibly
# be made a bit easier to read and understand with some whitespacce, or even possibly being split into
# two functions: one to retrieve the "soup" of each page, and one to parse the tables in the soup.


def get_lyric(song_name):
    """This function takes the song name and 
    finds the lyrics to the song using Google"""
    '''
    g = Google()
    search_phrase = 'azlyrics ' + song_name
    for result in g.search(search_phrase, type=SEARCH, start=1, count=1):
       song_website = urllib2.urlopen(result.url) #Open and read the url
       song_page = song_website.read() #Save it into a string       
       #Find the start and end
       start_song = song_page.find("<!-- start of lyrics -->")#find the beginning of the song in the website html
       end_song = song_page.find("<!-- end of lyrics -->")#find the end of the song in the website html
       song = song_page[start_song:end_song].replace("<br />","").replace(">","").replace("<","").replace("/i","").replace("\n"," ").replace("!-- start of lyrics --\r"," ").replace("\r","").replace("\xe2\x80\x99","'") #replace some unneeded hodgepodge
       return song
    '''
    #return all_songs[song_name]

    # Is this dead code or did you only have to use it once and didn't want it to run again?
    # If its the former, you normally want to take this out for the submitted version of your code.
    # If its the latter, you can probably either leave it in or put it in a seperate setup module
    # that you only run once. (Or you can just leave it here and not run it again).

def convert_to_word_mash(list_of_songs):
    """Takes a list of song titles and returns a list of words"""
    all_words = []
    for i in range(len(list_of_songs)): #goes through the list of songs and gets the lyrics for each song
        lyric = all_songs[list_of_songs[i]]
        song_words = remove_repeats(re.findall("[a-zA-Z']+",lyric))
        all_words +=song_words         
    return all_words
    
    
def count_words(words):
    word_count = {}
    bad_words = ["i'll",'got', 'this', 'what', 'get',"you're", 'from', 'yeah', 'but', 'when', 'like', 'just', 'all', 'a', 'you','i', "i'm", 'the', "me", "going", "to", "is", "and", "i", "it's", "for", "with", "your", "that", 'are']
    # You might want to write some of which words you omitted up in your reflection if they're hard coded in like this so that the reader is aware of
    # things that they will never see in your code. I assumed something like this existed but I didn't see it in the writeup. Just a note for future projects.
    for word in words:
        if word not in bad_words and len(word) > 1: 
            if word in word_count:
                word_count[word]+=1
            else:
                word_count[word]=1
    return word_count

def get_max(dic, n):
    ''' 
    returns the num n max values in a dictionary as a dictionary
    assumes: all values are positive numbers, the dictionary has more than n entries
    
    '''
    dup_dic = dict(dic) 
    # This would be a great place to use dict.keys() which returns
    # the keys of a dictionary as a list. The Counter module in the
    # collections module is a great tool for finding the modes of a list.
    # It saves the duplication and deletion that you perform here and
    # most likely would result in more succinct, easier to follow code.
    maxes={}
    max_val = 0
    for i in range(n):
        for key in dup_dic:
            val = dup_dic[key]
            if val>max_val: 
                max_val=val
                max_key = key
        del dup_dic[max_key]
        maxes[max_key]=max_val
        max_val=0
    return maxes

def generate_trends():
    start_year = 2009
    end_year = 2013
    hit_lists=find_all_hits(start_year, end_year)
    wc_by_year = []
    max_wc_by_year = []
    for hit_list in hit_lists:   
        wc_by_year.append(count_words(convert_to_word_mash(hit_list)))
        print "do: "+str(wc_by_year[len(wc_by_year)-1]["dance"])+"dont: "+" "+str(wc_by_year[len(wc_by_year)-1]["party"])
        # What does this mean? This could use a comment, or be changed to take multiple, readable lines
    for word_dic in wc_by_year:
        max_wc_by_year.append(get_max(word_dic,6))
    print max_wc_by_year
    
            
            
    
'''
function that takes a list of song names and turns that into list of words
function that takes a list of words and counts how frequently each one appears

'''
            
'''
if __name__ == '__main__':
    list = find_all_hits(2012,2013)[0]
    print convert_to_word_mash(list)
'''
# Why comment this? Seems like good stuff to have in here so that someone can run your code easily.
# Is it for fear that someone will overwrite the data you've collected?