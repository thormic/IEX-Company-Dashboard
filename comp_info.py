import pyEX as p
import sqlite3
from iexfinance import Stock
from pandas.io.json import json_normalize
import pandas as pd

def CompanyList():
    conn = sqlite3.connect('project_database.db')
    df = p.symbolsDF()
    df.reset_index(inplace=True)
    df = df[['symbol', 'date', 'name', 'type']]
    df.rename(columns={'symbol' : 'short_name', 'name' : 'full_name'}, inplace=True)
    df['notes']=""
    df.to_sql('company_list', conn, if_exists='replace', index=False)
    conn.commit()
    return df


def CompanyInfo(company):
    conn = sqlite3.connect('project_database.db')
    comp = Stock(company)
    dic = comp.get_key_stats()
    dic2 = comp.get_company()
    df = pd.DataFrame.from_dict(dic, orient='index')
    df = df.transpose()
    df2 = pd.DataFrame.from_dict(dic2, orient='index')
    df2 = df2.transpose()
    df2 = df2.drop(columns=['tags'])
    df.to_sql('key_info', conn, if_exists='replace', index=False)
    df2.to_sql('company_info', conn, if_exists='replace', index=False)
    conn.commit()
    conn.close()
