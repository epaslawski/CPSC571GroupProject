"""
CPSC 571 F21 Project 

Authors: 
Erin Paslawski 10099039
Peter Nguyen 10096424
Bohyeon Cha 10162219

December 23 2021

Disease Spread Simulator
"""

'''
Class Person

This class defines a person object and their attributes
'''
class Person:

    def __init__(self, age, works, household, workplace, division, contagious_rating):
        self.age = age              # integer value in 1-5 representing their age group
        self.works = works          # boolean indicating if they work
        self.household = household  # specific household they belong to (int)
        self.workplace = workplace  # specific workplace they belong to (int)
        self.division = division    # integer value in 1-19 representing division
        self.contagious_rating = contagious_rating  # calculated during initialization (float)
        self.infected = False       # label for infected or not
        self.days_infected = 0      # counts infected days
        self.recovered = False      # if they had the disease but are now recovered, they will not get reinfected.
        
   
    
    

