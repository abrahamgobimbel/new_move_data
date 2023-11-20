import function_activator
import os

def clear_terminal():
    os.system("cls")

pilihan = False
while not pilihan : 
    print("List Fitur \n")
    print ("1. Export EXCEL")
    print ("2. Export SQL\n")
    nomor = int(input(f"\nPilih nomor fitur yang ingin dijalankan : "))
    while nomor < 1 or nomor > 2 : 
        if nomor < 1 or nomor > 2:
            print(f"\nNomor yang diinput harus antara 1 hingga 2\n")
            nomor = int(input(f"Pilih nomor fitur yang ingin dijalankan : "))
    pilihan = True
if nomor == 1 :      
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
    
else : 
    clear_terminal()
    database_name = function_activator.database_name()
    clear_terminal()
    old_table_name = function_activator.old_table_name(old_database_name)  
    clear_terminal()
    data_excel = function_activator.data_excel(old_database_name, old_table_name)
    print (data_excel)
    for index, row in data_excel.iterrows() :
        insert_query = f"INSERT INTO "


