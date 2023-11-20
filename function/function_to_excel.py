from pathlib import Path
import mysql.connector as connection
import pandas as pd
from datetime import date

def date_today() :
    date_today = date.today() 
    date_today = str(date_today).replace("-", "_")
    return date_today


def to_excel(old_database_name, table_name, database_name, sql_query):   
    print(f"\n{sql_query}\n")

    date_today_value = date_today()   
    db = connection.connect(host="192.168.169.193", database=f"{old_database_name}", user="goexpert", passwd="!6iri&Lu5i?")
    df = pd.read_sql(sql_query, db)
    directory_path = Path(f"{database_name}/excel")
    if not directory_path.exists():
        directory_path.mkdir(parents=True, exist_ok=True)
    df.to_excel(directory_path / f"{table_name}_{date_today_value}.xlsx")  