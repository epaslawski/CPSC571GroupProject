import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

col_names = ['contagious_rating', 'household_size', 'workplace_size', 'infected']

sick = pd.read_csv("sample.csv", header=None, names=col_names)


feature_cols = ['contagious_rating', 'household_size', 'workplace_size']
X = sick[feature_cols]
y = sick.infected

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

dtree = DecisionTreeClassifier()

dtree = dtree.fit(X_train, y_train)

y_pred = dtree.predict(X_test)

print(y_pred)
print("Accuracy: ", metrics.accuracy_score(y_test, y_pred))

person = dtree.predict([[6,7,8]])

print(person)
