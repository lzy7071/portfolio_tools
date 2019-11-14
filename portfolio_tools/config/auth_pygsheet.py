import pygsheets
from portfolio_tools.config import config as auth_config
from pathlib import Path


class AuthPygsheets:

    def __init__(self):
        conf_dir = str(Path(auth_config.PortfolioConfig().credentials).expanduser())
        self.gc = pygsheets.authorize(service_account_file=conf_dir)