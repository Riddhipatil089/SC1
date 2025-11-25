from minisom import MiniSom
import numpy as np
import matplotlib.pyplot as plt

# --- 1. Generate Sample Data ---
# Simulate 100 samples belonging to two different "character" clusters.
# Input features are typically normalized between 0 and 1.
N_SAMPLES = 100
N_FEATURES = 3 # e.g., features derived from a character image
np.random.seed(42)

# Cluster 1 (Low features: simulating a character like 'C')
data_c1 = np.random.rand(N_SAMPLES // 2, N_FEATURES) * 0.2 
# Cluster 2 (High features: simulating a character like 'A')
data_c2 = np.random.rand(N_SAMPLES // 2, N_FEATURES) * 0.8 + 0.2

data = np.concatenate([data_c1, data_c2], axis=0)
# Create simple labels for visualization (0 for C1, 1 for C2)
labels = np.array([0] * (N_SAMPLES // 2) + [1] * (N_SAMPLES // 2))

# --- 2. Initialize and Train the SOFM ---
MAP_SIZE = (5, 5) 
EPOCHS = 500 # Increased epochs for better separation

# som = MiniSom(Map Height, Map Width, Input Dimension, sigma, learning_rate)
som = MiniSom(
    MAP_SIZE[0], MAP_SIZE[1], N_FEATURES,
    sigma=1.0, 
    learning_rate=0.5,
    random_seed=42
)

# Initialize weights to span the data space
som.pca_weights_init(data) 

# Train the map
som.train_random(data, EPOCHS) 

# --- 3. Evaluation and Mapping ---
# Find the Best Matching Unit (BMU) for every input vector
# bmu_map[i] will contain the (row, col) coordinates of the BMU for data[i]
bmu_map = np.array([som.winner(x) for x in data])

# --- 4. Display Results and Visualization ---
print("--- SOFM for Character Recognition Results ---")
print(f"Trained a {MAP_SIZE[0]}x{MAP_SIZE[1]} SOFM map over {EPOCHS} epochs.")

# Check how the two clusters mapped (First sample from C1, First sample from C2)
bmu_c1 = som.winner(data[0])
bmu_c2 = som.winner(data[N_SAMPLES // 2])
print(f"Cluster 1 ('C') sample mapped to neuron: {bmu_c1}")
print(f"Cluster 2 ('A') sample mapped to neuron: {bmu_c2}")


# Visualization: Plotting the Mapped Clusters
plt.figure(figsize=(8, 8))
# Assign a unique color/marker to each cluster
colors = ['r', 'b'] # Red for Cluster 1, Blue for Cluster 2
markers = ['s', 'o'] # Square for Cluster 1, Circle for Cluster 2

for i, (x, y) in enumerate(bmu_map):
    plt.plot(x + 0.5, y + 0.5, 
             markers[labels[i]], 
             markerfacecolor='None',
             markeredgecolor=colors[labels[i]], 
             markersize=10, 
             markeredgewidth=2)

# Plot the winning nodes' coordinates
plt.xticks(np.arange(MAP_SIZE[1])); 
plt.yticks(np.arange(MAP_SIZE[0]))
plt.grid(color='gray', linestyle='-', linewidth=0.5)

plt.title('SOFM Map: Unsupervised Clustering of Characters')
plt.xlabel('Map Row Index')
plt.ylabel('Map Column Index')
plt.show()