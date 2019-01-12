import sqlite3
import pandas as pd
from api_func import GetHistData
def DatabaseConn(company="BABA", start_date='2018-12-23', end_date='2018-12-30'):
    conn = sqlite3.connect('project_database.db')
    c = conn.cursor()
    df, company = GetHistData(company=company, start_date=start_date, end_date=end_date)
    df.to_sql('company_hist', conn, if_exists='replace', index=True)
    query = "SELECT date, open from company_hist"
    # pre_results = c.fetchall()
    results = pd.read_sql(query,conn)
    return results, company

    conn.commit()

    conn.close()
