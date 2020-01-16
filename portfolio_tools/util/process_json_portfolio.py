import json
from datetime import datetime as dt
from datetime import date as dto


class ProcessJsonPortfolio:

    def __init__(self, _dict):
        """Init
        
        Args:
            _dict (:obj:`dict`): Portfolio object.
        """
        self._dict = _dict

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