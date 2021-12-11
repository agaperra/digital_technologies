from PIL import Image
import numpy as numpy

# загрузка
image = Image.open("2g.bmp").convert('L')
width, height = image.size
im = image.load()
print(width, height)
w = width // 2
h = height // 2
print(w, h)

pic_out = numpy.zeros((w, h))
im_out = numpy.zeros((w, h), 'bytes')
for i in range(0, width):
    for j in range(0, height):
        pic_out[i // 2, j // 2] = im[i, j]
        pix = pic_out[i // 2, j // 2]
        im_out[i // 2, j // 2] = bytes([int(pix)])

image_out = Image.frombytes('L', (w, h), im_out)
image_out.save('result3.png', 'png')
print(pic_out)

pic_out1 = numpy.zeros((w, h))
im_out1 = numpy.zeros((w, h), 'bytes')
for i in range(0, width):
    if i % 2 == 0:
        print(i, i // 2)
    else:
        print(i, (i - 1) // 2)
    for j in range(0, height):
        if i % 2 == 0:
            pic_out1[i // 2, j // 2] = im[i, j]
            pix = pic_out1[i // 2, j // 2]
            im_out1[i // 2, j // 2] = bytes([int(pix)])
        else:
            pic_out1[(i - 1) // 2, (j - 1) // 2] = im[i, j]
            pix = pic_out1[(i - 1) // 2, (j - 1) // 2]
            im_out1[(i - 1) // 2, (j - 1) // 2] = bytes([int(pix)])

image_out1 = Image.frombytes('L', (w, h), im_out1)
image_out1.save('result4.png', 'png')
print(pic_out1)
