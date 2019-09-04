import unittest
from user_credentials import Info

class TestInfo(unittest.TestCase):
    def setUp(self):
        self.new_info =Info("firdausa.salat","salat.firdausa")
    def test_init(self):
        self.assertEqual(self.new_info.twitter_t,"firdausa.salat")
        self.assertEqual(self.new_info.email_e,"salat.firdausa")
    def test_save_info(self):
