import sqlite3
def CreateTables():
    conn = sqlite3.connect('project_database.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS company_hist (
                    id integer,
                    open real,
                    high real,
                    low real,
                    close real,
                    volume string,
                    company text);""")
    conn.commit()
    c.close()
    conn.close()

    conn = sqlite3.connect('project_database.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS temp_table (
                    id integer,
                    open real,
                    high real,
                    low real,
                    close real,
                    volume string,
                    company text);""")
    conn.commit()
    c.close()
    conn.close()
