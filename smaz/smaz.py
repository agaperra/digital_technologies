from PIL import Image
import numpy as numpy

filename = "2g.bmp"
image = Image.open(filename).convert("L")
width, height = image.size
im = image.load()

M = 1
N = 2
hA = numpy.zeros((3, 3))
hA[1, 1] = 1
hA[0, 1] = 0
hA[2, 1] = 0
hA[1, 0] = 0
hA[1, 2] = 0
hA[0, 0] = 0
hA[2, 0] = 0
hA[0, 2] = 0
hA[2, 2] = 0

hB = numpy.zeros((2, 2))
hB[0, 0] = 0
hB[0, 1] = 0.3
hB[1, 0] = 0.3
hB[1, 1] = 0.3

im_out = numpy.zeros((width, height), 'bytes')


def motionBlur(i):
    if i == 1:
        iRange = range(0, width)
        jRange = range(0, height)
    elif i == 2:
        iRange = reversed(range(0, width))
        jRange = range(0, height)
    elif i == 3:
        iRange = range(0, width)
        jRange = reversed(range(0, height))
    elif i == 4:
        iRange = reversed(range(0, width))
        jRange = reversed(range(0, height))

    pic_out = numpy.zeros((width, height))
    for i in iRange:
        for j in jRange:
            pix = 0
            for i1 in range(-M, M + 1):
                for j1 in range(-M, M + 1):
                    if ((i + i1) > (-1)) & ((i + i1) < width):
                        index_i = i + i1
                    if (i + i1) < 0:
                        index_i = i - i1
                    if (i + i1) > width - 1:
                        index_i = i - i1

                    if ((j + j1) > (-1)) & ((j + j1) < height):
                        index_j = j + j1
                    if (j + j1) < 0:
                        index_j = j - j1
                    if (j + j1) > (height - 1):
                        index_j = j - j1

                    pix = pix + float(im[index_i, index_j]) * hA[i1 + M, j1 + M]
            pic_out[i, j] = pix
            pix = pic_out[i, j]
            for i1 in range(0, N):
                for j1 in range(0, N):
                    if ((i - i1) > (-1)) & ((j - j1) > (-1)):
                        pix = pix + pic_out[i - i1, j - j1] * hB[i1, j1]
            pic_out[i, j] = pix
    return pic_out


pic_out1 = motionBlur(1)
pic_out2 = motionBlur(2)
pic_out3 = motionBlur(3)
pic_out4 = motionBlur(4)

pic_out = numpy.zeros((width, height))
for i in range(0, width):
    for j in range(0, height):
        pic_out[i, j] = round((pic_out1[i, j] + pic_out2[i, j] + pic_out3[i, j] + pic_out4[i, j]) / 4)

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
image_out.save('result.png', 'png')
