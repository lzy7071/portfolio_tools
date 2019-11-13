from configparser import ConfigParser
import json


class PortfolioConfig:

    config = ConfigParser()
    config.read('~/.project_configs/portfolio_tools_credentials/sheets.ini')
    holdings_test = config['Portfolio']['holdings_test'].split(',')
    holdings = config['Portfolio']['holdings'].split(',')
    holdings_count = json.loads(config['Portfolio']['holdings_count'])
    scope = config['Portfolio']['scope'].split(',')
    credentials = config['Portfolio']['credentials']
    sheet_name = config['Portfolio']['sheet_name']
    money_market = float(config['Portfolio']['money_market'])


class BenchmarkConfig(PortfolioConfig):

    config = PortfolioConfig.config
    test_benchmark = config['Portfolio-benchmark']['holdings_test'].split(',')
    holdings_benchmark = config['Portfolio-benchmark']['holdings'].split(',')
    holdings_benchmark_count = json.loads(config['Portfolio-benchmark']['holdings_count'])
    benchmark_money_market = float(config['Portfolio-benchmark']['money_market'])


class BootstrapConfig(BenchmarkConfig):
    
    config = BenchmarkConfig.config
    holdings_bootstrap = config['Portfolio-bootstrap']['holdings'].split(',')
    holdings_count_bootstrap = json.loads(config['Portfolio-bootstrap']['holdings_count'])
    sheet_id = config['Portfolio-bootstrap']['sheet_id']
    bootstrap_money_market = float(config['Portfolio-bootstrap']['money_market'])


class TestConfig(BenchmarkConfig):
    
    config = BenchmarkConfig.config
    holdings_test_0 = config['Portfolio-test-0']['holdings'].split(',')
    holdings_count_test_0 = json.loads(config['Portfolio-test-0']['holdings_count'])
    sheet_id = config['Portfolio-test-0']['sheet_id']
    test_0_money_market = float(config['Portfolio-test-0']['money_market'])