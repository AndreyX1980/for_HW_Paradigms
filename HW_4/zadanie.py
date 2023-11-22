import math
from functools import reduce
#Вычисляем среднее значение для каждого массива x и y
def mean(array):
    return sum(array) / float(len(array))

def pearson_correlation(x, y):
    x_mean = mean(x)
    y_mean = mean(y)
#Вычисляем числитель и знаменатель
    numerator = sum((xi - x_mean) * (yi - y_mean) for xi, yi in zip(x, y))
    denominator = math.sqrt(sum((xi - x_mean) ** 2 for xi in x) * sum((yi - y_mean) ** 2 for yi in y))

    return round(numerator / denominator, 2)
#Задаем значение массивов
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 6, 8]

#проверим
correlation = pearson_correlation(x, y)
print(f"Значение корреляции Пирсона: {correlation}")