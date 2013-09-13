import unittest
import sys

import mock

# Mock ajenti package
ajenti = mock.MagicMock()
sys.modules["ajenti"] = ajenti
sys.modules["ajenti.api"] = ajenti.api
sys.modules["ajenti.plugins"] = ajenti.plugins
del ajenti

from wondershaper.config import WonderShaperConfig


class WonderShaperConfigTest(unittest.TestCase):
    def setUp(self):
        self.content = """[wondershaper]
IFACE="eth0"
DSPEED="2048"
USPEED="512"
"""
        self.result = {
            "wondershaper": {
                "USPEED": "512",
                "IFACE": "eth0",
                "DSPEED": "2048"
            }
        }

    def test_config(self):
        config = WonderShaperConfig(content=self.content)
        config.load()
        a, b = self.result, config.tree.to_dict()
        self.assertEquals(a, b)


if __name__ == '__main__':
    unittest.main(verbosity=2)
