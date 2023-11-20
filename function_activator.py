import sys
import os
from function import function_table
from function import function_choice
from function import function_to_excel
from function import function_query

folder_path = "function"
sys.path.append(folder_path)



def old_database_name() :
    old_database_name = function_table.old_database_name()
    old_database_name = function_choice.old_database_name(old_database_name)
    return old_database_name

def database_name(old_database_name) :
    database_name = function_table.database_name(old_database_name)
    database_name = function_choice.database_name(database_name)
    return database_name

def old_table_name(old_database_name) :
    old_table_name = function_table.old_table_name(old_database_name)
    old_table_name = function_choice.old_table_name(old_table_name)
    return old_table_name

def table_name(database_name) :
    table_name = function_table.table_name(database_name)
    table_name = function_choice.table_name(table_name)
    return table_name

def to_excel(old_database_name, table_name, database_name, sql_query):
    function_to_excel.to_excel(old_database_name, table_name, database_name, sql_query)
    

def sql_query(old_table_name) :
    sql_query = function_query.sql_query(old_table_name)
    return sql_query