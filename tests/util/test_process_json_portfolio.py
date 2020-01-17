import unittest
from portfolio_tools.util import process_json_portfolio
from portfolio_tools.config import config as config_p
from datetime import date 


class TestJsonProcess(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.src_port = config_p.WifeRothIRA().portfolio
        cls.src_wife = process_json_portfolio.ProcessJsonPortfolio()

    def test_calculate_average_price_wife(self):
        result, _, _ = self.src_wife.calculate_average_price(self.src_port)
        self.assertEqual(result['test']['Lots'][1]['Processed'], "True")

    def test_get_earliest_date(self):
        result = self.src_wife.get_earliest_date(self.src_port)
        self.assertEqual(date(2020,1,13), result)