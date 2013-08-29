from ajenti.api import *
from ajenti.plugins import *


__version__ = "0.1.0"


info = PluginInfo(
    title='WonderShaper',
    icon=None,
    dependencies=[
        PluginDependency('main'),
    ],
)


def init():
    import main
