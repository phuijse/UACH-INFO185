## Universidad Austral de Chile

# INFO185 Comunicaciones 2019

### Responsables: Christian Lazo, Pablo Huijse, phuijse@inf.uach.cl


Repositorio con material docente del curso INFO185 Comunicaciones, Ingeniería Civil Informática, Universidad Austral de Chile. Las clases están en formato [jupyter notebook](http://jupyter.org) y los códigos están en lenguaje Python 3. 


***
## Contenidos

- **Unidad de aprendizaje 1** 
    - [Electricidad y circuitos eléctricos](unidad1.ipynb)
- **Unidad de aprendizaje 2** 
    - [Sistemas_de_comunicación](sistemas_de_comunicacion.ipynb)
    - [Procesamiento_señales_2D](unidad2_procesamiento_señales_2D.ipynb)
    - [Teoría de la Información](unidad2_compresion_teoria_de_la_informacion.ipynb)


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

2019 Pablo Huijse
