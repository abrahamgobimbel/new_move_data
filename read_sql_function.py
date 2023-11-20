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
database_name = function_activator.database_name(old_database_name)
all_data.append(f"database_name : {database_name}")
clear_terminal()
table_name = function_activator.table_name(database_name)  
all_data.append(f"table_name : {table_name}")  
clear_terminal()
for i in range(len(all_data)) : print(all_data[i])
sql_query = function_activator.sql_query(old_table_name)
function_activator.to_excel(old_database_name, table_name, database_name, sql_query)
clear_terminal()
print (f"Excel {database_name}_{table_name} sudah selesai")
nama_file_excel = 't_bab_2023_11_18.xlsx'
directory_path = Path(f"{database_name}/excel")
if not directory_path.exists():
        directory_path.mkdir()
file_path = Path(os.path.join(directory_path, nama_file_excel))
data_excel = pd.read_excel(file_path)

print(data_excel)
