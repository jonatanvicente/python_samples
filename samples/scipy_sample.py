import numpy as np
from scipy.optimize import minimize

# Define the objective function
def objective_function(x):
    return x**2 + 5*np.sin(x)

# Initial guess
x0 = 2.0

# Perform the optimization
result = minimize(objective_function, x0)

# Print the result
print("Optimal value:", result.x)
print("Objective function value at optimal point:", result.fun)