import json
from datetime import datetime as dt
from datetime import date as dto
import copy


class ProcessJsonPortfolio:

    def calculate_average_price(self, _dict):
        """Calculate dollar cost average per security.
        
        Args:
            _dict (:obj:`dict`): Portfolio loaded from json.

        Return:
            (:obj:`tuple` of :obj:`dict`, :obj:`list`, :obj:`list`): new portfolio object; list of securities; list of holdings 
        """
        securities = []
        holdings = []
        result = copy.deepcopy(_dict)
        for key in _dict:
            if key == 'test':
                continue
            total_count = 0
            total_cost = 0
            for i, val in enumerate(_dict[key]['Lots']):  #{'date': ... 'shares': ... 'executed price'}
                total_count += val['Shares']
                total_cost += val['Executed Price'] * val['Shares']
                result[key]['Lots'][i]['Processed'] = "True"
            avg_cost = total_cost / total_count
            result[key]['Total Holdings'] = total_count
            result[key]['Total Cost'] = total_cost
            result[key]['Average Cost'] = avg_cost
            securities.append(key)
            holdings.append(total_count)
        return result, securities, holdings

    def get_earliest_date(self, _dict):
        """Get the earliest unprocessed date.
        
        Args:
            _dict (:obj:`dict`): portfolio object.
        """
        earliest_date = dto.today()
        for key in _dict:
            if key == 'test':
                continue
            for val in _dict[key]['Lots']:
                if val.get('Processed') == "True":
                    continue
                else:
                    cur_date = dt.strptime(val['Date'], '%Y-%m-%d').date()
                    if cur_date < earliest_date:
                        earliest_date = cur_date
        return earliest_date

