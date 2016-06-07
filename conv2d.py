
from scipy import signal
from scipy import misc
import numpy as np
from imtool import *
from PIL import Image

if __name__ == "__main__":
    pil_im = Image.open('D:\lena.bmp','r')
    face = np.array(pil_im)
    scharr = np.array([[ -3-3j, 0-10j,  +3 -3j],
                    [-10+0j, 0+ 0j, +10 +0j],
                   [ -3+3j, 0+10j,  +3 +3j]]) # Gx + j*Gy
    grad = signal.convolve2d(face, scharr, boundary='symm', mode='same')
    import matplotlib.pyplot as plt
    fig, (ax_orig, ax_mag, ax_ang) = plt.subplots(1, 3)
    ax_orig.imshow(face, cmap='gray')
    ax_orig.set_title('Original')
    ax_orig.set_axis_off()
    ax_mag.imshow(np.absolute(grad), cmap='gray')
    ax_mag.set_title('Gradient magnitude')
    ax_mag.set_axis_off()
    ax_ang.imshow(np.angle(grad), cmap='hsv') # hsv is cyclic, like angles
    ax_ang.set_title('Gradient orientation')
    ax_ang.set_axis_off()
    fig.show()
    print  '12';
