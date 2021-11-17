from utilities import generate_residents

class Division:

    def __init__(self, division, population, avg_household_size, pop_density, employment_rate):
        self.division = division
        self.populaton = population
        self.avg_household_size = avg_household_size
        self.pop_density = pop_density
        self.employment_rate = employment_rate
        self.residents = generate_residents(population, avg_household_size, pop_density, employment_rate)
    
    #returns a list of residents
    def get_residents(self):
        return self.residents



division1 = Division("d1", 10000, 2.4, 4, 59.7)
print(division1.get_residents())