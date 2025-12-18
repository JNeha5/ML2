import numpy as np

# ---------------------------
# STEP 1: Input Data
# ---------------------------

X = np.array([
    [60, 22],
    [62,25],
    [67,24],
    [70,20],
    [71,15],
    [72,14],
    [75,14],
    [78,11]
])

# Y values
y = np.array([140,155,159,179,192,200,212,215])

# ---------------------------
# STEP 2: Add Bias Term (1s)
# ---------------------------
X_bias = np.c_[np.ones(X.shape[0]), X]   # shape: (n_samples, 3)

# ---------------------------
# STEP 3: Normal Equation
# θ = (Xᵀ X)⁻¹ Xᵀ y
# ---------------------------
theta = np.linalg.inv(X_bias.T @ X_bias) @ (X_bias.T @ y)

# ---------------------------
# STEP 4: Print Results
# ---------------------------
print("Intercept (θ0):", theta[0])
print("Coefficient for x1 (θ1):", theta[1])
print("Coefficient for x2 (θ2):", theta[2])

# ---------------------------
# STEP 5: Prediction Example
# y = θ0 + θ1*x1 + θ2*x2
# ---------------------------
x1 = 5
x2 = 2
new_point = np.array([1, x1, x2])  # include bias 1

predicted_y = new_point @ theta
print("Predicted y for x1=5, x2=2:", predicted_y)
