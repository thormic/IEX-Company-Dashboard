import pandas as pd
import datetime
from iexfinance.stocks import get_historical_data
from pandas.io.json import json_normalize

def GetHistData(company, start_date, end_date):
    df1 = get_historical_data(company, start_date, end_date)
    df = pd.DataFrame.from_dict(df1, orient='index')
    df.reset_index(level=0, inplace=True)
    df.rename (columns={'index':'date'}, inplace = True)
    df['company']=company
    return df
