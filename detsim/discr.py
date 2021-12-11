import sys
from PIL import Image
import numpy as numpy
import scipy
from scipy.fftpack import idctn, dctn

filename = "2g.bmp"
image = Image.open(filename).convert('L')
width, height = image.size
print(width)
print(height)
im = image.load()

pic_out = numpy.zeros((width, height))
pic_in = numpy.zeros((width, height))
im_out = numpy.zeros((width, height), 'bytes')
for i in range(0, width):
    for j in range(0, height):
        pic_in[i, j] = float(im[i, j])
dct_im = dctn(pic_in)

pic_out = idctn(dct_im)

POMAX = 0
POMIN = 0
for i in range(0, width):
    for j in range(0, height):
        if pic_out[i, j] > POMAX:
            POMAX = pic_out[i, j]
        if pic_out[i, j] < POMIN:
            POMIN = pic_out[i, j]

for i in range(0, width):
    for j in range(0, height):
        pix = pic_out[i, j]
        pix = 255 * (pix - POMIN) / (POMAX - POMIN)
        im_out[i, j] = bytes([int(pix)])
image_out = Image.frombytes('L', (width, height), im_out)
savepath = 'lab_dct_result.png'
image_out.save(savepath, 'png')
