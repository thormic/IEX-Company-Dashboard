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
                    volume integer,
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
                    volume integer,
                    company text);""")
    conn.commit()
    c.close()
    conn.close()

    conn = sqlite3.connect('project_database.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS company_list (
                    id integer,
                    short_name text,
                    date text,
                    full_name text,
                    type text,
                    notes text);""")
    conn.commit()
    c.close()
    conn.close()

CreateTables()
