# Code to test the central limit theorem on exponential distributions

import numpy as np
import matplotlib.pyplot as plt

sample_size = 35
iters = 3000
beta = 1
bins = 50

sample=[np.mean([np.random.exponential(beta) for i in range(sample_size)]) for j in range(iters)]

plt.hist(sample, bins=bins)
plt.show()
