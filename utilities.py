from random import randint


def generate_workplace(workplaces):
    start, end = workplaces
    return randint(start,end+1)


def generate_household(households):
    start, end = households
    return randint(start,end+1)


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




