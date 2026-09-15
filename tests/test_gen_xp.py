import os
import unittest

from globals import BASE_DIR
from libs.processors import xp
from libs.services import i18n


class TestGenXp(unittest.TestCase):
    def test_test(self):
        i18n.set_language("fr")
        res = xp._map_single(os.path.join(BASE_DIR, "resources", "cv_sample", "XP"), "201406-CyberShield")
        print(res.business_domain)
        self.assertEqual("Cybersécurité", res.business_domain)
