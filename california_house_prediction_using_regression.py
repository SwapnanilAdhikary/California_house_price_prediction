# -*- coding: utf-8 -*-
"""california_house_prediction using regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1j9ZNYJUm6DODUGXxzBGhw2kOeYXoAwaW
"""

#get california housing data set
from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing()

housing

import pandas as pd
housing_df = pd.DataFrame(housing["data"],columns=housing["feature_names"])
housing_df

housing_df["target"] = housing["target"]
housing_df.head()

housing_df =housing_df.drop("MdeHouseVal",axis=1)

housing_df

# import algorithm
from sklearn.linear_model import Ridge
import numpy as np
#setup random seed
np.random.seed(42)
#create data
x=housing_df.drop("target",axis=1)
y=housing_df["target"] #median house price in $100,000s
#split data(train , test)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)
#instantiate and fit the modle(on the training set)
model=Ridge()
model.fit(x_train,y_train)
#check the score of the model(on test set)
model.score(x_test,y_test)

