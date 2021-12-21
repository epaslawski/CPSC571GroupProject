from os import times_result
from scipy.stats import norm
import random
import time
import pandas as pd
from person import Person
from classifier import *
from division import *
from utilities import *
import csv



def run_day(div, day, infected_days):
    name = div.name
    res_total = len(div.residents)

    if (day > 0 ):

        random.shuffle(div.residents)
        
        num_test = (res_total * 17) // 100 # 1/6 of population
        # create test list
        test_list = []
        # create training list
        training_list = []

        for x in range (0,res_total):
            
            per = div.residents[x]
            if (per.recovered == False):
                if len(test_list) < num_test:

                    if (per.infected == False):
                        test_list.append(per)
                    else:
                        training_list.append(per)
                else:
                    training_list.append(per)

        # run classifier
        if (len(training_list) > 0 and len(test_list) > 0):
            classifier_out = classifier(training_list,test_list)
        

    #return data list to add to csv
    active = 0
    new = 0
    recover = 0
    for per in div.residents:
        if per.infected == True:
            active += 1
            if (per.days_infected == 0):
                new += 1
            per.days_infected += 1
        if per.days_infected >= infected_days:
            per.infected = False
            per.recovered = True
        if per.recovered == True:
            recover += 1
    return [name, day, active,res_total, new, recover]

def main():

    # create output csv
    headers = ['division', 'day', 'active_cases', 'population', 'new_cases', 'recovered']

    sim_days = int(input("How many days to run the simulator: "))
    init_infect_pct = int(input("What percentage of the population is infected at day 0: "))
    infected_days = int(input("Numbers of days people are contagious with the disease: "))
    # create divisions and populations
    ds = initialize_divisions(init_infect_pct)
    with open('sim_out.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(headers)

        for x in range(0,sim_days):
            for div in ds:
                data = run_day(div, x, infected_days)
                if (div.name == 1):
                    print(data)
                writer.writerow(data)

if __name__ == "__main__":
    main()