from scipy.stats import norm
import random
import time
peopleDict = []

# This class will define a person. It will have a scale on age, 
# if they go into work or school (based on age and employment rate), their household size

class Person():
    def __init__(self, age, startingImmunity, repro_value, house_size, employment_rate, population, worked_at_place):
        if random.randint(0,100)<startingImmunity:
            self.immunity = True
        else:
            self.immunity = False
        self.contagiousness = repro_value
        self.mask = False
        self.contagiousDays = 0
        
        # get a guess on friends
        if age > 9:
            self.friends = int((norm.rvs(size=1,loc=0.5,scale=0.15)[0]*10).round(0))
        else:
            self.friends = 0

        #get an estimate on associates based on age, employment rate and % going into work
        if age > 4 and age < 20:
            self.associates =  int((25*0.96).round(0))
        if age >19 and age < 65:
            self.associates = int((employment_rate*(worked_at_place/population)*random.randint(3,50)).round(0))
        else:
            self.associates = 2
        
        # get family size
        self.family = int(house_size.round(0))

        # total people being seen
        self.encounters = self.family+self.friends+ self.associates
    
    def wearMask(self):
        self.contagiousness /=2

def initiate_pandemic():
    population: int(input("Population: "))
    startingImmunity = int(input("Percentage of people with natural immunity: "))
    startingInfecters = int(input("How many people will be infectious at t=0: "))
    babies = int(input("Number of people aged 0-4: "))
    kids = int(input("Number of people aged 5-9: "))
    teens = int(input("Number of people aged 10-19: "))
    adults = int(input("Number of people aged 20-64: "))
    elders = int(input("Number of people aged 65+: "))

    house_size = float(input("Average household size: "))