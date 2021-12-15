from random import randint


def generate_workplace(division):
    start, end = division.workplaces
    return randint(start,end)

def generate_household(division):
    start, end = division.households
    return randint(start,end)

def contagious_rating(age):

    if age <= 4 :
        return 1
    elif 5 <= age <= 9:
        return 2
    elif 10 <= age <= 14:
        return 3
    elif 15 <= age <= 19:
        return 4
    elif 20 <= age <= 64:
        return 5
    else:
        return 6

def generate_residents(population, age_0_4, age_5_9, age_10_14, age_15_19, age_20_64,\
                        age_65, avg_household_size, pop_density, emp_rate, worked):
    return []


