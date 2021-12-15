from utilities import generate_workplace, generate_household
import csv

class Division:

    def __init__(self, name, population, age_0_4, age_5_9, age_10_14,\
                                        age_15_19, age_20_64, age_65, avg_household_size,\
                                        pop_density, emp_rate, worked, workplaces, households):
        self.name = name
        self.populaton = population
        self.age_0_4 = age_0_4
        self.age_5_9 = age_5_9
        self.age_10_14 = age_10_14
        self.age_15_19 = age_15_19
        self.age_20_64 = age_20_64
        self.age_65 = age_65
        self.avg_household_size = avg_household_size
        self.pop_density = pop_density
        self.emp_rate = emp_rate
        self.worked = worked
        self.workplaces = workplaces  
        self.households = households    
        #self.residents = generate_residents(population, age_0_4, age_5_9, age_10_14, age_15_19, age_20_64,\
        #                                     age_65, avg_household_size, pop_density, emp_rate, worked)
        
    #returns a list of residents
    def get_residents(self):
        return self.residents





def initialize_divisons():
    '''
    This method returns a list of divisions.
    All divisions from the data are parsed and initialized inside this method.
    '''

    divisions = [] 

    with open('data.csv', mode='r') as data_file:

        WORK_OVERLAP = 30        # overlap in workplaces in case of inter-division employees
        wp_start = 0           
        wp_end = 0

        h_start = 0
        h_end = 0

        csv_reader = csv.DictReader(data_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                #print(f'{", ".join(row)}')
                line_count += 1
            else:
                name = row["Division"]
                population = row["Population"]
                age_0_4 = row["0-4"]
                age_5_9 = row["5-9"]
                age_10_14 = row["10-14"]
                age_15_19 = row["15-19"]
                age_20_64 = row["20-64"]
                age_65 = row["65+"]
                avg_household_size = row["Average Household Size"]
                pop_density = row["Population density"]
                emp_rate = row["Employment Rate"]
                worked = row["Worked at usual place"]


                wp_end = wp_start + float(worked)//80              #assume 80 people work in on place on average
                workplaces = (wp_start,wp_end)                    
                wp_start = wp_end - WORK_OVERLAP

                h_end = h_start + int(population)//float(avg_household_size)
                households = (h_start,h_end)
                h_start = h_end + 1


                divisions.append(Division(name, int(population), int(age_0_4), int(age_5_9), int(age_10_14),\
                                            int(age_15_19), int(age_20_64), int(age_65), float(avg_household_size),\
                                            float(pop_density), float(emp_rate), int(worked), workplaces, households ))
                
    return divisions



'''
ds = initialize_divisons()
for d in ds:
    #print(d.workplaces)
    #print(generate_workplace(d))
    print(d.households)
    print(generate_household(d))
'''