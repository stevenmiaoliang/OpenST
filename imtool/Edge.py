######################################
#Open ST
#Edge
#Author:steven.miaoliang@gmail.com
#Data:2016/5/26
######################################
from scipy import signal
from scipy import misc
import numpy as np
from imtool import *
from PIL import Image

def stEdge(src,type,scaleX=1,scaleY=1):
    scharr = np.array([[-3 - 3j, 0 - 10j, +3 - 3j],
                       [-10 + 0j, 0 + 0j, +10 + 0j],
                       [-3 + 3j, 0 + 10j, +3 + 3j]])
    sobel = np.array([[-1 - 1j, 0 - 2j, +1 - 1j],
                       [-2 + 0j, 0 + 0j, +2 + 0j],
                       [-1 + 1j, 0 + 2j, +1 + 1j]]) #Gx+jGy
    prewitt = np.array([[-1 - 1j, 0 - 1j, +1 - 1j],
                       [-1 + 0j, 0 + 0j, +1 + 0j],
                       [-1 + 1j, 0 + 2j, +1 + 1j]])
    if type == 'Sobel':
        grad = signal.convolve2d(src, sobel, boundary='symm', mode='same')
    elif type == 'Scharr':
        grad = signal.convolve2d(src, scharr, boundary='symm', mode='same')
    elif type == 'prewitt':
        grad = signal.convolve2d(src, scharr, boundary='symm', mode='same')
    else:
        raise  ValueError("Type: "+type + " Not support")
    return np.array(np.absolute(grad),dtype=np.uint8),np.angle(grad)

