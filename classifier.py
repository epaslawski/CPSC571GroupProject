"""
CPSC 571 F21 Project 

Authors: 
Erin Paslawski 10099039
Peter Nguyen 10096424
Bohyeon Cha 10162219

December 23 2021

Disease Spread Simulator
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from random import randint
from person import *

def classifier(random_people: list[Person], people_to_be_tested: list[Person]):

    '''
    This function takes two inputs,   
        1. list of randomly selected people for training the classifier (testing data)
        2. list of people to be tested (training data)
    and ouputs the updated list of tested people
    '''

    training_data = random_people
    testing_data = people_to_be_tested

    train_age = []
    train_works = []
    train_hh = []
    train_wp = []
    train_div = []
    train_cr = []
    train_if = []

    for p in training_data:
        
        train_age.append(p.age)
        train_works .append(p.works)
        train_hh.append(p.household)
        train_wp.append(p.workplace)
        train_div.append(p.division)
        train_cr.append(p.contagious_rating)
        train_if.append(p.infected)

    feature_vec = list(zip(train_age,train_works,train_hh,train_wp,train_div,train_cr))
    x_train = pd.DataFrame(feature_vec, columns =['age', 'works', 'household', 'workplace', 'division', 'contagious_rating'])
    y_train = pd.DataFrame(train_if, columns =['infected'])

    test_age = []
    test_works = []
    test_hh = []
    test_wp = []
    test_div = []
    test_cr = []
    test_if = []

    for p in testing_data:
        
        test_age.append(p.age)
        test_works .append(p.works)
        test_hh.append(p.household)
        test_wp.append(p.workplace)
        test_div.append(p.division)
        test_cr.append(p.contagious_rating)
        test_if.append(p.infected)

    feature_vec = list(zip(test_age,test_works,test_hh,test_wp,test_div,test_cr))
    x_test = pd.DataFrame(feature_vec, columns =['age', 'works', 'household', 'workplace', 'division', 'contagious_rating'])
    y_test = pd.DataFrame(test_if, columns =['infected'])


    dtree = DecisionTreeClassifier()
    dtree = dtree.fit(x_train, y_train)

    y_pred = dtree.predict(x_test)

    for i in range(len(y_pred)):
        testing_data[i].infected = y_pred[i]


    return testing_data



'''
random = [Person(1,0,3,4,1,4), Person(2,1,5,1,1,5), Person(3,0,3,3,3,3)]
to_be_tested = [Person(1,0,3,4,1,4), Person(2,1,5,1,1,5)]

random[1].infected = True

updated = classifier(random, to_be_tested)

for p in updated:
    print(p.infected)
'''
