import unittest
from portfolio_tools.util import price_extractor
import datetime as dt  


class TestPriceExtractor(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        companies = ['AAPL', 'GOOG']
        cls.src = price_extractor.PriceExtractor(companies)

    def test_price_extractor(self):
        end_date_0 = dt.date(2019, 11, 6)
        start_date_0 = dt.date(2019, 10, 27)
        result_0 = self.src.get_prices(start_date_0, end_date_0)
        self.assertAlmostEqual(result_0.loc['2019-10-28']['AAPL'], 249.0500030517578)
        end_date_1 = dt.date(2019, 10, 27)
        start_date_1 = dt.date(2019, 10, 27)
        result_1 = self.src.get_prices(start_date_1, end_date_1)
        self.assertAlmostEqual(result_1.loc['2019-10-28']['AAPL'], 249.0500030517578)