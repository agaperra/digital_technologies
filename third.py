import numpy
from PIL import Image
import math
import matplotlib.pyplot as pyplot
import random
from sklearn.model_selection import GridSearchCV
from sklearn.neural_network import MLPClassifier
import pandas as pd

# Лабораторная работа №1 по курсу Цифровые технологии обработки информации
# часть 3

responses = numpy.zeros((1000, 100))
response_type = numpy.zeros(1000, int)

# учебный сет
for i in range(0, 1000):
    w0 = random.uniform(0.05, 0.5)  # резонансная частота
    dt = 0.1 / w0  # малый интервал времени
    Q = random.random()  # добротность
    if Q < 0.5:
        # апериодический
        D = math.sqrt(w0 * w0 * (1 / (Q * Q) - 4))
        l1 = (-w0 / (2 * Q) + D / 2)
        l2 = (-w0 / (2 * Q) - D / 2)
    else:
        if Q > 0.5:
            w = random.uniform(1, 20)
            Q = Q * w
            # колебательный
            D = math.sqrt(w0 * w0 * (4 - 1 / (Q * Q)))
            l1 = -w0 / (Q * 2)
            l2 = D / 2

    a = random.randint(-100, 100)
    b = random.randint(-100, 100)
    c = random.randint(-100, 100)
    for j in range(0, 100):
        t = j * dt
        if Q < 0.5:
            # апериодический
            responses[i, j] = a + math.exp(l1 * t) * b - math.exp(l2 * t) * b
            response_type[i] = -1
        else:
            if Q > 0.5:
                # колебательный
                responses[i, j] = a + b * math.exp(l1 * t) * math.sin(l2 * t + c)
                response_type[i] = 1

pyplot.plot(responses[10, :], 'o')
pyplot.show()

param_grid = {'max_iter': [5000],
              'activation': ['tanh'],  # функция перехода
              'alpha': [0.65],
              'hidden_layer_sizes': [10, 50, 20],
              'solver': ['lbfgs']}

grid_search = GridSearchCV(MLPClassifier(), param_grid, cv=2)
grid_search.fit(responses, response_type)

res = pd.DataFrame(grid_search.cv_results_)
print(res)
model_json = grid_search.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)

# responses_test = numpy.zeros((150, 100))
# response_type_test = numpy.zeros(150, int)
#
# # тестовый сет
# for i in range(0, 150):
#     w0 = random.uniform(0.05, 0.5)  # резонансная частота
#     dt = 0.1 / w0  # малый интервал времени
#     Q = random.random()  # добротность
#     if Q < 0.5:
#         # апериодический
#         D = math.sqrt(w0 * w0 * (1 / (Q * Q) - 4))
#         l1 = (-w0 / (2 * Q) + D / 2)
#         l2 = (-w0 / (2 * Q) - D / 2)
#     else:
#         if Q > 0.5:
#             w = random.uniform(1, 20)
#             Q = Q * w
#             # колебательный
#             D = math.sqrt(w0 * w0 * (4 - 1 / (Q * Q)))
#             l1 = -w0 / (Q * 2)
#             l2 = D / 2
#
#     a = random.randint(-100, 100)
#     b = random.randint(-100, 100)
#     c = random.randint(-100, 100)
#     for j in range(0, 100):
#         d = random.uniform(-1, 1)
#         t = j * dt
#         if Q < 0.5:
#             # апериодический
#             responses_test[i, j] = a + math.exp(l1 * t) * b - math.exp(l2 * t) * b + d * (a + b + c) / 100
#             response_type_test[i] = -1
#         else:
#             if Q > 0.5:
#                 # колебательный
#                 responses_test[i, j] = a + b * math.exp(l1 * t) * math.sin(l2 * t + c) + d * (a + b + c) / 100
#                 response_type_test[i] = 1
#
# store = grid_search.predict(responses_test)
# percent = store - response_type_test
# print(percent)
# count = 0
# for i in range(0, len(percent)):
#     if percent[i] == 0:
#         count = count + 1
# print("Точность:" + str(int(100 * count / len(percent))) + "%")
