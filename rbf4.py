import numpy as np

# Input XOR data
X = np.array([[0,0], [0,1], [1,0], [1,1]])
T = np.array([[0], [1], [1], [0]])   # column vector

# RBF centers
C = np.array([[0,0], [1,1]])

# RBF Layer (Gaussian kernel)
H = np.exp(-np.sum((X[:, None, :] - C[None, :, :])**2, axis=2))

# Compute weights using least squares
W = np.linalg.pinv(H).dot(T)

# Prediction
Y = H.dot(W)

# MSE Error
print("Outputs:\n", np.round(Y, 4))
print("MSE =", np.mean((T - Y)**2))