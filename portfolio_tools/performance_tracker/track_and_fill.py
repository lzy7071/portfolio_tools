from portfolio_tools.util import price_extractor, sheet_util
import datetime as dt
from portfolio_tools.config import config as config_p
from portfolio_tools.config import auth_pygsheet
import gspread.exceptions


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

    def update_price(self, worksheet, _lists, holdings_count, money_market):
        """update price sheet
        
        Args:
            worksheet(:obj:`str`): name of worksheet
            _lists (:obj:`list` of :obj:`list`): lists with date and prices
            money_market (:obj:`flat`): money market holding
            holdings_count (:obj:`list`) number of holding for each stock

        Returns:
            (:obj:`list`): final rows 
        """
        result = []
        for _list in _lists:
            value = sum(a * b for a, b in zip(_list[1:-1], holdings_count))
            _list.append(money_market)
            total_value = value + money_market
            _list.append(total_value)
            result.append(_list)
            self.sheet.worksheet(worksheet).append_row(_list)
        return result

    def update_count(self, worksheet, date):
        """update count worksheet
        
        Args:
            worksheet(:obj:`str`): name of worksheet
            date (:obj:`str`): date
        """
        count = config_p.PortfolioConfig().holdings_count
        count.insert(0, str(date))
        try:
            self.sheet.worksheet(worksheet).append_row(count)
        except gspread.exceptions.WorksheetNotFound:
            self.sheet.add_worksheet(worksheet, 100, 100)
            self.sheet.worksheet(worksheet).append_row(count)

    def update_benchmark(self, worksheet, _lists, holdings_count, money_market):
        """update benchmark asset total value
        
        Args:
            worksheet(:obj:`str`): name of worksheet
            _lists (:obj:`list` of :obj:`list`): lists with date and prices
            money_market (:obj:`flat`): money market holding
            holdings_count (:obj:`list`) number of holding for each stock

        Returns:
            (:obj:`list`): final rows 
        """
        for _list in _lists:
            value = sum(a * b for a, b in zip(_list[1:], holdings_count))
            _list.append(money_market)
            total_value = value + money_market
            _list.append(total_value)
            self.sheet.worksheet(worksheet).append_row(_list)


class SheetBatch(auth_pygsheet.AuthPygsheets):

    def __init__(self, spreadsheet, portfolio_composition=None, holdings_count=None):
        self.spreadsheet = spreadsheet
        self.portfolio_composition = portfolio_composition
        self.holdings_count = holdings_count
        super().__init__()
        self.sh = self.gc.open_by_key(spreadsheet)

    def get_closing_prices(self, start_date, end_date):
        """get closing prices for date range 
        
        Args:
            start_date (:obj:`str`): starting date
            end_date (:obj:`str`): end date

        Returns:
            (:obj:`DataFrame`): prices
        """
        return price_extractor.PriceExtractor(self.portfolio_composition).get_prices(start_date, end_date)

    def set_empty_wksheet(self, worksheet, df):
        """name of worksheet to be set
        
        Args:
            worksheet (:obj:`str`): name of worksheet
            df (:obj:`DataFrame`): dataframe without column title
            dates (:obj:`list`): list of dates
        """
        wks = self.sh.worksheet_by_title(worksheet)
        wks.set_dataframe(df, (1,1), copy_index=True)