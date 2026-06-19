from sklearn.linear_model import LinearRegression
import numpy as np

x = np.array([[1],[2],[3],[4],[5],[6]])
y = np.array([10,20,30,40,50,60])

model = LinearRegression()
model.fit(x, y)

pred = model.predict([[8]])

print("Predicted Salary:", pred[0])