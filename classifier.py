import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from random import randint

# Headings for the .csv file containing the sample
col_names = ['contagious_rating', 'household_size', 'workplace_size', 'infected']

sick = pd.read_csv("sample.csv", header=None, names=col_names)

# Columns that affect the decision tree
feature_cols = ['contagious_rating', 'household_size', 'workplace_size']
X = sick[feature_cols]
# The column that we are interested in, ie. if a person is infected or not
y = sick.infected

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

dtree = DecisionTreeClassifier()
dtree = dtree.fit(X_train.values, y_train)

#y_pred = dtree.predict(X_test)
#print(y_pred)
#print("Accuracy: ", metrics.accuracy_score(y_test, y_pred))

# The amount of people to be in the community
print("Specify how many people: ")
people = int(input())

# Preparing a data frame
myDict = {}
myDict["contagious_rating"] = []
myDict["household_size"] = []
myDict["workplace_size"] = []
myDict["infected"] = []

# Populating the data frame
for x in range(people):
    c_rating = randint(1,6)
    h_size = randint(1,8)
    w_size = randint(1,200)
    is_infected = dtree.predict([[c_rating, h_size, w_size]])
    #print(is_infected[0])
    myDict["contagious_rating"].append(c_rating)
    myDict["household_size"].append(h_size)
    myDict["workplace_size"].append(w_size)
    myDict["infected"].append(is_infected[0])

print(myDict)

# Output the dataframe into a csv file 
df = pd.DataFrame(myDict)
df.to_csv('tree_output.csv', index=False)
