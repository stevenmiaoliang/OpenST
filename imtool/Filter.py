from numpy import *
from PIL import Image
from matplotlib.pyplot import *
from scipy.ndimage import filters

def denoise(im,U_init,tolerance = 0.05,tau = 0.125,tv_weight=100):
    m, n = im.shape
    U = U_init
    Px = im
    Py = im
    error = 1
    while (error > tolerance):
        Uold = U
        GradUx = roll(U, -1, axis=1) - U
        GradUy = roll(U, -1, axis=0) - U
        PxNew = Px + (tau / tv_weight) * GradUx
        PyNew = Py + (tau / tv_weight) * GradUy
        NormNew = maximum(1, sqrt(PxNew ** 2 + PyNew ** 2))
        Px = PxNew / NormNew
        Py = PyNew / NormNew
        RxPx = roll(Px, 1, axis=1)
        RyPy = roll(Py, 1, axis=0)
        DivP = (Px - RxPx) + (Py - RyPy)
        U = im + tv_weight * DivP
        error = linalg.norm(U - Uold) / sqrt(n * m);
    return U, im - U

if __name__ == "__main__":
    im = np.zeros((500,500))
    im[100:400,100:400] = 128
    im[200:300,200:300] = 255
    im = im + 10*np.random.standard_normal((500,500))
    U,T = denoise(im,im)
    G = filters.gaussian_filter(im,10)
    figure();
    gray();
    imshow(im);
    figure();gray();imshow(U);
    figure();gray();imshow(T);
    figure();gray();imshow(G);
    show();



