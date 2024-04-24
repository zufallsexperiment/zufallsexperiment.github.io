import numpy as np
import matplotlib.pyplot as plt

# Number of trials
num_trials = 1000

# Simulate dice rolls
dice_rolls = np.random.randint(1, 7, size=num_trials)

# Calculate running means and running variances
running_means = np.cumsum(dice_rolls) / np.arange(1, num_trials + 1)

# Calculate the squared differences from the running mean to determine the variance
squared_diff = (dice_rolls - running_means[:, None]) ** 2
running_variance = np.cumsum(squared_diff) / np.arange(1, num_trials + 1)

# Plot the running mean over time
plt.figure(figsize=(12, 6))

# Plotting the running mean
plt.subplot(1, 2, 1)
plt.plot(running_means, label='Running Mean')
plt.axhline(y=3.5, color='r', linestyle='--', label='Expected Mean (3.5)')
plt.xlabel('Number of Rolls')
plt.ylabel('Running Mean')
plt.title('Law of Large Numbers - Mean')
plt.legend()

# Plotting the running variance
plt.subplot(1, 2, 2)
plt.plot(running_variance[:, 0], label='Running Variance')
plt.axhline(y=2.92, color='r', linestyle='--', label='Expected Variance (2.92)')
plt.xlabel('Number of Rolls')
plt.ylabel('Running Variance')
plt.title('Law of Large Numbers - Variance')
plt.legend()

plt.tight_layout()
plt.show()
