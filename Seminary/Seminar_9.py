# # Постройте графики для приведенных наборов данных. Найдите коэффициенты для линии
# # регрессии и коэффициенты детерминации. Что вы замечаете? Нанесите на график модель
# # линейной регрессии.

# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression

# X1= np.array([30,30,40, 40])
# Y1= np.array([37, 47, 50, 60])

# x2= np.array([30,30,40, 40, 20, 20, 50, 50])
# y2= np.array([37, 47, 50, 60, 25, 35, 62, 72])

# X3 = np.array([30,30,40, 40, 20, 20, 50, 50, 10, 10, 60, 60])
# Y3 = np.array([37, 47, 50, 60, 25, 35, 62, 72, 13, 23, 74, 84]) 

# models = [[X1, Y1],[x2,y2],[X3,Y3]]

# fig, axis = plt.subplots(3,1)
# for i in range(len(models)):
#     cor = np.corrcoef(models[i])[0][1]
#     axis[i].scatter(models[i][0], models[i][1])
#     axis[i].set_title(f'r={round(cor,3)}')

# plt.tight_layout()   
# # plt.show()

# # reshape
# for i in range(len(models)):
#     models[i][0] = models[i][0].reshape(-1,1)

# # regression
# for i in  range(len(models)):
#     model= LinearRegression()
#     model.fit(models[i][0], models[i][1])
#     r_sq = model.score(models[i][0], models[i][1])
#     print(f'model {i + 1}')
#     print(f'R2: {round(r_sq, 3)}')
#     print(f'const: {round(model.intercept_, 3)}')
#     print(f'beta: {model.coef_}')
#     print('-' * 30)

# #plot
# fig, axis = plt.subplots(3,1)
# for i in range(len(models)):
#     x = models[i][0]
#     y = models[i][1]
#     model = LinearRegression()
#     model.fit(x, y)
#     r_sq = model.score(x, y)
#     const = model.intercept_
#     beta = model.coef_[0]

#     axis[i].scatter(x, y)
#     axis[i].set_title(f'R2 = {round(r_sq, 3)}')

#     axis[i].plot(x, beta * x + const, 'g')

# plt.tight_layout()
# plt.show()    



import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

x1 = np.array([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5])
y1 = np.array([8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68])

plt.subplot(231)
plt.scatter(x1, y1)
plt.title('Experiment 1')
coef1, pval1 = stats.pearsonr(x1, y1)
plt.xlabel('x')
plt.ylabel('y')
plt.text(4, 11, f'r={coef1:.2f}')


plt.tight_layout()
plt.show()