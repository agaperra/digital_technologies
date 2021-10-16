import random

from PIL import Image, ImageDraw

filename = r"C:\Users\Agaperra\PycharmProjects\digital_technologies\паук.png"
image = Image.open(filename)
w, h = image.size
im_load = image.load()
draw = ImageDraw.Draw(image)
y = random.uniform(0.5, 1.5)
for i in range(w):
    for j in range(h):
        r = im_load[i, j][0]
        R = r ** y
        g = im_load[i, j][1]
        G = g ** y
        b = im_load[i, j][2]
        B = b ** y
        image.putpixel((i, j), (int(R), int(G), int(B)))
im = image.tobytes()
im_out = Image.frombytes(image.mode, (w, h), im)
im_out.save(r"C:\Users\Agaperra\PycharmProjects\digital_technologies\other.png", 'png')
