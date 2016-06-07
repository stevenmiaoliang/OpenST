import numpy as np
from skimage import data, io, filters

def stFilter_ROF(im,U_init,tolerance = 0.05,tau = 0.125,tv_weight=100):
    m, n = im.shape
    U = U_init
    Px = im
    Py = im
    error = 1
    while (error > tolerance):
        Uold = U
        GradUx = np.roll(U, -1, axis=1) - U
        GradUy = np.roll(U, -1, axis=0) - U
        PxNew = Px + (tau / tv_weight) * GradUx
        PyNew = Py + (tau / tv_weight) * GradUy
        NormNew = np.maximum(1, np.sqrt(PxNew ** 2 + PyNew ** 2))
        Px = PxNew / NormNew
        Py = PyNew / NormNew
        RxPx = np.roll(Px, 1, axis=1)
        RyPy = np.roll(Py, 1, axis=0)
        DivP = (Px - RxPx) + (Py - RyPy)
        U = im + tv_weight * DivP
        error = np.linalg.norm(U - Uold) / np.sqrt(n * m);
    return U, im - U

def stFilter_Mean(im,size=3):
    kernel = np.ones((size,size))
    im = np.asarray(im,dtype=np.float)
    result = filters.convolve(im, kernel)
    return result

def stFilter_Bilateral(im,sigmad,sigmar,size):
    im = im/255.0
    nx, ny = (size*2+1, size*2+1)
    x = np.linspace(-size, size, nx)
    y = np.linspace(-size, size, ny)
    xv, yv = np.meshgrid(x, y)
    G = np.exp((xv**2+yv**2)/(2*sigmad*sigmad))
    rows,cols = im.shape;
    B = np.ones((rows,cols))
    I = np.zeros((size*2+1,size*2+1),dtype=float)
    for i in range(size,rows-size):
        for j in range(size,cols-size):
            I[:,:] = im[i-size:i+size+1,j-size:j+size+1];
            #Compute Gaussian intensity weights.
            M = (I - im[i,j]);
            H = np.exp(-M**2 / (2 * sigmar*sigmar));
            F = (H * G);
            B[i,j] = np.sum(np.sum(F*I)) / np.sum(np.sum(F));
    return  B*255.0
















