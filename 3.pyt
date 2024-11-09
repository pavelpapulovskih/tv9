import numpy as np
zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
# Начальные коэффициенты
w = 0
b = 0
# Скорость обучения
alfa = 0.001
# Количество итераций
n_iter = 100
# Среднеквадратичная ошибка
def compute_mse (y_true, y_pred):return np.mean ((y_true - y_pred)**2)
# Градиентный спуск
for i in range (n_iter):y_predict = w * zp + b
errors = y_predict - ks
dw = (2 / len (zp)) * np.dot(zp, errors)
db = (2 / len (zp)) * np.sum(errors)
w -= alfa * dw
b -= alfa * db
if i % 10 == 0:mse = compute_mse (ks, y_predict)
print (f'Interaction {i}: MSE = {mse}, w = {w}, b = {b}')
print(f'Итоговые значения коэффициента при zp = {w}, b = {b}')