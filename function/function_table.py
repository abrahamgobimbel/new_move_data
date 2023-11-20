def old_database_name() :
    old_database_name = [
        'GOIconsV2',
        'GOKasirV2',
        'GOKreasi',
        'IsianDPPV3',
        'banksoalV2',
        ]
    return old_database_name
def old_table_name(old_database_name) :
    if old_database_name == 'db_GOIconsV2' :
        old_table_name = [
            'Produk'
        ]
    elif old_database_name == 'db_GOKreasi' : 
        old_table_name = [
            "peringkatnew"
        ]
    elif old_database_name == 'db_banksoalV2' :
        old_table_name = [
            "Bab",
            "Buku",
            "TOB",
            "isiTOB"
            ]
    elif old_database_name == 'db_GOIconsV2' :
        old_table_name = [
            "Bundling",
            "isiProdukMix",
            "mkt_JenisKelas",
            "mkt_JenisProduk"
            ]
    return old_table_name