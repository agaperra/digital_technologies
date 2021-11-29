import numpy as np
from PIL import Image
import numpy as numpy
import math

image1 = Image.open("imageFirst.png")
w, h = image1.size
# print(w, h)
image_bytes1 = image1.tobytes()
data_bytes1 = bytearray(image_bytes1)

image2 = Image.open("imageSecond.png")
w1, h1 = image2.size
# print(w, h)
image_bytes2 = image2.tobytes()
data_bytes2 = bytearray(image_bytes2)

image3 = Image.open("паук.jpg")
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

# LUT = np.zeros((9, 9, 9, 3))
# file = open("LUT9.txt", 'r')
# for i in range(9):
#     for j in range(9):
#         for k in range(9):
#             for l in range(3):
#                 LUT[i, j, k, l] = float(file.readline())
#
# file.close()
# print(LUT)

def applyLookUpTable(R, G, B, LUT):
    """"apply LUT"""
    if R == 1:
        iR = 8
        iRa = 8
        print('!')
    if R < 1:
        iR = int(math.floor(R * 8))
        iRa = iR + 1
    if G == 1:
        iG = 8
        iGa = 8
        print('!!')
    if G < 1:
        iG = int(math.floor(G * 8))
        iGa = iG + 1
    if B == 1:
        iB = 8
        iBa = 8
        print('!!!')
    if B < 1:
        iB = int(math.floor(B * 8))
        iBa = iB + 1

    C000 = LUT[iR, iG, iB, 0]
    C001 = LUT[iR, iG, iBa, 0]
    C010 = LUT[iR, iGa, iB, 0]
    C100 = LUT[iRa, iG, iB, 0]
    C011 = LUT[iR, iGa, iBa, 0]
    C101 = LUT[iRa, iG, iBa, 0]
    C110 = LUT[iRa, iGa, iB, 0]
    C111 = LUT[iRa, iGa, iBa, 0]

    r = C000 * (float(iRa) / 8 - R) * (float(iGa) / 8 - G) * (float(iBa) / 8 - B) + C100 * (R - float(iR) / 8) * (
            float(iGa) / 8 - G) * (float(iBa) / 8 - B) + C101 * (R - float(iR) / 8) * (float(iGa) / 8 - G) * (
                B - float(iB) / 8) + C110 * (R - float(iR) / 8) * (G - float(iG) / 8) * (
                float(iBa) / 8 - B) + C111 * (R - float(iR) / 8) * (G - float(iG) / 8) * (
                B - float(iB) / 8) + C010 * (float(iRa) / 8 - R) * (G - float(iG) / 8) * (
                float(iBa) / 8 - B) + C001 * (float(iRa) / 8 - R) * (float(iGa) / 8 - G) * (
                B - float(iB) / 8) + C011 * (float(iRa) / 8 - R) * (G - float(iG) / 8) * (B - float(iB) / 8)
    r = r * 8 * 8 * 8

    C000 = LUT[iR, iG, iB, 1]
    C001 = LUT[iR, iG, iBa, 1]
    C010 = LUT[iR, iGa, iB, 1]
    C100 = LUT[iRa, iG, iB, 1]
    C011 = LUT[iR, iGa, iBa, 1]
    C101 = LUT[iRa, iG, iBa, 1]
    C110 = LUT[iRa, iGa, iB, 1]
    C111 = LUT[iRa, iGa, iBa, 1]

    g = C000 * (float(iRa) / 8 - R) * (float(iGa) / 8 - G) * (float(iBa) / 8 - B) + C100 * (R - float(iR) / 8) * (
            float(iGa) / 8 - G) * (float(iBa) / 8 - B) + C101 * (R - float(iR) / 8) * (float(iGa) / 8 - G) * (
                B - float(iB) / 8) + C110 * (R - float(iR) / 8) * (G - float(iG) / 8) * (
                float(iBa) / 8 - B) + C111 * (R - float(iR) / 8) * (G - float(iG) / 8) * (
                B - float(iB) / 8) + C010 * (float(iRa) / 8 - R) * (G - float(iG) / 8) * (
                float(iBa) / 8 - B) + C001 * (float(iRa) / 8 - R) * (float(iGa) / 8 - G) * (
                B - float(iB) / 8) + C011 * (float(iRa) / 8 - R) * (G - float(iG) / 8) * (B - float(iB) / 8)
    g = g * 8 * 8 * 8

    C000 = LUT[iR, iG, iB, 2]
    C001 = LUT[iR, iG, iBa, 2]
    C010 = LUT[iR, iGa, iB, 2]
    C100 = LUT[iRa, iG, iB, 2]
    C011 = LUT[iR, iGa, iBa, 2]
    C101 = LUT[iRa, iG, iBa, 2]
    C110 = LUT[iRa, iGa, iB, 2]
    C111 = LUT[iRa, iGa, iBa, 2]

    b = C000 * (float(iRa) / 8 - R) * (float(iGa) / 8 - G) * (float(iBa) / 8 - B) + C100 * (R - float(iR) / 8) * (
            float(iGa) / 8 - G) * (float(iBa) / 8 - B) + C101 * (R - float(iR) / 8) * (float(iGa) / 8 - G) * (
                B - float(iB) / 8) + C110 * (R - float(iR) / 8) * (G - float(iG) / 8) * (
                float(iBa) / 8 - B) + C111 * (R - float(iR) / 8) * (G - float(iG) / 8) * (
                B - float(iB) / 8) + C010 * (float(iRa) / 8 - R) * (G - float(iG) / 8) * (
                float(iBa) / 8 - B) + C001 * (float(iRa) / 8 - R) * (float(iGa) / 8 - G) * (
                B - float(iB) / 8) + C011 * (float(iRa) / 8 - R) * (G - float(iG) / 8) * (B - float(iB) / 8)
    b = b * 8 * 8 * 8

    return r, g, b


filename = "паук.jpg"
image = Image.open(filename)
width, height = image.size
print(width)
print(height)
im = image.load()
arr = numpy.asarray(image)
LUT = numpy.zeros((9, 9, 9, 3))
f = open('LUT9.txt', 'r')
for i in range(0, 9):
    for j in range(0, 9):
        for k in range(0, 9):
            for l in range(0, 3):
                LUT[i, j, k, l] = float(f.readline())
for i in range(0, height):
    for j in range(0, width):
        [r, g, b] = applyLookUpTable(float(arr[i, j, 0]) / 255, float(arr[i, j, 1]) / 255,
                                     float(arr[i, j, 2]) / 255,
                                     LUT)

        arr[i, j, 0] = int(255 * r)
        arr[i, j, 1] = int(255 * g)
        arr[i, j, 2] = int(255 * b)
image_out = Image.frombuffer('RGB', (width, height), arr)
image_out.save('result.png', 'png')
