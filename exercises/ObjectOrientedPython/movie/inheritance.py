# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 09:54:00 2016

@author: paul
"""

class Parent():
    def __init__ (self, last_name, eye_color):
        print ("Parent constructor called")        
        self.last_name = last_name
        self.eye_color = eye_color
    def show_info(self):
        """prints last name and eye color of a person"""
        print ("Last Name " + self.last_name)
        print ("Eye color " + self.eye_color)
class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print ("Child constructor called")        
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys
    def show_info(self):
        """prints last name and eye color of a child"""
        print ("Last Name " + self.last_name)
        print ("Eye color " + self.eye_color)
        print ("Number of toys " + str(self.number_of_toys))
#billy_cirus = Parent("Cirus", "Blue")
#print billy_cirus.last_name

#billy_cirus.show_info()

miley_cirus = Child("Cirus", "Blue", 5)
#print (miley_cirus.last_name)
#print (miley_cirus.number_of_toys)

miley_cirus.show_info()

        
        
        