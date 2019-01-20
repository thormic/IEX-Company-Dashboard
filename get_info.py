import sqlite3
import pandas as pd

def GetInfo(company):
    conn = sqlite3.connect('project_database.db')
    query = """
              select
              c.short_name,
              c.full_name,
              c.type,
              i.industry,
              i.website,
              i.description,
              i.CEO,
              i.sector,
              k.marketcap,
              k.week52high,
              k.week52low,
              k.ytdChangePercent
              from company_list c
              left join company_info i
              on c.short_name = i.symbol
              left join key_info k
              on c.short_name = k.symbol
              where short_name='{comp}'
              """.format(comp=company)
    company_info = pd.read_sql(query, conn)
    conn.close()
    return company_info
