import numpy as np
# Данные
zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])
# 1.1 Ковариация и коэффициент наклона без intercept
mean_zp = np.mean(zp)
mean_ks = np.mean(ks)
b = np.sum((zp - mean_zp) * (ks - mean_ks)) / np.sum((zp - mean_zp)** 2)
print(f"Коэффициент наклона (b) без intercept: {b}")
# 1.2 Коэффициенты регрессии с intercept
a = mean_ks - b * mean_zp
print(f"Коэффициент наклона (b) с intercept: {b}")
print(f"Intercept (a): {a}")