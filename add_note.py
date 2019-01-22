import sqlite3
import pandas as pd



def AddNote(company, note):
    """
    Takes note's merit and company name and updates it to
    company_list[note]
    """
    conn = sqlite3.connect('project_database.db')
    c = conn.cursor()
    query_add = """UPDATE company_list
                   SET notes='{note}'
                   WHERE short_name='{company}';
                   """.format(note=note, company=company)
    c.execute(query_add)
    conn.commit()
    conn.close()



def SeeNote(company):
    """
    Take's company name and shows note from company_list[note]
    """
    conn = sqlite3.connect('project_database.db')
    query = """SELECT notes
               from company_list
               where short_name='{comp}'
               """.format(comp=company)
    results = pd.read_sql(query,conn).iloc[0]['notes']
    conn.close()
    return results
