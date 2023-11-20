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

def database_name() :
    database_name = [
            'go',
            'kbm',
            'materi',
            'materi_teaser',
            'product',
            'product_teaser',
            'pt',
            'report_siswa_empati_mandiri',
            'report_siswa_empati_wajib',
            'report_siswa_goa',
            'report_siswa_irt',
            'report_siswa_kuis',
            'report_siswa_koding',
            'report_siswa_lateks',
            'report_siswa_paket_intensif',
            'report_siswa_pendalaman_materi',
            'report_siswa_peringkat',
            'report_siswa_presensi',
            'report_siswa_racing',
            'report_siswa_soref',
            'report_siswa_tobk',
            'report_siswa_vak',
            'report_tamu',
            'sekolah',
            'user',
            'user_lembaga',
            'user_tamu'
        ]
    return database_name    
def table_name(database_name) :
    if database_name == 'db_materi' :
        table_name = [
            "bab",
            "buku"
            ]
    elif database_name == 'db_product' :
        table_name = [
            "bundling",
            "isi_produk_mix",
            "isi_tob",
            "jenis_kelas",
            "jenis_produk",
            "produk",
            "tob"
        ]
    elif database_name == 'db_report_siswa_peringkat' :
        table_name = [
            "peringkat_new"
        ]
    return table_name