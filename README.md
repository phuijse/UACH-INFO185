## Universidad Austral de Chile

# INFO236 Comunicaciones 2020

### Responsables: Christian Lazo, Pablo Huijse, phuijse@inf.uach.cl


Repositorio con material docente del curso INFO185 Comunicaciones, Ingeniería Civil Informática, Universidad Austral de Chile. Las clases están en formato [jupyter notebook](http://jupyter.org) y los códigos están en lenguaje Python 3. 


***
## Contenidos

- Sistemas digitales de comunicación 
    - [Introducción](unidad1/01_sistemas_de_comunicacion.ipynb)
    - [¿Qué es una señal?](unidad1/02_señales.ipynb)
    - [Análisis de señales](unidad1/03_análisis_de_señales.ipynb)


***
## Bibliografía


1. B.P. Lathi and Z. Ding, "Modern Digital and Analog Communication Systems", *Oxford University Press*, 2009
    
***
## Instrucciones de uso
- Los notebooks están diseñados para proyectarse en resolución 1024x768 
- Se puede modificar el tamaño de fuente modificando el CSS en el primer bloque de cada notebook
- Para que los gráficos interactivos funcionen es necesario [habilitar los widgets para jupyter](http://ipywidgets.readthedocs.io/en/latest/user_install.html)
- Para renderear las ecuaciones con latex se necesita *mathjax*
- Para usar latex con matplotlib se necesita *latex-extra*
- (Opcional) Para el modo presentación se necesita instalar y habilitar la extensión [RISE](https://github.com/damianavila/RISE)

Para instalar los requisitos en archlinux:
```
sudo pacman -S python-numpy python-scipy python-matplotlib python-pillow mathjax texlive-latexextra jupyter-notebook python-pydot python-networkx python-scikit-learn
```

2020 Pablo Huijse
