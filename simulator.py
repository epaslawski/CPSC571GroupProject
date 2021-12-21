from scipy.stats import norm
import random
import time
import pandas as pd
from .person import Person
from .classifier import *
from .division import *
from .utilities import *
import csv


def run_day(division) -> list[str]:
    # create test list


    # create training list


    # run classifier


    #return data list to add to csv

def main():
    # create divisions and populations
    ds = initialize_divisions()

    # create output csv
    headers = ['division', 'day', 'active_cases', 'recovered']

    sim_days = int(input("How many days to run the simulator: "))

    with open('sim_out.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(headers)

        for x in range(0,sim_days):
            for div in ds:
                data = run_day(div)
                writer.writerow(data)

    

if __name__ == "__main__":
    main()