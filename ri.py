import numpy as np
import matplotlib.pyplot as plt

# Number of trials
num_trials = 1000

# Simulate dice rolls
dice_rolls = np.random.randint(1, 7, size=num_trials)

# Calculate running means
running_means = np.cumsum(dice_rolls) / np.arange(1, num_trials + 1)

# Plot the running mean over time
plt.plot(running_means, label='Running Mean')
plt.axhline(y=3.5, color='r', linestyle='--', label='Expected Value (3.5)')
plt.ylabel('Number of Rolls')
plt.xlabel('Running Mean')
plt.title('Law of Large Numbers Demonstration')
plt.legend()
plt.show()
