import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split;
from sklearn.metrics import mean_squared_error

regressor=LinearRegression();


dataset=pd.read_csv('Boston.csv');

X=  dataset[['Unnamed: 0','crim','zn','indus','chas','nox','rm','age','dis','rad','tax','ptratio', 'black', 'lstat' ]]



y=dataset['medv']


x_train,x_test,y_train, y_test,=train_test_split(X,y,test_size=0.3)

regressor.fit(x_train,y_train)

#pylint: disable-msg=R0913
y_pred=regressor.predict(x_test)

mse=mean_squared_error(y_test,y_pred)

plt.scatter(y_test,y_pred)
plt.xlabel("Prices $Y_i")
plt.ylabel("Predicted Prices $\hat{Y}_i$")
plt.title("Prices versus Predicted Prices");
plt.show();
