# portfolio optimizator

1. Monte Carlo of portfolio
2. Portfolio performance tracking and writing into google sheets

## Installation

1. git clone git@github.com:lzy7071/PortfolioOptimisation.git
2. cd PortfolioOptimisation
3. pip install -e .
4. google api json file in ~/.project_configs/credentials/
5. google sheet variables in .ini file in ~/.project_configs/credentials/ in following format  
    [Portfolio]  
    holdings = abc,def  
    holdings_count = [105,175]  
    scope = https://www.googleapis.com/auth/drive  
    credentials = ~/.project_configs/credentials/project_api.json  
    sheet_name = google spreadsheet ID
    money_market = 12313         

