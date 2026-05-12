import os
import unittest

from globals import BASE_DIR
from libs.processors import xp
from libs.services import i18n


class TestGenXp(unittest.TestCase):
    def test_test(self):
        i18n.set_language("fr")
        res = xp._process_single(
            os.path.join(BASE_DIR, "cv_sample", "XP"), "2021.01-HUG"
        )
        print(res)
