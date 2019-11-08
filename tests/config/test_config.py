import unittest
from portfolio_tools.config import config as config_p


class TestConfig(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.src = config_p.PortfolioConfig()
        cls.src_benchmark = config_p.BenchmarkConfig()

    def test_config(self):
        holdings_test = self.src.holdings_test
        self.assertEqual(holdings_test, ['abc', 'def'])
        holdings_count = self.src.holdings_count
        self.assertEqual(holdings_count[0], 105)

    def test_benchmark(self):
        b_test = self.src_benchmark.test_benchmark
        h_test = self.src_benchmark.holdings_test
        self.assertEqual(b_test, 'benchmark')
        self.assertEqual(h_test, ['abc', 'def'])
