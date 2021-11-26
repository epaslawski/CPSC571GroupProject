from utilities import contagious_rating, generate_household, generate_workplace

class Person:

    def __init__(self, age, division):
        self.age = age
        self.division = division
        self.contagious_rating = contagious_rating(age)
        self.household = generate_household(division)
        self.workplace = generate_workplace(division)
        self.days_infectious = 10               # number of days this person is infectious
        
    
    
    

