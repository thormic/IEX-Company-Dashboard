import sqlite3
import pandas as pd
from api_func import GetHistData 
def DatabaseConn():
    conn = sqlite3.connect('project_database.db')
    c = conn.cursor()
    df, company = GetHistData()
    df.to_sql('company_hist', conn, if_exists='replace', index=True)
    query = "SELECT date, open from company_hist"
    # pre_results = c.fetchall()
    results = pd.read_sql(query,conn)
    return results, company

    conn.commit()

    conn.close()