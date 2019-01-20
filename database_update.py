import sqlite3
import pandas as pd
from api_func import GetHistData
def DatabaseConn(company, start_date, end_date):
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
    query = """SELECT *
               from company_hist
               where company='{comp}'
               and (date between date('{start}') and date('{end}'))
               order by date asc
               """.format(comp=company, start=start_date, end=end_date)
    results = pd.read_sql(query,conn)
    return results
    conn.close()
