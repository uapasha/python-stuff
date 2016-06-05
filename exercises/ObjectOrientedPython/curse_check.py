# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 17:55:02 2016

@author: paul
"""
import urllib

def read_text():
    quotes = open("/home/paul/Dropbox/Ubuntu/courses/Udacity/Python1/movie_quotes.txt")
    contents_of_file = quotes.read()
    #print contents_of_file
    quotes.close()
    return contents_of_file
    
def text_profanity(text_to_check):
    connection = urllib.urlopen("http://192.168.1.1"\
                                +text_to_check)    
    output = connection.read()                            
    print output
    connection.close()
text_profanity(read_text())