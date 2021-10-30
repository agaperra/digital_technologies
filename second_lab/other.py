from PIL import Image
import numpy as np

image = Image.open(r"C:\Users\Agaperra\PycharmProjects\digital_technologies\паук.jpg")
w, h = image.size

imgbytes = image.tobytes()
databytes = bytearray(imgbytes)
data = np.zeros(w * h * 3)
gamma = 1 / 2.0

for y in range(0, h * 3):
    for x in range(0, w, 3):
        data[y * w + x + 0] = databytes[y * w + x + 0] / 255.0
        if (y * w + x + 1) != len(databytes) & (y * w + x + 2) != len(databytes):
            data[y * w + x + 1] = databytes[y * w + x + 1] / 255.0
            data[y * w + x + 2] = databytes[y * w + x + 2] / 255.0

for y in range(0, h * 3):
    for x in range(0, w, 3):
        data[y * w + x] = pow(data[y * w + x], gamma)
        if (y * w + x + 1) != len(data) & (y * w + x + 2) != len(data):
            data[y * w + x + 1] = pow(data[y * w + x + 1], gamma)
            data[y * w + x + 2] = pow(data[y * w + x + 2], gamma)

for y in range(0, h * 3):
    for x in range(0, w, 3):
        databytes[y * w + x + 0] = int(data[y * w + x + 0] * 255.0)
        if (y * w + x + 1) != len(data) & (y * w + x + 2) != len(data):
            databytes[y * w + x + 1] = int(data[y * w + x + 1] * 255.0)
            databytes[y * w + x + 2] = int(data[y * w + x + 2] * 255.0)

result = bytes(databytes)

imout = Image.frombytes('RGB', (w, h), result)
imout.save(r"C:\Users\Agaperra\PycharmProjects\digital_technologies\imageFirst.png", 'png')
