import numpy as np

# -----------------------------
# Feature: Lawn size (x2)
# -----------------------------
x2 = np.array([
    14, 14.8, 16, 16.4, 16.8, 17.2, 17.6, 17.6, 17.6,
    18.4, 18.4, 18.8, 19.2, 19.6, 20, 20,
    20.4, 20.8, 20.8, 20.8, 21.6, 22, 22.4, 23.6
])

# -----------------------------
# Class labels
# Owner = 1, Nonowner = 0
# (24 labels — MUST match x2)
# -----------------------------
y = np.array([
    0,0,0,0,0,0,0,0,0,
    0,0,0,
    1,1,1,1,
    1,1,1,1,
    1,1,1,1
])

# -----------------------------
# Gini function
# -----------------------------
def gini(labels):
    classes, counts = np.unique(labels, return_counts=True)
    probs = counts / counts.sum()
    return 1 - np.sum(probs ** 2)

# -----------------------------
# Sort x2 and y together
# -----------------------------
sorted_idx = np.argsort(x2)
x2_sorted = x2[sorted_idx]
y_sorted = y[sorted_idx]

# -----------------------------
# Generate midpoints
# -----------------------------
midpoints = [
    (x2_sorted[i] + x2_sorted[i + 1]) / 2
    for i in range(len(x2_sorted) - 1)
]

# -----------------------------
# Evaluate each split
# -----------------------------
best_gini = float("inf")
best_split = None

for split in midpoints:
    left = y_sorted[x2_sorted <= split]
    right = y_sorted[x2_sorted > split]

    if len(left) == 0 or len(right) == 0:
        continue

    weighted_gini = (
        len(left) / len(y_sorted) * gini(left) +
        len(right) / len(y_sorted) * gini(right)
    )

    print(f"Split at {split:.1f} -> Gini = {weighted_gini:.3f}")

    if weighted_gini < best_gini:
        best_gini = weighted_gini
        best_split = split

print("\nBest Split:")
print("x2 <=", best_split)
print("Minimum Gini =", round(best_gini, 3))

