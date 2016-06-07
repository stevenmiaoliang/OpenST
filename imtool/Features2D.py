######################################
#Open ST
#Corner
#Author:steven.miaoliang@gmail.com
#Data:2016/5/26
######################################
import numpy as np
#from skimage import data, io, filters
from scipy.ndimage import  filters
def corner(im,opts):
    type = opts['type']
    corner = np.array(im)
    if type == 'Gradient':
        kernel = np.array([[1,0,-1],[0,0,0],[-1,0,1]])
        corner = filters.convolve(im,kernel)
    elif type == 'Harris':
        subType = opts['subType']
        if subType == 'Gaussian':
            sigma = opts['sigma']
            imx = np.zeros(im.shape)
            filters.gaussian_filter(im,(sigma,sigma),(0,1),imx)
            imy = np.zeros(im.shape)
            filters.gaussian_filter(im,(sigma,sigma),(1,0),imy)
            Wxx = filters.gaussian_filter(imx*imx,sigma)
            Wxy = filters.gaussian_filter(imx*imy,sigma)
            Wyy = filters.gaussian_filter(imy*imy,sigma)
            Wdet = Wxx*Wyy-Wxy*2
            Wtr = Wxx+Wyy
            corner =  Wdet/Wtr
        elif subType == 'Sobel':
            sigma = opts['sigma']
            imx = np.zeros(im.shape)
            imy = np.zeros(im.shape)
            filters.sobel(im,-1,output=imx)
            filters.sobel(im,0,output=imy)
            Wxx = filters.gaussian_filter(imx * imx, sigma)
            Wxy = filters.gaussian_filter(imx * imy, sigma)
            Wyy = filters.gaussian_filter(imy * imy, sigma)
            Wdet = Wxx*Wyy - Wxy*2
            Wtr = Wxx+Wyy
            corner = Wdet/Wtr
        return corner

def get_corner_points(im,min_dist=10,threshold = 0.1):
    corner_max = im.max()*threshold
    im_t = (im>threshold)*1
    coords = np.array(im_t.nonzero()).T
    candidate_values = [im[c[0],c[1]] for c in coords]
    index = np.argsort(candidate_values)
    allowed_locations = np.zeros(im.shape)
    allowed_locations[min_dist:-min_dist,min_dist:-min_dist] = 1
    filter_coord = [];
    for i in index:
        if allowed_locations[coords[i,0],coords[i,1]] == 1:
            filter_coord.append(coords[i])
            allowed_locations[(coords[i,0]-min_dist):(coords[i,0]+min_dist),(coords[i,1]-min_dist):(coords[i,1]+min_dist)] = 0
    return  filter_coord;