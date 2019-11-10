import pygsheets
from portfolio_tools.config import config as auth_config


class AuthPygsheets:

    def __init__(self):
        self.gc = pygsheets.authorize(service_account_file=auth_config.PortfolioConfig().credentials)