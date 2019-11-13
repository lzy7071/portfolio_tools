import unittest
from portfolio_tools.util import sheet_util


class TestSheeUtil(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        scope = ['https://www.googleapis.com/auth/drive']
        credentials = '~/.project_configs/portfolio_tools_credentials/project_api.json'
        sheet_name = 'Copy of All weather portfolio (liquid asset)'
        cls.src = sheet_util.Sheet(sheet_name, scope=scope, credentials=credentials)

    def test_setup(self):
        result_0 = self.src.sheet.worksheet('price')
        self.assertEqual(result_0.get_all_records()[0]['VOO'], 282.32)