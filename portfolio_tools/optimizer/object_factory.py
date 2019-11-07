from portfolio_tools.optimizer.chart_plotter import chart_plotter
from portfolio_tools.optimizer.file_repository import file_repository
from portfolio_tools.optimizer.monte_carlo_simulator import monte_carlo_simulator
from portfolio_tools.optimizer.companies_extractor import webpage_companies_extractor as webpage_companies_extractor
from portfolio_tools.optimizer.companies_extractor import static_companies_extractor as static_companies_extractor
from portfolio_tools.optimizer.price_extractor import price_extractor
from portfolio_tools.optimizer.calculator import metrics_calculator
from portfolio_tools.optimizer import optimiser_factory


class object_factory:

    def __init__(self, settings):
        self.__settings = settings 
    
    def get_price_extractor(self, companies):
        return price_extractor(self.__settings.API, companies)

    def get_metrics_calculator(self):
        return metrics_calculator

    def get_charts_plotter(self):
        return chart_plotter(self.get_metrics_calculator())

    def get_companies_extractor(self):
        return static_companies_extractor(self.__settings().MyCompanies)

    def get_portfolio_generator(self):
        return monte_carlo_simulator(self.get_metrics_calculator(), self.__settings.RiskFunction, self.__settings.ReturnFunction, self.__settings.NumberOfPortfolios)

    def get_file_repository(self):
        return file_repository(self.__settings.PortfolioOptimisationFile)

    def get_optimiser(self, targets, size):
        return optimiser_factory.optimiser(self.get_metrics_calculator(), self.__settings.RiskFunction, self.__settings.ReturnFunction, targets, size)
    
