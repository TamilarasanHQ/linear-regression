import numpy as np

# Your data as numpy arrays (fast number lists)
x = np.array([1, 2, 3, 4])
y = np.array([2, 4, 5, 4.5])

# All those sums become one-liners
N = len(x)
m = (N * np.sum(x*y) - np.sum(x)*np.sum(y)) / (N * np.sum(x**2) - (np.sum(x))**2)
b = (np.sum(y) - m * np.sum(x)) / N

print(m, b)  # same result, less typing