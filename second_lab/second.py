# интерполяция
import random
from PIL import Image, ImageDraw
import sys

#
# gamma05 = []
# for i in range(0, 255, 16):
#     gamma05.append(int(i ** 0.5))
#
# print(gamma05)
#
# gamma06 = []
# for i in range(0, 255, 16):
#     gamma06.append(int(i ** 0.6))
#
# print(gamma06)
#
# gamma07 = []
# for i in range(0, 255, 16):
#     gamma07.append(int(i ** 0.7))
#
# print(gamma07)
#
# gamma08 = []
# for i in range(0, 255, 16):
#     gamma08.append(int(i ** 0.8))
#
# print(gamma08)
#
# gamma09 = []
# for i in range(0, 255, 16):
#     gamma09.append(int(i ** 0.9))
#
# print(gamma09)
#
# gamma10 = []
# for i in range(0, 255, 16):
#     gamma10.append(int(i ** 1.0))
#
# print(gamma10)
#
# gamma11 = []
# for i in range(0, 255, 16):
#     gamma11.append(int(i ** 1.1))
#
# print(gamma11)
#
# gamma12 = []
# for i in range(0, 255, 16):
#     gamma12.append(int(i ** 1.2))
#
# print(gamma12)
#
# gamma13 = []
# for i in range(0, 255, 16):
#     gamma13.append(int(i ** 1.3))
#
# print(gamma13)
#
# gamma14 = []
# for i in range(0, 255, 16):
#     gamma14.append(int(i ** 1.4))
#
# print(gamma14)
#
# gamma15 = []
# for i in range(0, 255, 16):
#     gamma15.append(int(i ** 1.5))
#
# print(gamma15)


# gamma05 = [0, 4, 5, 6, 8, 8, 9, 10, 11, 12, 12, 13, 13, 14, 14, 15]
# gamma06 = [0, 5, 7, 10, 12, 13, 15, 16, 18, 19, 21, 22, 23, 24, 25, 26]
# gamma07 = [0, 6, 11, 15, 18, 21, 24, 27, 29, 32, 34, 37, 39, 41, 44, 46]
# gamma08 = [0, 9, 16, 22, 27, 33, 38, 43, 48, 53, 57, 62, 67, 71, 75, 80]
# gamma09 = [0, 12, 22, 32, 42, 51, 60, 69, 78, 87, 96, 104, 113, 121, 130, 138]
gamma10 = [0, 16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240]
# gamma11 = [0, 21, 45, 70, 97, 123, 151, 179, 207, 236, 265, 295, 324, 354, 384, 415]
# gamma12 = [0, 27, 63, 104, 147, 192, 239, 287, 337, 389, 441, 495, 549, 604, 661, 718]
# gamma13 = [0, 36, 90, 153, 222, 297, 377, 461, 548, 639, 733, 830, 929, 1031, 1135, 1242]
# gamma14 = [0, 48, 127, 225, 337, 461, 595, 739, 891, 1051, 1218, 1392, 1572, 1759, 1951, 2149]
# gamma15 = [0, 64, 181, 332, 512, 715, 940, 1185, 1448, 1728, 2023, 2334, 2660, 2999, 3352, 3718]

filename = r"C:\Users\Agaperra\PycharmProjects\digital_technologies\паук.png"
image = Image.open(filename)
w, h = image.size
im_load = image.load()
