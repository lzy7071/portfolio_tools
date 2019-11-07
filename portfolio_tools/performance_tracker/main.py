from portfolio_tools.performance_tracker import track_and_fill
import datetime as dt
from portfolio_tools.config import config as config_p


def main():
    sheet_name = config_p.PortfolioConfig().sheet_name
    holdings = config_p.PortfolioConfig().holdings
    holdings_count = config_p.PortfolioConfig().holdings_count
    credentials = config_p.PortfolioConfig().credentials
    scope = config_p.PortfolioConfig().scope
    manager = track_and_fill.TAF(sheet_name, portfolio_composition=holdings, holdings_count=holdings_count,
                                credentials=credentials, scope=scope)
    start_date = dt.datetime.today() - dt.timedelta(days=1)
    end_date = dt.datetime.today() - dt.timedelta(days=1)
    prices = manager.get_closing_prices(start_date, end_date)
    tmp = manager.make_list_for_update(prices)
    manager.update_price(tmp)
