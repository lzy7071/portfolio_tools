import unittest
from portfolio_tools.config import config as config_p


class TestConfig(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.src = config_p.PortfolioConfig()
        cls.src_benchmark = config_p.BenchmarkConfig()
        cls.src_wife = config_p.WifeRothIRA()

    def test_config(self):
        holdings_test = self.src.holdings_test
        self.assertEqual(holdings_test, ['abc', 'def'])
        holdings_count = self.src.holdings_count
        self.assertEqual(holdings_count[0], 0)

    def test_benchmark(self):
        b_test = self.src_benchmark.test_benchmark
        h_test = self.src_benchmark.holdings_test
        self.assertEqual(b_test, ['benchmark'])
        self.assertEqual(h_test, ['abc', 'def'])

    def test_wife_roth(self):
        test = self.src_wife.load_portfolio()
        self.assertEqual(test['test']['Lots'][0]["Executed Price"], 91.645)

    @unittest.skip('passed')
    def test_process_portfolio_wife(self):
        tmp = self.src_wife.load_portfolio()
        result = self.src_wife.process_portfolio(tmp)
        print(result)

    def test_calculate_average_price_wife(self):
        tmp = self.src_wife.load_portfolio()
        result = self.src_wife.calculate_average_price(tmp)
        print(result)