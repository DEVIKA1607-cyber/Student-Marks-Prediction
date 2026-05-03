## Name: D DEVIKA 

## Register Number: 212224100010 

## Title 

Student Marks Prediction using Machine Learning 

## About 

This project uses Machine Learning to predict student marks based on the number of hours studied. Linear Regression is used to find the relationship between study time and marks. This helps in understanding how effort affects performance. 

## Algorithm 

Start  

Import required libraries (NumPy, Linear Regression)  

Define input data (hours studied)  

Define output data (marks)  

Create Linear Regression model  

Train the model using data  

Predict marks for new input  

Display the result  

Stop  

## Code 

import numpy as np 
from sklearn.linear_model import LinearRegression 
 
hours = np.array([1, 2, 3, 4, 5]).reshape(-1, 1) 
marks = np.array([20, 40, 50, 70, 90]) 
 
model = LinearRegression() 
model.fit(hours, marks) 
 
predicted_marks = model.predict([[6]]) 
 
print("Predicted Marks:", predicted_marks) 

 

## Screenshot 
<img width="1920" height="1200" alt="image" src="https://github.com/user-attachments/assets/cf56ca83-a682-4e07-97fc-998dfa177182" /> 

## Result

This project shows how Machine Learning can predict student performance based on study hours. It helps in analyzing the relationship between input and output data using Linear Regression.
