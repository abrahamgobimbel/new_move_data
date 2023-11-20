from datetime import date
import pandas as pd
from pathlib import Path
import os


def date_today() :
    date_today = date.today() 
    date_today = str(date_today).replace("-", "_")
    return date_today

def data_excel(old_database_name, old_table_name) :
    date_today_value = date_today()   
    nama_file_excel = f'{old_database_name}_{old_table_name}_{date_today_value}.xlsx'
    directory_path = Path(f"{old_database_name}/excel")
    file_path = Path(os.path.join(directory_path, nama_file_excel))
    data_excel = pd.read_excel(file_path)
    return data_excel