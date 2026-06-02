# Now we add matplotlib – just for drawing
import matplotlib.pyplot as plt

x = [1, 3.58, 3, 1.76]
y = [7.99, 4, 5, 6.4]

# scatter() puts dots at each (x,y) pair
plt.scatter(x, y, label="Data points")
N = len(x)
sum_x = sum(x)
sum_y = sum(y)
sum_xy = sum(x[i]*y[i] for i in range(N))
sum_x_sq = sum(x[i]**2 for i in range(N))

m = (N * sum_xy - sum_x * sum_y) / (N * sum_x_sq - sum_x**2)
b = (sum_y - m * sum_x) / N
line_y = [m * xi + b for xi in x]
plt.plot(x, line_y, color="red", label="Regression line")
print("Slope (m):", m)
print("Intercept (b):", b)

# Predict for a new x (e.g. study 5 hours)
new_x = 5
predicted_y = m * new_x + b
print("Predicted score for 5 hours:", predicted_y)
plt.xlabel("Study hours")
plt.ylabel("Exam score")
plt.legend()
plt.show()