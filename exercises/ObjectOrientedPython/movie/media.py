# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 18:40:33 2016

@author: paul
"""
import webbrowser

class Movie():
    """This class provides structures for working with movies"""
    VALID_RATINGS = ["G",'PG', 'PG-13', 'R']      
    def __init__(self, movie_title, movie_storyline, 
                 poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
            