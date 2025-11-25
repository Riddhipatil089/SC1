import math

# Sigmoid activation
def s(x):
    return 1 / (1 + math.exp(-x))

# Sigmoid derivative
def sd(y):
    return y * (1 - y)

# Dataset for XOR
X = [(0,0), (0,1), (1,0), (1,1)]
T = [0, 1, 1, 0]

# Initial weights & learning rate
w1, w2 = 0.5, -0.5
lr = 0.5

print("Epoch wise predictions:")
for epoch in range(10):
    print(f"\nEpoch {epoch+1}")
    print("x1 x2  target  output")

    for (a, b), t in zip(X, T):
        # Forward pass
        z = a*w1 + b*w2
        o = s(z)

        print(a, b, " ", t, "   ", round(o, 4))

        # Backpropagation
        d = (t - o) * sd(o)  # error * derivative

        # Weight update
        w1 = w1 + lr * d * a
        w2 = w2 + lr * d * b

print("\nFinal weights:", w1, w2)
