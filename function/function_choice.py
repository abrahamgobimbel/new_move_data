def old_database_name(old_database_name):
    pilihan = False
    while not pilihan : 
        for i in range(len(old_database_name)) : old_database_name[i] = f"db_{old_database_name[i]}"
        print ("\nOld database list : \n")
        for i in range(len(old_database_name)) : print(f"{i+1}.{old_database_name[i]}")

        nomor = int(input(f"\nPilih nomor database yang diinginkan (1-{len(old_database_name)}) : "))
        while nomor < 1 or nomor > len(old_database_name) : 
            if nomor < 1 or nomor > len(old_database_name):
                print(f"Nomor yang diinput harus antara 1 hingga {len(old_database_name)}\n")
                nomor = int(input(f"Pilih nomor database yang diinginkan (1-{len(old_database_name)}) : "))
        old_database_name = f"{old_database_name[nomor-1]}"
        while pilihan != 'y' and pilihan != 'n' :
            pilihan = input(f"Nama database : {old_database_name} | Apakah nama database postgre sudah sesuai (y|n) : ")
        if (pilihan != 'y' and pilihan != 'n') :
            print("input harus y (yes) or n (no)")
        if pilihan.lower() == 'y' : 
            pilihan = True
        elif pilihan.lower()  == 'n' :
            pilihan = False    
    return old_database_name

def old_table_name(old_table_name):
    pilihan = False
    while not pilihan : 
        for i in range(len(old_table_name)) : old_table_name[i] = f"t_{old_table_name[i]}"
        print ("\nOld table name : \n")
        for i in range(len(old_table_name)) : print(f"{i+1}.{old_table_name[i]}")

        nomor = int(input(f"\nPilih nomor database yang diinginkan (1-{len(old_table_name)}) : "))
        while nomor < 1 or nomor > len(old_table_name) : 
            if nomor < 1 or nomor > len(old_table_name):
                print(f"Nomor yang diinput harus antara 1 hingga {len(old_table_name)}\n")
                nomor = int(input(f"Pilih nomor database yang diinginkan (1-{len(old_table_name)}) : "))
        old_table_name = f"{old_table_name[nomor-1]}"
        while pilihan != 'y' and pilihan != 'n' :
            pilihan = input(f"Nama database : {old_table_name} | Apakah nama database postgre sudah sesuai (y|n) : ")
        if (pilihan != 'y' and pilihan != 'n') :
            print("input harus y (yes) or n (no)")
        if pilihan.lower() == 'y' : 
            pilihan = True
        elif pilihan.lower()  == 'n' :
            pilihan = False    
    return old_table_name

def database_name(database_name):
    pilihan = False
    while not pilihan : 
        for i in range(len(database_name)) : database_name[i] = f"db_{database_name[i]}"
        print ("\nDatabase name : \n")
        for i in range(len(database_name)) : print(f"{i+1}.{database_name[i]}")

        nomor = int(input(f"\nPilih nomor database yang diinginkan (1-{len(database_name)}) : "))
        while nomor < 1 or nomor > len(database_name) : 
            if nomor < 1 or nomor > len(database_name):
                print(f"Nomor yang diinput harus antara 1 hingga {len(database_name)}\n")
                nomor = int(input(f"Pilih nomor database yang diinginkan (1-{len(database_name)}) : "))
        database_name = f"{database_name[nomor-1]}"
        while pilihan != 'y' and pilihan != 'n' :
            pilihan = input(f"Nama database : {database_name} | Apakah nama database postgre sudah sesuai (y|n) : ")
        if (pilihan != 'y' and pilihan != 'n') :
            print("input harus y (yes) or n (no)")
        if pilihan.lower() == 'y' : 
            pilihan = True
        elif pilihan.lower()  == 'n' :
            pilihan = False    
    return database_name

def table_name(table_name):
    pilihan = False
    while not pilihan : 
        for i in range(len(table_name)) : table_name[i] = f"t_{table_name[i]}"
        print ("\nTable name : \n")
        for i in range(len(table_name)) : print(f"{i+1}.{table_name[i]}")

        nomor = int(input(f"\nPilih nomor database yang diinginkan (1-{len(table_name)}) : "))
        while nomor < 1 or nomor > len(table_name) : 
            if nomor < 1 or nomor > len(table_name):
                print(f"Nomor yang diinput harus antara 1 hingga {len(table_name)}\n")
                nomor = int(input(f"Pilih nomor database yang diinginkan (1-{len(table_name)}) : "))
        table_name = f"{table_name[nomor-1]}"
        while pilihan != 'y' and pilihan != 'n' :
            pilihan = input(f"Nama database : {table_name} | Apakah nama database postgre sudah sesuai (y|n) : ")
        if (pilihan != 'y' and pilihan != 'n') :
            print("input harus y (yes) or n (no)")
        if pilihan.lower() == 'y' : 
            pilihan = True
        elif pilihan.lower()  == 'n' :
            pilihan = False    
    return table_name