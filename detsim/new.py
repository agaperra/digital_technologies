from PIL import Image
import numpy as numpy
import scipy
from scipy.fftpack import idctn, dctn
from math import sqrt, log10
from statistics import mean

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

N = 50
for i in range(N, (width)):
    for j in range(N, (height)):
        dct_im[i, j] = float(0)

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
        pic_out[i, j] = pix
        im_out[i, j] = bytes([int(pix)])

avgDists = []
avgEners = []
for i in range(0, width):
    for j in range(0, height):
        newV = float(pic_out[i, 3])
        oldV = float(pic_in[i, 3])
        dif = abs(oldV - newV)
        avgDists.append(dif)
        avgEners.append(newV)
        avgEners.append(oldV)
maxEner = 255
avgDist = mean(avgDists)

PSNR = 20 * log10(maxEner / avgDist)
print(avgDist, PSNR)

image_out = Image.frombytes('L', (width, height), im_out)
savepath = 'lab_dct_result.png'
image_out.save(savepath, 'png')
