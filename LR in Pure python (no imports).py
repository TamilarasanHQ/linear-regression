# Linear Regression in Pure Python – no imports
x = [1, 2, 3, 4]
y = [2, 4, 5, 4.5]

N = len(x)
sum_x = sum(x)
sum_y = sum(y)
sum_xy = sum(x[i]*y[i] for i in range(N))
sum_x_sq = sum(x[i]**2 for i in range(N))

m = (N * sum_xy - sum_x * sum_y) / (N * sum_x_sq - sum_x**2)
b = (sum_y - m * sum_x) / N

print("Slope (m):", m)
print("Intercept (b):", b)

# Predict for a new x (e.g. study 5 hours)
new_x = 5
predicted_y = m * new_x + b
print("Predicted score for 5 hours:", predicted_y)