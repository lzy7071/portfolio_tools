from configparser import ConfigParser
import json


class PortfolioConfig:

    config = ConfigParser()
    config.read('./credentials/sheets.ini')
    holdings_test = config['Portfolio']['holdings_test'].split(',')
    holdings = config['Portfolio']['holdings'].split(',')
    holdings_count = json.loads(config['Portfolio']['holdings_count'])
    scope = config['Portfolio']['scope'].split(',')
    credentials = config['Portfolio']['credentials']
    sheet_name = config['Portfolio']['sheet_name']
    money_market = float(config['Portfolio']['money_market'])


class BenchmarkConfig(PortfolioConfig):

    config = PortfolioConfig.config
    test_benchmark = config['Portfolio-benchmark']['holdings_test']
    holdings_benchmark = config['Portfolio-benchmark']['holdings']
    holdings_benchmark_count = config['Portfolio-benchmark']['holdings_count']