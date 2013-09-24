from ajenti.api import PluginInfo
from ajenti.plugins import PluginDependency


__version__ = "0.2.1"


info = PluginInfo(
    title='WonderShaper',
    icon=None,
    dependencies=[
        PluginDependency('main'),
    ],
)


def init():
    import main
