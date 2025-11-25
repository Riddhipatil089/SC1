import tensorflow as tf # type: ignore
import numpy as np

# Training data
x = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([2, 4, 6, 8, 10], dtype=float)

# Model: single neuron
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(1,)),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer='sgd', loss='mse')

model.fit(x, y, epochs=200, verbose=0)

# Prediction
print("Prediction for x=6:", model.predict(np.array([[6.0]]))[0])


