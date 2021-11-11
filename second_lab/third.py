import math

import numpy as np
from PIL import Image
from matplotlib import pyplot as plt

image1 = Image.open(r"C:\Users\Agaperra\PycharmProjects\digital_technologies\imageFirst.png")
w, h = image1.size
# print(w, h)
image_bytes1 = image1.tobytes()
data_bytes1 = bytearray(image_bytes1)

image2 = Image.open(r"C:\Users\Agaperra\PycharmProjects\digital_technologies\imageSecond.png")
w1, h1 = image2.size
# print(w, h)
image_bytes2 = image2.tobytes()
data_bytes2 = bytearray(image_bytes2)

image3 = Image.open(r"C:\Users\Agaperra\PycharmProjects\digital_technologies\паук.jpg")
w2, h2 = image3.size
# print(w, h)
image_bytes3 = image3.tobytes()
data_bytes3 = bytearray(image_bytes3)


def euclid(data_bytes, bytes_correct):
    data = np.zeros(len(bytes_correct))
    for i in range(0, len(bytes_correct) - 2):
        data[i] = math.sqrt(
            pow(data_bytes[i + 0] - bytes_correct[i + 0], 2)
            + pow(data_bytes[i + 1] - bytes_correct[i + 1], 2)
            + pow(data_bytes[i + 2] - bytes_correct[i + 2], 2))
    return data


def mean(array_data):
    means = 0
    for i in range(0, len(array_data)):
        means = means + array_data[i]
    return means / len(array_data)


def energy(data_array):
    data = np.zeros(len(data_array))
    for i in range(0, len(data_array) - 2):
        data[i] = math.sqrt(
            pow(data_array[i + 0], 2)
            + pow(data_array[i + 1], 2)
            + pow(data_array[i + 2], 2))
    return data


# обычное гамма
a = euclid(data_bytes3, data_bytes1)
# print(a, len(a))
print("Средний квадрат отклонения обычной гаммы", mean(a))
print("Максимальное отклонения обычной гаммы", max(a))
ossh1 = 20 * math.log(mean(energy(data_bytes3)) / mean(a), 10)
print("ОСШ обычной гаммы", ossh1)
possh1 = 20 * math.log(max(energy(data_bytes3)) / mean(a), 10)
print("ПОСШ обычной гаммы", possh1)

# интерполяционное гамма
b = euclid(data_bytes3, data_bytes2)
# print(b, len(b))
print("Средний квадрат отклонения интерполяционной гаммы", mean(b))
print("Максимальное отклонения интерполяционной гаммы", max(a))
ossh2 = 20 * math.log(mean(energy(data_bytes3)) / mean(b), 10)
print("ОСШ интерполяционной гаммы", ossh2)
possh2 = 20 * math.log(max(energy(data_bytes3)) / mean(b), 10)
print("ПОСШ интерполяционной гаммы", possh2)

sub_ossh = abs(ossh1 - ossh2)
sub_possh = abs(possh1 - possh2)
sub_max = abs(max(a) - max(b))
print("Разница ОСШ гамм", sub_ossh)
print("Разница ПОСШ гамм", sub_possh)
print("Разница максимумов", sub_possh)

print("\n")
print("LUT, чтение массива из файла")

# LUT = np.loadtxt(r"C:\Users\Agaperra\PycharmProjects\digital_technologies\LUT9.txt")
# for i in range(0, len(LUT)):
#     LUT[i] = float(LUT[i])
# print(LUT)
# LUT.resize((9, 9, 9, 3))

LUT = np.zeros((9, 9, 9, 3))
file = open(r"C:\Users\Agaperra\PycharmProjects\digital_technologies\LUT9.txt", 'r')
for i in range(9):
    for j in range(9):
        for k in range(9):
            for l in range(3):
                LUT[i, j, k, l] = float(file.readline())

file.close()
print(LUT)

