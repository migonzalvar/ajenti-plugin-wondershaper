import subprocess

from ajenti.api import plugin
from ajenti.plugins.main.api import SectionPlugin
from ajenti.ui import on
from ajenti.ui.binder import Binder

from .config import WonderShaperConfig


@plugin
class WonderShaper(SectionPlugin):
    # default config could be overwitten on main config.json
    default_classconfig = {'path': '/etc/conf.d/wondershaper.conf'}

    def init(self):
        self.title = 'WonderShaper'
        # Icons set: http://fortawesome.github.io/Font-Awesome/icons/
        self.icon = 'download-alt'
        self.category = 'DXS'

        self.append(self.ui.inflate('wondershaper:main'))

        path = self.classconfig['path']
        self.config = WonderShaperConfig(path=path)
        self.binder = Binder(None, self)

    def on_page_load(self):
        self.config.load()
        data = self.config.tree.wondershaper
        self.binder.reset(data).autodiscover().populate()

    @on('save', 'click')
    def on_save(self):
        self.binder.update()
        self.config.save()
        self.context.notify('info', 'Saved conf')
        ret = subprocess.call(['systemctl', 'restart', 'wondershaper.service'])
        if ret == 0:
            self.context.notify('info', 'Reload service')
        else:
            self.context.notify('error', 'Error on reload service')
