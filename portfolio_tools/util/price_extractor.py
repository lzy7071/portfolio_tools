import pandas as pd
import numpy as np
from pandas_datareader import data as web
import matplotlib.pyplot as plt
import scipy.optimize as solver


class PriceExtractor:

    def __init__(self, companies, provider='yahoo'):
        self.__api = provider
        self.__companies = companies

    def get_prices(self, start_date, end_date, event='Adj Close'):
        prices = pd.DataFrame()
        symbols = self.__companies
        tmp={}
        for i in symbols:
            try:
                tmp = web.DataReader(i, self.__api, start_date, end_date)
                print('Fetched prices for: '+i)                
            except:
                print('Issue getting prices for: '+i)
            else:
                prices[i] = tmp[event]            
        return prices