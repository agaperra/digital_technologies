from PIL import Image
import numpy as numpy

# загрузка
image = Image.open("2g.bmp").convert('L')
width, height = image.size
im = image.load()

# произволная h
M = 1
h = numpy.zeros((3, 3))
h[0, 0] = 0
h[0, 1] = -0.3
h[0, 2] = 0
h[1, 0] = -0.5
h[1, 1] = 1
h[1, 2] = -0.5
h[2, 0] = 0
h[2, 1] = 0.3
h[2, 2] = 0


pic_out = numpy.zeros((width, height))
im_out = numpy.zeros((width, height), 'bytes')

for i in range(0, width):
    for j in range(0, height):
        pix = 0
        for ii in range(-M, M + 1):
            for jj in range(-M, M + 1):
                if ((i + ii) > (-1)) & ((j + jj) > (-1)) & ((i + ii) < width) & ((j + jj) < height):
                    index_i = i + ii
                    index_j = j + jj
                if (i + ii) < 0:
                    index_i = i - ii
                if (j + jj) < 0:
                    index_j = j - jj
                if (i + ii) > (width - 1):
                    index_i = i - ii
                if (j + jj) > (height - 1):
                    index_j = j - jj
                pix = pix + float(im[index_i, index_j]) * h[ii + 1, jj + 1]
        pic_out[i, j] = pix

po_max = 0
po_min = 0

for i in range(0, width):
    for j in range(0, height):
        if pic_out[i, j] > po_max:
            po_max = pic_out[i, j]
        if pic_out[i, j] < po_min:
            po_min = pic_out[i, j]

for i in range(0, width):
    for j in range(0, height):
        pix = pic_out[j, i]
        pix = 255 * (pix - po_min) / (po_max - po_min)
        im_out[i, j] = bytes([int(pix)])

image_out = Image.frombytes('L', (width, height), im_out)
image_out.save('result3.png', 'png')
