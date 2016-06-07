######################################
#Open ST
#Region
#Author:steven.miaoliang@gmail.com
#Data:2016/5/26
######################################

from scipy import signal
from scipy import misc
from scipy.ndimage import measurements
from scipy.ndimage import morphology

import numpy as np
from imtool import *
from PIL import Image

def findContours(src):
    labels,nbr_objects = measurements.label(src)
    return  labels,nbr_objects

