import sqlite3
import pandas as pd
def ImportNames():
    conn = sqlite3.connect('project_database.db')
    c = conn.cursor()
    query = "SELECT short_name, full_name from list_company"
    comp_names = pd.read_sql(query,conn)
    return comp_names

    conn.close()

def ShortName(company_name):
    conn = sqlite3.connect('project_database.db')
    c = conn.cursor()
    query = "SELECT short_name from list_company where full_name='{}'".format(company_name)
    company = pd.read_sql(query,conn).iloc[0]['short_name']
    return company

    conn.close()
