from configparser import ConfigParser
import json


class PortfolioConfig:

    config = ConfigParser()
    config.read('./credentials/sheets.ini')
    holdings_test = config['Portfolio']['holdings_test'].split(',')
    holdings = config['Portfolio']['holdings'].split(',')
    holdings_count = json.loads(config['Portfolio']['holdings_count'])
    scope = [config['Portfolio']['scope']]
    credentials = config['Portfolio']['credentials']
    sheet_name = config['Portfolio']['sheet_name']
