import sqlite3
import pandas as pd
from comp_info import CompanyList



def ImportNames():
    """
    Reads contents from company_list table if there is any, if not runs
    a function CompanyList(). Returns DataFrame with all the companies names.
    """
    conn = sqlite3.connect('project_database.db')
    query = """SELECT
               short_name,
               full_name
               from company_list
               where full_name is not ''
               order by full_name asc
               """
    comp_names = pd.read_sql(query,conn)
    if comp_names.empty is True:
        CompanyList()
        comp_names = pd.read_sql(query,conn)
    conn.close()
    return comp_names



def ShortName(company_name):
    """
    Takes company_name as an argument and returns its short name from
    table company_list.
    """
    conn = sqlite3.connect('project_database.db')
    query = """SELECT
               short_name
               from company_list
               where full_name='{}'
               """.format(company_name)
    company = pd.read_sql(query,conn).iloc[0]['short_name']
    conn.close()
    return company
