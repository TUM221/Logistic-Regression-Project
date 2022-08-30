# -*- coding: utf-8 -*-
"""Logistic_Regression_Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PrFtLNJARVBOEUDuEP7jt6R0B4aW4HbK

# Logistic Regression Project


## Import Libraries
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

"""## Get the Data
**Read in the advertising.csv file and set it to a data frame called ad_data.**
"""

ad_data = pd.read_csv('advertising.csv')

"""**Check the head of ad_data**"""

ad_data.head()

"""** Use info and describe() on ad_data**"""

ad_data.info()

ad_data.describe()

"""## Exploratory Data Analysis

Use seaborn to explore the data

Try recreating the plots shown below

** Create a histogram of the Age**
"""

sns.set_style('whitegrid')
ad_data['Age'].hist(bins=30)
plt.xlabel('Age')

"""**Create a jointplot showing Area Income versus Age.**"""

sns.jointplot(x='Age',y='Area Income',data=ad_data)

"""**Create a jointplot showing the kde distributions of Daily Time spent on site vs. Age.**"""

sns.jointplot(x='Age',y='Daily Time Spent on Site',data=ad_data,color='red',kind='kde');

"""** Create a jointplot of 'Daily Time Spent on Site' vs. 'Daily Internet Usage'**"""

sns.jointplot(x='Daily Time Spent on Site',y='Daily Internet Usage',data=ad_data,color='green')

"""** Finally, create a pairplot with the hue defined by the 'Clicked on Ad' column feature.**"""

sns.pairplot(ad_data,hue='Clicked on Ad',palette='bwr')

"""# Logistic Regression

To do a train test split, and train the model

 The freedom here to choose columns that has to be used to train on

** Split the data into training set and testing set using train_test_split**
"""

from sklearn.model_selection import train_test_split

X = ad_data[['Daily Time Spent on Site', 'Age', 'Area Income','Daily Internet Usage', 'Male']]
y = ad_data['Clicked on Ad']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

"""** Train and fit a logistic regression model on the training set.**"""

from sklearn.linear_model import LogisticRegression

logmodel = LogisticRegression()
logmodel.fit(X_train,y_train)

"""## Predictions and Evaluations
** Now predict values for the testing data.**
"""

predictions = logmodel.predict(X_test)

"""** Create a classification report for the model.**"""

from sklearn.metrics import classification_report

print(classification_report(y_test,predictions))