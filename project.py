import numpy as np
from sklearn.linear_model import LinearRegression

hours = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
marks = np.array([20, 40, 50, 70, 90])

model = LinearRegression()
model.fit(hours, marks)

predicted_marks = model.predict([[6]])

print("Predicted Marks:", predicted_marks)
