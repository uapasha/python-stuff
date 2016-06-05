# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 18:44:04 2016

@author: paul
"""

import media
import webbrowser
import fresh_tomatoes

toy_story = media.Movie("Toy story", 
                        "Story about a boy and his toys caming to life",
                        "http://a.dilcdn.com/bl/wp-content/uploads/sites/8/2013/02/toy_story_wallpaper_by_artifypics-d5gss19.jpg",
                        "https://youtu.be/KYz2wyBy3kc")
                        

avatar = media.Movie("Avatar",
                     "Story about a marin on an alien",
                     "http://media.kg-portal.ru/production/avatar/avatar_23.jpg",
                     "https://youtu.be/5PSNL1qE6VY?t=32s")
                         

borat = media.Movie("Borat",
                    "The one who is destined to change Kazakhstan",
                    "https://upload.wikimedia.org/wikipedia/en/3/39/Borat_ver2.jpg",
                    "https://youtu.be/vlnUa_dNsRQ?t=18s")

forrest = media.Movie("Forrest Gump",
                     "Stupid is what stupid does",
                     "https://upload.wikimedia.org/wikipedia/en/6/67/Forrest_Gump_poster.jpg",
                     "https://youtu.be/uPIEn0M8su0?t=2s")
                     
fight_club = media.Movie("Бойцовский клуб",
                         "Телевидение внушило нам веру в то, \
                         что все мы станем миллионерами, \
                         звёздами кино и рок-н-ролла. \
                         Всё враньё. И мы начали это осознавать.\
                         И это приводит всех в ярость.",
                         "https://upload.wikimedia.org/wikipedia/ru/8/8a/Fight_club.jpg",
                         "https://youtu.be/SUXWAEX2jlg")                     
                     
movies = [toy_story, avatar, borat, forrest, fight_club]
#fresh_tomatoes.open_movies_page(movies)

#print media.Movie.VALID_RATINGS
print media.Movie.__module__