from portfolio_tools.util import price_extractor, sheet_util
import datetime as dt


class TAF(sheet_util.Sheet):

    def __init__(self, spreadsheet, portfolio_composition=None, holdings_count=None,
                credentials=None, scope=None):
        """initialization
        
        Args:
            spreadsheet (:obj:`str`): name of spreadsheet
            portfolio_composition (:obj:`list` of :obj:`str`, optional): list of portfolio hodings. Defaults to None.
            holdings_count (:obj:`list` of :obj:`int`, optional): list of number of holdings. Defaults to None.
            credentials (:obj:`str`, optional): location of credential file. Defaults to None.
            scope (:obj:`str`, optional): auth scope. Defaults to None.
        """
        super().__init__(spreadsheet, scope=scope, credentials=credentials)
        self.portfolio_composition = portfolio_composition
        self.holdings_count = holdings_count

    def get_closing_prices(self, start_date, end_date):
        """get closing prices for date range 
        
        Args:
            start_date (:obj:`str`): starting date
            end_date (:obj:`str`): end date

        Returns:
            (:obj:`DataFrame`): prices
        """
        start_date = start_date
        end_date = end_date
        return price_extractor.PriceExtractor(self.portfolio_composition).get_prices(start_date, end_date)

    def make_list_for_update(self, df):
        """Make lists for update in sheets
        
        Args:
            df (:obj:`DataFrame`): dataframe to convert

        Returns:
            (:obj:`list`): converted lists
        """
        result = []
        values = df.values.tolist()
        dates = df.index.values
        for date, value in zip(dates, values):
            value.insert(0, str(date))
            result.append(value)
        return result

    def update_price(self, _lists, holdings_count, money_market):
        """update price sheet
        
        Args:
            _lists (:obj:`list`): lists with date and prices
            money_market (:obj:`flat`): money market holding
            holdings_count (:obj:`list`) number of holding for each stock
        """
        for _list in _lists:
            value = sum(a * b for a, b in zip(_list[:-1], holdings_count[:-1]))
            _list.append(money_market)
            total_value = value + money_market
            _list.append(total_value)
            self.sheet.worksheet('price').append_row(_list)