
import scipy.stats as stats
import numpy as np
# print(stats.norm.ppf(0.975)) 
print(71.2-stats.t.ppf(0.95,99)*np.sqrt(3.6)/np.sqrt(100), 71.2+stats.t.ppf(0.95,99)*np.sqrt(3.6)/np.sqrt(100))