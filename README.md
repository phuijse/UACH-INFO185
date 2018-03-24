# INFO185 Comunicaciones, UACH

Repositorio con material docente del curso INFO185 Comunicaciones, Ingeniería Civil Informática, Universidad Austral de Chile. Las clases están en formato jupyter notebook [1] y los códigos están en lenguaje Python 3. 


### Notas
- Los notebooks están diseñados para proyectarse en resolución 1024x768. Se puede modificar el tamaño de la fuente en el primer bloque de cada notebook
- Para que los gráficos interactivos funcionen es necesario habilitar los widgets para jupyter [2]
- Para renderear las ecuaciones con latex se necesita *mathjax*
- Para usar latex con matplotlib se necesita *latex-extra*
- Para el modo presentación se necesita instalar y habilitar la extensión *RISE* [3]
- Para ocultar el código en ciertos bloques se necesita instalar y habilitar la extensión hide\_code [4]

### Requisitos: 
- jupyter 
- numpy
- scipy
- matplotlib
- pillow (para abrir archivos jpeg con matplotlib)

En archlinux:
```
sudo pacman -S python-numpy python-scipy python-matplotlib python-pillow mathjax texlive-latexextra jupyter-notebook 
```

[1]: http://jupyter.org
[2]: http://ipywidgets.readthedocs.io/en/latest/user_install.html
[3]: https://github.com/damianavila/RISE
[4]: https://github.com/kirbs-/hide_code



2018 Pablo Huijse
