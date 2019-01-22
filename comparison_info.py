import sqlite3
import pandas as pd



def ComparisonInfo():
    """
    Returns summarized information about all the database contents from
    table company_hist as a DataFrame.
    """
    conn = sqlite3.connect('project_database.db')
    query = """SELECT
               cl.full_name as company_name,
               max(high) as max_price,
               min(low) as min_price,
               max(ch.date) as till_date,
               min(ch.date) as from_date,
               avg(volume) as mean_volume
               from company_hist ch
               left join company_list cl
               on ch.company=cl.short_name
               group by company"""
    results = pd.read_sql(query,conn)
    conn.close()
    return results
