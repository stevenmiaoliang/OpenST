from numpy import *
from PIL import Image
import matplotlib.pyplot as plt
from scipy.ndimage import filters
from imtool import *
from skimage import data, io, filters


if __name__ == "__main__":
    im = np.zeros((500,500))
    im[100:400,100:400] = 128
    im[200:300,200:300] = 255
#    im = np.array(im + 10*np.random.standard_normal((500,500)),dtype=uint8)
#    im,imT = ROF(im,im)
#    image = data.moon() # or any NumPy array!
 #   edges = filters.scharr(image)
 #   io.imshow(edges)
 #   io.show()
#    im = open('lenaT.bmp')
#    sobelIm,angleIm = edge(im,'Sobel')
    opts = {'type':'Harris','subType':'Gaussian','sigma':0.6}
    bIm = corner(im,opts)
    filtered_coords = get_corner_points(bIm)
    plt.imshow(bIm)
    plt.plot([p[1] for p in filtered_coords],[p[0] for p in filtered_coords],'*')
    plt.show()
 #   io.imshow(255*(bIm>1))
 #   io.show()
    pt1 = Point(0,0)
    pt2 = Point(10,10)
    rectA = Rect(Point(0,0),Point(10,10))
    rectB = Rect(Point(1,1),Point(21,21));
    rectC = rectA.union(rectB)

 #   binaryIm = 1*(sobelIm>100)
 #   labels,nbr_objects = findContours(binaryIm)
#    U,T = ROF(im,im)
 #   G = filters.gaussian_filter(im,10)
#    show(binaryIm);