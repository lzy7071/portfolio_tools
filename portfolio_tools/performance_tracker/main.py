from portfolio_tools.performance_tracker import track_and_fill
from portfolio_tools.util import price_extractor, process_json_portfolio
import datetime as dt
from portfolio_tools.config import config as config_p


def main():
    sheet_name = config_p.PortfolioConfig().sheet_name
    holdings = config_p.PortfolioConfig().holdings
    holdings_count = config_p.PortfolioConfig().holdings_count
    credentials = config_p.PortfolioConfig().credentials
    scope = config_p.PortfolioConfig().scope
    money_market = config_p.PortfolioConfig().money_market
    manager = track_and_fill.TAF(sheet_name, portfolio_composition=holdings, holdings_count=holdings_count,
                                credentials=credentials, scope=scope)
    start_date = dt.date.today()
    end_date = dt.date.today()
    prices = manager.get_closing_prices(start_date, end_date)
    prices.fillna(0, inplace=True)
    tmp = manager.make_list_for_update(prices)
    _ = manager.update_price('price', tmp, holdings_count, money_market)
    manager.update_count('count', start_date)
    
def benchmark():
    sheet_name = config_p.BenchmarkConfig().sheet_name
    holdings = config_p.BenchmarkConfig().holdings_benchmark
    holdings_count = config_p.BenchmarkConfig().holdings_benchmark_count
    credentials = config_p.BenchmarkConfig().credentials
    scope = config_p.BenchmarkConfig().scope
    money_market = config_p.BenchmarkConfig().benchmark_money_market
    start_date = dt.date.today()
    end_date = dt.date.today()
    manager = track_and_fill.TAF(sheet_name, portfolio_composition=holdings, holdings_count=holdings_count,
                                credentials=credentials, scope=scope)
    prices = manager.get_closing_prices(start_date, end_date)
    tmp = manager.make_list_for_update(prices)
    manager.update_benchmark('benchmark', tmp, holdings_count, money_market)

def ideas():
    sheet_name = config_p.BootstrapConfig().sheet_id
    holdings = config_p.BootstrapConfig().holdings_bootstrap
    holdings_count = config_p.BootstrapConfig().holdings_count_bootstrap
    credentials = config_p.BenchmarkConfig().credentials
    scope = config_p.BenchmarkConfig().scope
    money_market = config_p.BootstrapConfig().bootstrap_money_market
    start_date = dt.datetime(2014, 11, 8)
    end_date = dt.datetime(2019, 11, 8)
    manager = track_and_fill.TAF(sheet_name, portfolio_composition=holdings, holdings_count=holdings_count,
                                credentials=credentials, scope=scope)
    prices = manager.get_closing_prices(start_date, end_date)
    tmp = manager.make_list_for_update(prices)
    manager.update_benchmark('benchmark', tmp, holdings_count, money_market)

def fill_as_dataframe():
    sheet_name = config_p.TestConfig(profile='Portfolio-test-2').sheet_id
    holdings = config_p.TestConfig(profile='Portfolio-test-2').holdings_test_0
    # holdings_count = config_p.TestConfig(profile='Portfolio-test-1').holdings_count_test_0
    money_market = config_p.TestConfig(profile='Portfolio-test-2').test_0_money_market 
    start_date = dt.datetime(2014, 11, 8)
    end_date = dt.datetime(2019, 12, 5)
    manager = track_and_fill.SheetBatch(sheet_name, portfolio_composition=holdings)
    prices = manager.get_closing_prices(start_date, end_date)
    daily_return = prices.pct_change()
    cov = daily_return.cov()
    cor = daily_return.corr()
    manager.set_empty_wksheet('prices', prices)
    manager.set_empty_wksheet('correlation', cor)
    manager.set_empty_wksheet('covariance', cov)
    manager.set_empty_wksheet('daily_returns', daily_return)

def track_wife_ira():
    portfolio = config_p.WifeRothIRA().portfolio
    json_manager = process_json_portfolio.ProcessJsonPortfolio()
    new_portfolio, securities, count = json_manager.calculate_average_price(portfolio)
    earliest_date = json_manager.get_earliest_date(portfolio)
    prices = price_extractor.PriceExtractor(securities).get_prices(earliest_date, dt.date.today())
    print(prices)
    print(prices.multiply(count, axis=1))


if __name__ == '__main__':
    main()
    # benchmark()
    # ideas()
    # fill_as_dataframe()
    # track_wife_ira()