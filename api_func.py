import pandas as pd
import datetime
from iexfinance.stocks import get_historical_data
from pandas.io.json import json_normalize

def GetHistData(company="BABA", start_date="01-01-2014", end_date=datetime.datetime.today().strftime('%d-%m-%Y')):
    df1 = get_historical_data(company, start_date, end_date)
    df = pd.DataFrame.from_dict(df1, orient='index')
    df.reset_index(level=0, inplace=True)
    df.rename (columns={'index':'date'}, inplace = True)
    return df, company
