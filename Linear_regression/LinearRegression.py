
import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
import matplotlib.pyplot as plt

data = pd.read_csv("student-mat.csv", sep=";")
data.head()
data.shape
data.columns

data.columns
data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]
data.shape
predict = "G3"

x = np.array(data.drop([predict], 1)) #Features
y = np.array(data[predict]) #labels
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x,y,test_size = 0.1)
linear = linear_model.LinearRegression()
linear.fit(x_train, y_train)
acc = linear.score(x_test, y_test)
print(acc)
print('Coefficient: \n', linear.coef_) # These are each slope value
print('Intercept: \n', linear.intercept_) # This is the intercept
predictions = linear.predict(x_test) # Gets a list of all predictions

for x in range(len(predictions)):
    print(predictions[x], x_test[x], y_test[x])
import pickle
with open("linear_regression_model.pickle","wb") as f:
    pickle.dump(linear, f)
linear_data = open("linear_regression_model.pickle","rb")
linear = pickle.load(linear_data)
