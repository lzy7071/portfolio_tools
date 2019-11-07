import unittest
from portfolio_tools.performance_tracker import track_and_fill
import datetime as dt


class TestTAF(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        scope = ['https://www.googleapis.com/auth/drive']
        credentials = './credentials/project_api.json'
        sheet_name = 'Copy of All weather portfolio (liquid asset)'
        portfolio_composition = ['AAPL', 'GOOG', '^GSPC']
        cls.src = track_and_fill.TAF(sheet_name, portfolio_composition=portfolio_composition, holdings_count=[1,1],
        credentials=credentials, scope=scope)

    def test_get_closing_prices(self):
        start_date = dt.date(2019, 7, 16)
        end_date = dt.date(2019, 7, 16)
        result = self.src.get_closing_prices(start_date, end_date)
        self.assertAlmostEqual(result.iloc[0]['AAPL'], 203.725952, places=5)

    def test_make_list_for_update(self):
        start_date = dt.date(2019, 7, 16)
        end_date = dt.date(2019, 7, 16)
        df = self.src.get_closing_prices(start_date, end_date) 
        result = self.src.make_list_for_update(df)
        self.assertEqual(result[0][0], '2019-07-16T00:00:00.000000000')