from ajenti.api import *
from ajenti.plugins import *


info = PluginInfo(
    title='WonderShaper',
    icon=None,
    dependencies=[
        PluginDependency('main'),
    ],
)


def init():
    import main
