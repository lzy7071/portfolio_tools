import unittest
from portfolio_tools.config import auth_pygsheet


class TestAuthPygsheet(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.src = auth_pygsheet.AuthPygsheets()

    def test_auth(self):
        self.gc = self.src