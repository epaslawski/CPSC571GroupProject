from utilities import *
from person import *
import csv
import random 

class Division:

    def __init__(self, name, population, age_0_4, age_5_9, age_10_14,\
                                        age_15_19, age_20_64, age_65, avg_household_size,\
                                        pop_density, emp_rate, workplaces, households, residents):
        self.name = name
        self.population = population
        self.age_0_4 = age_0_4
        self.age_5_9 = age_5_9
        self.age_10_14 = age_10_14
        self.age_15_19 = age_15_19
        self.age_20_64 = age_20_64
        self.age_65 = age_65
        self.avg_household_size = avg_household_size
        self.pop_density = pop_density
        self.emp_rate = emp_rate
        self.workplaces = workplaces  
        self.households = households    
        self.residents = residents
        




def initialize_divisions(init_infection_pct):
    '''
    This function returns a list of divisions.
    All divisions from the data file are parsed and initialized inside this function.
    '''

    divisions = [] 

    with open('data.csv', mode='r') as data_file:

        WORK_OVERLAP = 30        # overlap in workplaces in case of inter-division employees
        wp_start = 1           
        wp_end = 0

        h_start = 1
        h_end = 0

        csv_reader = csv.DictReader(data_file)

        for row in csv_reader:
            name = int(row["Division"])
            population = int(row["Population"])//10
            age_0_4 = int(row["0-4"])//10
            age_5_9 = int(row["5-9"])//10
            age_10_14 = int(row["10-14"])//10
            age_15_19 = int(row["15-19"])//10
            age_20_64 = int(row["20-64"])//10
            age_65 = int(row["65+"])//10
            avg_household_size = float(row["Average Household Size"])
            pop_density = float(row["Population density"])
            emp_rate = float(row["Employment Rate"])/100

            # create a tuple that represents the range of workplaces in this division
            adult_pop = age_20_64 + age_65
            wp_end = wp_start + (adult_pop*emp_rate)//10              #assume 10 people work in on place on average
            workplaces = (wp_start,wp_end)                    
            wp_start = wp_end - WORK_OVERLAP

            # create a tuple that represents the range of households in this division
            h_end = h_start + int(population)//float(avg_household_size)
            households = (h_start,h_end)
            h_start = h_end + 1

            num_infected = (population*init_infection_pct ) // 100

            residents = generate_residents(num_infected, name, emp_rate, workplaces, households, age_0_4, age_5_9, age_10_14, age_15_19, age_20_64, age_65, pop_density)


            divisions.append(Division(name, population, age_0_4, age_5_9, age_10_14,\
                                        age_15_19, age_20_64, age_65, avg_household_size,\
                                        pop_density, emp_rate, workplaces, households, residents ))
            
            
    return divisions





def generate_residents(num_infected, name, emp_rate, workplaces, households, age_0_4, age_5_9, age_10_14, age_15_19, age_20_64, age_65, pop_density):

    '''
    This is a helper function for initialize_divisions().
    It generates and returns a list of residents(people) in a division.

    It also randomly infects a percentage of the population.
    '''

    residents = []

    working20 = int((age_20_64*emp_rate)//1)
    working65 = int((age_65*emp_rate)//1)
    

    for i in range(age_0_4):
        residents.append(Person(0, False, generate_household(households), 0, name, contagious_rating(0, pop_density)))
    
    for i in range(age_5_9):
        residents.append(Person(1, False, generate_household(households), 0, name, contagious_rating(1, pop_density)))

    for i in range(age_10_14):
        residents.append(Person(2, False, generate_household(households), 0, name, contagious_rating(2, pop_density)))
    
    for i in range(age_15_19):
        residents.append(Person(3, False, generate_household(households), 0, name, contagious_rating(3, pop_density)))
    
    for a in range(working20+1):
        residents.append(Person(4, True, generate_household(households), generate_workplace(workplaces), name, contagious_rating(4, pop_density)))
        
    for b in range(age_20_64-working20+1):
        residents.append(Person(4, False, generate_household(households), 0, name, contagious_rating(4, pop_density)))

    for a in range(working65+1):
        residents.append(Person(5, True, generate_household(households), generate_workplace(workplaces), name, contagious_rating(5, pop_density)))
        
    for b in range(age_65-working65+1):
        residents.append(Person(5, False, generate_household(households), 0, name, contagious_rating(5, pop_density)))
    

    random.shuffle(residents)

    for x in range (0,num_infected):
        residents[x].infected = True

    infected = 0
    for per in residents:
        if per.infected == True:
            infected+=1
    return residents

'''
ds = initialize_divisions()

for d in ds:
    print(d.name, '\t',len(d.residents), '\t', d.residents[5].contagious_rating)

'''