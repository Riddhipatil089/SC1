import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 1) TRIANGULAR MF
# -----------------------------
def triangular(x, a, b, c):
    """
    Triangular membership function.
    a = left point
    b = peak
    c = right point
    """
    return np.maximum(np.minimum((x - a) / (b - a), (c - x) / (c - b)), 0)


# -----------------------------
# 2) TRAPEZOIDAL MF
# -----------------------------
def trapezoidal(x, a, b, c, d):
    """
    Trapezoidal membership function.
    a,b = left slope
    c,d = right slope
    """
    return np.maximum(np.minimum(np.minimum((x-a)/(b-a), 1), (d-x)/(d-c)), 0)


# -----------------------------
# 3) GAUSSIAN MF
# -----------------------------
def gaussian(x, mean, sigma):
    """
    Gaussian membership function.
    mean = center
    sigma = spread (standard deviation)
    """
    return np.exp(-0.5 * ((x - mean) / sigma) ** 2)


# -----------------------------
# 4) GENERALIZED BELL (GBELL) MF
# -----------------------------
def gbell(x, a, b, c):
    """
    Generalized Bell membership function.
    a = width
    b = slope
    c = center
    """
    return 1 / (1 + np.abs((x - c) / a) ** (2 * b))


# -----------------------------
# 5) PI-SHAPED MF
# -----------------------------
def pi_curve(x, a, b, c, d):
    """
    Pi-shaped membership function.
    Combination of S function and Z function.
    """
    # S-curve (left side)
    s = np.where(x <= a, 0,
         np.where(x <= b, 2*((x-a)/(b-a))**2,
         np.where(x <= c, 1 - 2*((x-c)/(c-b))**2, 1)))

    # Z-curve (right side)
    z = np.where(x <= b, 1,
         np.where(x <= c, 1 - 2*((x-b)/(c-b))**2,
         np.where(x <= d, 2*((x-d)/(c-d))**2, 0)))

    # Combined
    return np.minimum(s, z)   # taking intersection


# -----------------------------
# 6) GAMMA MF
# -----------------------------
def gamma_mf(x, a, b):
    """
    Gamma membership function.
    a = start (foot)
    b = slope point
    """
    return np.where(x <= a, 0,
         np.where(x <= b, (x - a) / (b - a), 1))


# -----------------------------
# TEST & PLOT ALL MFs
# -----------------------------
x = np.linspace(0, 10, 500)

plt.figure(figsize=(12,10))

plt.subplot(3,2,1)
plt.plot(x, triangular(x, 2, 5, 8))
plt.title("Triangular MF")
plt.grid(True)

plt.subplot(3,2,2)
plt.plot(x, trapezoidal(x, 2, 4, 6, 8))
plt.title("Trapezoidal MF")
plt.grid(True)

plt.subplot(3,2,3)
plt.plot(x, gaussian(x, 5, 1))
plt.title("Gaussian MF")
plt.grid(True)

plt.subplot(3,2,4)
plt.plot(x, gbell(x, 2, 4, 5))
plt.title("G-Bell MF")
plt.grid(True)

plt.subplot(3,2,5)
plt.plot(x, pi_curve(x, 2, 4, 6, 8))
plt.title("Pi-shaped MF")
plt.grid(True)

plt.subplot(3,2,6)
plt.plot(x, gamma_mf(x, 2, 6))
plt.title("Gamma MF")
plt.grid(True)

plt.tight_layout()
plt.show()
