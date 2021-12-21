from scipy.stats import norm
import random
import time
import pandas as pd
from person import Person
from classifier import *
from division import *
from utilities import *
import csv



def run_day(div, day):
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

            if len(test_list) < num_test:

                if (per.infected == False):
                    test_list.append(per)
                else:
                    training_list.append(per)
            else:
                training_list.append(per)

        # run classifier
        classifier_out = classifier(training_list,test_list)
        
        

    #return data list to add to csv
    active = 0

    for per in div.residents:
        if per.infected == True:
            active += 1
    return [name, day, active,res_total]

def main():

    # create output csv
    headers = ['division', 'day', 'active_cases', 'population']

    sim_days = int(input("How many days to run the simulator: "))
    init_infect_pct = int(input("What percentage of the population is infected at day 0: "))

    # create divisions and populations
    ds = initialize_divisions(init_infect_pct)
    with open('sim_out.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(headers)

        for x in range(0,sim_days):
            for div in ds:
                data = run_day(div, x)
                print(data)
                writer.writerow(data)

if __name__ == "__main__":
    main()