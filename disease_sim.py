from scipy.stats import norm
import random
import time
import pandas as pd
peopleDictionary = []

# This class will define a person. It will have a scale on age, 
# if they go into work or school (based on age and employment rate), their household size

#simulation of a single person
class Person():
    def __init__(self, contagious_rating, household_size, work_size, infected,starting_immunity):
        if random.randint(0,100)<starting_immunity:
            self.immunity = True
        else:
            self.immunity = False
        self.contagiousness = contagious_rating*16
        self.contagiousDays = 0
        self.house_size = household_size
        self.work_size = work_size
        self.is_sick = bool(infected)
        self.mask = False
        self.contacts = household_size + work_size
    def wearMask(self):
        self.contagiousness /= 2

def initiateSim():
    col_names = ['contagious_rating', 'household_size', 'workplace_size', 'infected']
    people_df = pd.read_csv("people_test.csv", header=None,names=col_names)
    starting_immunity = int(input("Percentage of people with natural immunity: "))   
    numPeople = people_df.size
    for index, row in people_df.iterrows():
        contagiousness = row['contagious_rating']
        house_size = row['household_size']
        work_size = row['workplace_size']
        is_infected = row['infected']
        peopleDictionary.append(Person(contagiousness,house_size,work_size,is_infected,starting_immunity))
    daysContagious = 10
    lockdownDay = int(input("Day for lockdown to be enforced: "))
    maskDay = int(input("Day for masks to be used: "))
    return daysContagious, lockdownDay, maskDay

def runDay(daysContagious, lockdown):
    for person in [person for person in peopleDictionary if person.contagiousness>0 and person.contacts>0]:
        peopleCouldMeetToday = int(person.contacts/2)
        if peopleCouldMeetToday > 0:
            peopleMetToday = random.randint(0,peopleCouldMeetToday)
        else:
            peopleMetToday= person.house_size
        
        if lockdown == True:
            peopleMetToday= person.house_size

        for x in range(0,peopleMetToday):
            friendInQuestion = peopleDictionary[random.randint(0,len(peopleDictionary)-1)]
            if random.randint(0,100)<person.contagiousness and friendInQuestion.contagiousness == 0 and friendInQuestion.immunity==False:
                friendInQuestion.contagiousness = int((norm.rvs(size=1,loc=0.5,scale=0.15)[0]*10).round(0)*10)
                print(peopleDictionary.index(person), " >>> ", peopleDictionary.index(friendInQuestion))
                
    for person in [person for person in peopleDictionary if person.contagiousness>0]:
        person.contagiousDays += 1
        if person.contagiousDays > daysContagious:
            person.immunity = True
            person.contagiousness = 0
            print("|||", peopleDictionary.index(person), " |||")

lockdown = False
daysContagious, lockdownDay, maskDay = initiateSim()
saveFile = open("pandemicsave3.txt", "a")
for x in range(0,100):
    if x==lockdownDay:
        lockdown = True
        
    if x == maskDay:
        for person in peopleDictionary:
            person.wearMask()
            
    print("DAY ", x)
    runDay(daysContagious,lockdown)
    write = str(len([person for person in peopleDictionary if person.contagiousness>0])) + "\n"
    saveFile.write(write)
    print(len([person for person in peopleDictionary if person.contagiousness>0]), " people are contagious on this day.")
saveFile.close()