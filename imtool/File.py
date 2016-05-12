import numpy as np
from PIL import Image
from matplotlib.pyplot import *

def stOpen(filePath,mode):
    try:
        pil_im = Image.open(filePath, mode)
    except IOError:
        raise ValueError("File: "+filePath + " Open Error ")
    im = np.array(pil_im)
    return im

#write
def stWrite(array,filePath):
    pil_im = Image.fromarray(array)
    try:
        pil_im.save(filePath)
    except IOError:
        raise ValueError("File: " + filePath + " Save Error ")

def stShow(array,color = False):
    figure();
    if color == False:
        gray();
    imshow(array);
    show();





