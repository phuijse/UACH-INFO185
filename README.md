# INFO185 Comunicaciones, UACH

Repositorio con material docente del curso INFO185 Comunicaciones, Ingeniería Civil Informática, Universidad Austral de Chile. Las clases están en formato [jupyter notebook](http://jupyter.org) y los códigos están en lenguaje Python 3. 


### Notas de uso
- Los notebooks están diseñados para proyectarse en resolución 1024x768 
- Se puede modificar el tamaño de fuente modificando el CSS en el primer bloque de cada notebook
- Para que los gráficos interactivos funcionen es necesario [habilitar los widgets para jupyter](http://ipywidgets.readthedocs.io/en/latest/user_install.html)
- Para renderear las ecuaciones con latex se necesita *mathjax*
- Para usar latex con matplotlib se necesita *latex-extra*
- Para el modo presentación se necesita instalar y habilitar la extensión [RISE](https://github.com/damianavila/RISE)
- Para ocultar el código en ciertos bloques se necesita instalar y habilitar la extensión [hide\_code](https://github.com/kirbs-/hide_code)

Para instalar los requisitos en archlinux:
```
sudo pacman -S python-numpy python-scipy python-matplotlib python-pillow mathjax texlive-latexextra jupyter-notebook 
```

2018 Pablo Huijse
