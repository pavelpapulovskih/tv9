import numpy as np
zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
slope = 0
learning_rate = 0.0001
interactions = 100
# # среднеквадратичная ошибка
def mean_squared_error(y_true, y_pred):return np.mean((y_true - y_pred)**2)
# # градиент
def gradient(zp, ks, slope):return np.mean((slope * zp - ks) * zp)
# # градиентный спуск
for i in range (interactions):slope -= learning_rate * gradient (zp, ks, slope)
mse = mean_squared_error (ks, slope * zp)
print (f'Итерация {i+1}: Коэффициент склонности = {slope:.2f},Среднеквадратичная ошибка = {mse:.4f}')
print(f'Коэффициент склонности: {slope:.2f}')