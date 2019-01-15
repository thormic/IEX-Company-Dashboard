import sqlite3
import pandas as pd
from datetime import datetime
from database_update import DatabaseConn
def DataDownload(company="BABA", start_date='2018-12-23', end_date='2018-12-30'):
    conn = sqlite3.connect('project_database.db')
    c = conn.cursor()
    sql_count = """select count(*)
                 from company_hist
                 where company='{comp}'
                 and (date between date('{start}') and date('{end}'))""".format(comp=company,
                                                                start=start_date,
                                                                end=end_date)
    c.execute(sql_count)
    result = c.fetchone()
    work_days = result[0]
    date_format = '%Y-%m-%d'
    start = datetime.strptime(start_date, date_format)
    end = datetime.strptime(end_date, date_format)
    d = end - start
    diff = d.days
    if (work_days/diff) < 0.65:
        downloaded = DatabaseConn(company, start_date, end_date)
    else:
        sql = """select *
                 from company_hist
                 where company='{comp}'
                 and (date between date('{start}') and date('{end}'))
                 order by date asc""".format(comp=company,
                                                                start=start_date,
                                                                end=end_date)
        downloaded = pd.read_sql(sql, conn)
    return downloaded

    conn.close()

print(DataDownload('FB', '2018-03-01', '2018-03-30'))
