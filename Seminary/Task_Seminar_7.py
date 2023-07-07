import scipy.stats as stats
import numpy as np

# X = np.array([20,17, 14, 42, 50, 62, 8, 49, 81, 54, 48, 55, 56])
# Y = np.array ([20, 26, 1, 24, 1, 47, 15, 7, 65, 9, 21, 36, 30])

# X_1 = np.array([ 32, 41, 51, 29, 76, 47, 60, 58, 40, 64, 73, 66, 73])
# Y_1 = np.array ([42, 90, 71, 47, 56, 43, 137, 63, 28, 60, 87, 69, 50])

# print(stats.wilcoxon(X,Y))
# print(stats.wilcoxon(X_1,Y_1))

# print(X_1-Y_1)


# A = np.array([3.5, 3.3, 4.9, 3.6])
# B = np.array([8.6, 5.4, 8.8, 5.6])
# C = np.array([5.1, 8.6, 7.7, 5.0])

# print(stats.friedmanchisquare(A,B,C))

# n = 4
# k = 3                                                                                                                                                                                 
# R1 = 4
# R2 = 11
# R3 = 9
# R = n * (k + 1) / 2
# print(R)
# print(12 / (n * k * (k + 1)) * ((R1 - R)**2 + (R2 - R)**2 + (R3 - R)**2))

gr1 =([0.5, 0.7, 1, 1.2, 1.4])

gr2 = ([1.3, 1.45, 1.6, 1.7, 1.8])

gr3 = ([6.2, 12.6, 13.2, 14.1, 14.2])

print(stats.kruskal(gr1,gr2,gr3))

N = 15
T1 = 16
T2 = 39
T3 = 65
n = 5
print(12 / (N * (N + 1)) * (T1**2/n + T2**2/n + T3**2/n) - 3 * (N + 1)) 