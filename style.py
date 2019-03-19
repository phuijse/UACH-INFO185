from matplotlib import rcParams
from ipywidgets import interact, FloatSlider, IntSlider, SelectionSlider, Layout
from traitlets.config.manager import BaseJSONConfigManager

# Default options for matplotlib plots
rcParams['figure.dpi'] = 80
rcParams['font.size'] = 16
rcParams['axes.grid'] = True
rcParams['lines.linewidth'] = 2.0
rcParams['legend.framealpha'] = 0.5
rcParams['legend.fontsize'] = 'medium'
rcParams['figure.titlesize'] = 'medium'
rcParams['figure.autolayout'] = True
#rcParams['animation.html'] = 'html5'
slider_layout = Layout(width='600px', height='20px')
slider_style = {'description_width': 'initial'}
from functools import partial
FloatSlider_nice = partial(FloatSlider, style=slider_style, layout=slider_layout, continuous_update=False)
IntSlider_nice = partial(IntSlider, style=slider_style, layout=slider_layout, continuous_update=False)
SelectionSlider_nice = partial(SelectionSlider, style=slider_style, layout=slider_layout, continuous_update=False)

# Optional: Set options for slide theme and transition
path = "/home/phuijse/.jupyter/nbconfig/"
try:
    cm = BaseJSONConfigManager(config_dir=path)
    cm.update('livereveal', {
        'theme': 'simple',
        'transition': 'fast',
        'start_slideshow_at': 'selected',
        'width': 1440,
        'height': 1080,
        'scroll': True,
        'center': True
    });
except:
    print("Cannot find path %s, rise configuration wasn't set" %(path))
