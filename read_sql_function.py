import function_activator
import pandas as pd
from pathlib import Path

import os

def clear_terminal():
    os.system("cls")
all_data = []
clear_terminal()
old_database_name = function_activator.old_database_name()    
all_data.append(f"old_database_name : {old_database_name}")
clear_terminal()
old_table_name = function_activator.old_table_name(old_database_name)  
all_data.append(f"old_table_name : {old_table_name}")   
clear_terminal()
for i in range(len(all_data)) : print(all_data[i])
sql_query = function_activator.sql_query(old_table_name)
function_activator.to_excel(old_database_name, old_table_name, sql_query)
clear_terminal()
print (f"Excel {old_database_name}_{old_table_name} sudah selesai")

from datetime import date
def date_today() :
    date_today = date.today() 
    date_today = str(date_today).replace("-", "_")
    return date_today

date_today_value = date_today()   
nama_file_excel = f'{old_database_name}_{old_table_name}_{date_today_value}.xlsx'
directory_path = Path(f"{old_database_name}/excel")
file_path = Path(os.path.join(directory_path, nama_file_excel))
data_excel = pd.read_excel(file_path)

print(data_excel)

