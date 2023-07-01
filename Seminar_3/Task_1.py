import scipy.stats as stats
import numpy as np

# x = np.array([2.5, 2.2, 2.6, 2, 2.1, 1.8, 2.4, 2.3, 2.7, 2.7, 1.9])

# y = np.array([2.5, 1.7, 1.5, 2.5, 1.4, 1.9, 2.3, 2.0, 2.6, 2.3, 2.2])

# print(stats.ttest_ind(x,y))

# t = (np.mean(x) - np.mean(y))/np.sqrt(np.var(x, ddof=1)/len(x) + np.var(y,ddof=1)/len(y))
# print(t)
# t1 = stats.t.ppf(0.95,20)

# t = ((2.71 - 2.63) / np.sqrt(0.71**2 / 200 + 0.73**2 / 200))
# print(t)
# print(stats.t.ppf(0.975,398))

print(stats.norm.ppf(0.975))