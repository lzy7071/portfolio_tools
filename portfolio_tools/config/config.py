from configparser import ConfigParser
import json
from datetime import datetime as dt
from datetime import date as dto
from pathlib import Path


class PortfolioConfig:

    config = ConfigParser()
    config_path = str(Path('~/.project_configs/portfolio_tools_credentials/sheets.ini').expanduser())
    config.read(config_path)
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

    def __init__(self, profile='Portfolio-test-0'):    
        config = BenchmarkConfig.config
        self.holdings_test_0 = config[profile]['holdings'].split(',')
        # self.holdings_count_test_0 = json.loads(config[profile]['holdings_count'])
        self.sheet_id = config[profile]['sheet_id']
        self.test_0_money_market = float(config[profile]['money_market'])


class WifeRothIRA:

    def __init__(self, porfolio='~/.project_configs/portfolio_tools_credentials/wife_roth_ira.json'):
        self.portfolio_file = str(Path('~/.project_configs/portfolio_tools_credentials/wife_roth_ira.json').expanduser())

    def load_portfolio(self):
        with open(self.portfolio_file) as f:
            portfolio = json.load(f)
        return portfolio

    def process_portfolio(self, _dict):
        """Process key/val pairs in portfolio file
        
        Args:
            _dict (:obj:`dict`): Portfolio loaded from json.

        Return:
            (:obj:`list` of :obj:`dict`): list of securities and dates with which to get pricing info. 
        """
        sd = {'earliest_date': dto(2100, 1, 1), 'latest_date': dto.today(), 'equities': {},
              'companies': []}
        for key in _dict:
            if key == 'test':
                continue
            for i, val in enumerate(_dict[key]):
                date = dt.strptime(val.get('Date'), '%Y-%m-%d').date()
                sd['companies'].append(key)
                if date < sd['earliest_date']:
                    sd['earliest_date'] = date

                if sd['equities'].get(key) is None:
                    sd['equities'][key] = [i]
                else:
                    sd['equities'][key] += [i]
        return sd

    def calculate_average_price(self, _dict):
        """Calculate dollar cost average per security.
        
        Args:
            _dict (:obj:`dict`): Portfolio loaded from json.

        Return:
            (:obj:`dict`): Securities and their corresponding average purchase price.
        """
        for key in _dict:
            if key == 'test':
                continue
            total_count = 0
            total_cost = 0
            for val in _dict[key]['Lots']:  #{'date': ... 'shares': ... 'executed price'}
                total_count += val['Shares']
                total_cost += val['Executed Price'] * val['Shares']
            avg_cost = total_cost / total_count
            _dict[key]['Total Holdings'] = total_count
            _dict[key]['Total Cost'] = total_cost
            _dict[key]['Average Cost'] = avg_cost
        return _dict
