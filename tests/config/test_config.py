import unittest
from portfolio_tools.config import config


class TestConfig(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.src = config.PortfolioConfig()

    def test_config(self):
        holdings_test = self.src.holdings_test
        self.assertEqual(holdings_test, ['abc', 'def'])
        holdings_count = self.src.holdings_count
        self.assertEqual(holdings_count[0], 105)