from random import randint


def generate_workplace(workplaces):
    start, end = workplaces
    return randint(start,end+1)


def generate_household(households):
    start, end = households
    return randint(start,end+1)


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




