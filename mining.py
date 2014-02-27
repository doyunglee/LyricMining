# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 17:52:18 2014

@author: cauerswald
"""

from pattern.web import *
w=Wikipedia()
start_year = 2014;
hits = {}
for year in range(start_year,2015):
    top_hits_page =  w.search('List of Billboard Hot 100 number-one singles of '+str(year))
    section = top_hits_page.sections[1]
    table = section.tables
    print table