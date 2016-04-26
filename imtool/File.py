import numpy as np
from PIL import Image
from matplotlib.pyplot import *
from scipy.ndimage import filters
import cv2

def open(fileName,mode):
    pil_im = Image.open(fileName, mode)
    im = np.array(pil_im)
    return im;

def  write(array,fileName):
