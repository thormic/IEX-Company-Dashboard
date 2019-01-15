import sqlite3
import pandas as pd
from api_func import GetHistData
def DatabaseConn(company="BABA", start_date='2018-12-23', end_date='2018-12-30'):
    conn = sqlite3.connect('project_database.db')
    c = conn.cursor()
    df = GetHistData(company=company, start_date=start_date, end_date=end_date)
    # df.to_sql('company_hist', conn, if_exists='append', index=False)
    # query = "SELECT date, open, company from company_hist"
    # results = pd.read_sql(query,conn)
    # return results
    # conn.commit()
    # conn.close()
    df.to_sql('temp_table', conn, if_exists='replace', index=False)
    query_add = """INSERT INTO company_hist (date, open, high, low, close, volume, company)
                   SELECT date, open, high, low, close, volume, company from temp_table
                   EXCEPT
                   SELECT date, open, high, low, close, volume, company from company_hist"""
    c.execute(query_add)
    conn.commit()
    query = "SELECT date, open, company from company_hist order by date asc"
    results = pd.read_sql(query,conn)
    return results
    conn.close()
