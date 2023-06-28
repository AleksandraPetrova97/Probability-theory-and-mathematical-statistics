import scipy.stats as stats
import numpy as np
x = np.array([2.5, 2.2, 2.6, 2, 2.1, 1.8,2.4, 2.3, 2.7, 2.7, 1.9])

y= np.array([2.5, 1.7, 1.5, 2.5, 1.4, 1.9, 2.3, 2.0, 2.6, 2.3, 2.2])

print(stats.ttest_ind(x,y))

