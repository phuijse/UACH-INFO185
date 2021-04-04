# # Tutorial de OpenCV
# 
# [OpenCV](https://opencv.org/about/) (Open Source Computer Vision Library) es una librería enfocada en visión computacional y machine learning con más de 2500 algoritmos optimizados, una gran comunidad de usuarios y amplia adopción por parte de empresas.
# 
# La librería está escrita en C++ pero tiene interfaces para Python, Java y MATLAB. Adicionalmente tiene algunos algoritmos implementados en GPU. OpenCV fue diseñada pensando en aplicaciones de visión computacional que trabajan en tiempo real. 
# 
# En esta sesión haremos un tutorial breve de la interfaz de Python de OpenCV
# 
# Se recomienda crear un ambiente de conda con opencv y gtk

# conda create -n opencv
# conda activate opencv
# conda install -c conda-forge opencv=4.2.0 numpy gtk2 ipython six pillow matplotlib


import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
print(cv.__version__)

# Lectura de datos
img = cv.imread('casa_central.jpg')
print(type(img), img.shape) # img es un arreglo de numpy

# Mostrar una imagen con opencv
def mostrar_y_esperar(img, title='Titulo'):
    cv.imshow(title, img)
    cv.waitKey(0) # Se queda esperando una tecla
    cv.destroyWindow(title)
    
mostrar_y_esperar(img)

# También se puede mostrar com matplotlib
# Por defecto opencv usa el estándar BGR (blue first) 
plt.imshow(img)
# plt.show()

# Función esencial: cvtColor()
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
plt.imshow(img_rgb)

# Imagen en escala de grises
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
plt.imshow(img_gray, cmap=plt.cm.Greys_r)

# Separando los canales de una imagen
img_ycbcr = cv.cvtColor(img, cv.COLOR_BGR2YCrCb)
Y, Cr, Cb = cv.split(img_ycbcr)
fig, ax = plt.subplots(3,1, sharex=True, sharey=True, figsize=(6, 9))
ax[0].imshow(Y, cmap=plt.cm.Greys_r)
ax[1].imshow(Cr, cmap=plt.cm.Greys_r)
ax[2].imshow(Cb, cmap=plt.cm.Greys_r)

# Más sobre colorspaces: https://docs.opencv.org/master/df/d9d/tutorial_py_colorspaces.html

# Función esencial: resize
img_resized = cv.resize(img_gray, (100,100), interpolation=cv.INTER_LINEAR)
plt.imshow(img_resized, cmap=plt.cm.Greys_r)
# Más sobre transformaciones afines: https://docs.opencv.org/master/da/d6e/tutorial_py_geometric_transformations.html


# Filtrado Gaussiano
# Las dimensiones del filtro deben ser impar, 
sigma = 0
img_blur = cv.GaussianBlur(img_gray, (21,21), sigma, cv.BORDER_DEFAULT)
plt.imshow(img_blur, cmap=plt.cm.Greys_r)
# Más sobre suavizado: https://docs.opencv.org/master/d4/d13/tutorial_py_filtering.html

# Filtro Canny
# Requiere dos umbrales para definir lo que es parte de un borde
img_edge = cv.Canny(img_gray, 150, 200)
plt.imshow(img_edge, cmap=plt.cm.Greys_r)
# Más sobre filtro canny: https://docs.opencv.org/master/da/d22/tutorial_py_canny.html

# Histogramas
hist_img = cv.calcHist([img_gray], [0], None, [256], [0, 256])
plt.plot(hist_img)
plt.xlabel('Pixel')
# Más sobre histogramas: https://docs.opencv.org/master/de/db2/tutorial_py_table_of_contents_histograms.html


# Binarización
# El primer argumento es el umbral, si pix > umbral, entonces pix=value
_, img_binary = cv.threshold(img_gray, 200, 255, cv.THRESH_BINARY)
plt.imshow(img_binary, cmap=plt.cm.Greys_r)
# También se puede hacer binarización local (adaptiva)
img_binary = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 0)
plt.imshow(img_binary, cmap=plt.cm.Greys_r)
# Más sobre binarización: https://docs.opencv.org/master/d7/d4d/tutorial_py_thresholding.html

# Transformada de Fourier
# cv.dft requiere convertir la imagen a flotante
# Retorna una matriz con dos canales: real e imaginario
# La frecuencia cero está en la esquina superior izquierda
img_dft = cv.dft(img_gray.astype('float32'), flags=cv.DFT_COMPLEX_OUTPUT)
mag_dft, phase_dft = cv.cartToPolar(img_dft[:, :, 0], img_dft[:, :, 1])
fig, ax = plt.subplots(2, 1, sharey=True, figsize=(8, 8))
ax[0].imshow(np.log(mag_dft+1), cmap=plt.cm.Spectral_r)
ax[1].imshow(phase_dft, cmap=plt.cm.Spectral_r)
# Comparación de desempeño versus fftpack
from scipy import fftpack
%timeit -n10 -r10 fftpack.fft2(img_gray.astype('float32'))
%timeit -n10 -r10 cv.dft(img_gray.astype('float32'), flags=cv.DFT_COMPLEX_OUTPUT)
np.allclose(np.abs(fftpack.fft2(img_gray.astype('float32'))), mag_dft, rtol=1e-2)

# Transformada Coseno

img_dct = cv.dct(img_gray.astype('float32'))
fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(np.log(img_dct+1), cmap=plt.cm.Spectral_r)

