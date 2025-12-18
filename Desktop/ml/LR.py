X = [-2, -1, 0, 1, 2]
Y = [1, 2, 3, 3, 4]


def mean(values):
    return sum(values) / len(values)

# Step 2: Calculate slope 'm'
def calculate_slope(X, Y):
    n = len(X)
    
    sum_x = sum(X)
    sum_y = sum(Y)
    sum_xy = sum([X[i] * Y[i] for i in range(n)])
    sum_x2 = sum([X[i] ** 2 for i in range(n)])
    
    m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - (sum_x ** 2))
    return m

# Step 3: Calculate intercept 'c'
def calculate_intercept(X, Y, m):
    return mean(Y) - m * mean(X)

# Step 4: Predict function
def predict(x, m, c):
    return m * x + c


# ---- MAIN ----

m = calculate_slope(X, Y)
c = calculate_intercept(X, Y, m)

print("Slope (m):", m)
print("Intercept (c):", c)

# Predicting for new value
x_new = 6
y_pred = predict(x_new, m, c)

print(f"Prediction for x = {x_new} is y = {y_pred}")