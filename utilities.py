"""
CPSC 571 F21 Project 

Authors: 
Erin Paslawski 10099039
Peter Nguyen 10096424
Bohyeon Cha 10162219

December 23 2021

Disease Spread Simulator
"""

from random import randint

"""
Generate workplaces
"""
def generate_workplace(workplaces):
    start, end = workplaces
    return randint(start,end+1)

"""
Generate Households
"""
def generate_household(households):
    start, end = households
    return randint(start,end+1)

"""
Calculate contagious rating based on age and population denisty
"""
def contagious_rating(age, pop_density):

    if age == 0 or age == 1:
        rating = 1
    elif age == 2:
        rating = 2
    elif age == 3 or age == 4:
        rating = 3
    elif age == 5:
        rating = 2
    
    return rating*pop_density




