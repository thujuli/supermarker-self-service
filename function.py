import csv
from tabulate import tabulate

def reset_transaction(file):
    """
    Fungsi untuk membuat tabel baru / reset tabel

    arg:
        file (str): nama file csv untuk menyimpan transaksi

    return:
        None
    """
    with open(file=file, mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        
        csv_writer.writerow(['nama','jumlah','harga'])

def add_item(list_item, file):
    """
    Fungsi untuk menambahkan item ke file csv

    arg:
        list_item (list): array of item (nama, jumlah, harga)
        file (str): variable untuk menyimpan file csv

    return:
        None
    """

    with open(file=file, mode='a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)

        csv_writer.writerow(list_item)

def choice_add_item():
    """
    Fungsi untuk mengolah input jika memilih untuk add_item

    arg:
        None

    return: 
        list_item (list): array of item (nama, jumlah, harga)
    """

    nama_item = input('Masukkan nama item: ')
    jumlah_item = input('Masukkan jumlah item: ')
    harga_item = input('Masukkan harga item: ')

    list_item = [nama_item, jumlah_item, harga_item]
    return list_item

def update_item_name(nama_item, update_nama_item, file):
    """
    Fungsi untuk update nama item di keranjang

    arg:
        nama_item (str): nama item yang ingin diubah
        update_nama_item (str): nama item baru setelah diubah
        file (str): variable untuk menyimpan file csv
    
    return:
        None
    """

    with open(file=file, mode='r') as csvfile:
        csv_reader = csv.reader(csvfile)
        
        lines = list(csv_reader)
        
        for line in lines:
            if line[0] == nama_item: 
                line[0] =  update_nama_item
            
    with open(file='transaction.csv', mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(lines)

def choice_update_item_name():
    """
    Fungsi untuk mengolah input jika memilih untuk update_item_name

    arg:
        None

    return:
        nama_item (str): nama item yang ingin diubah
        update_nama_item (str): nama item baru setelah diubah
    """

    nama_item = input('Masukkan nama item yang ingin diubah: ')
    update_nama_item = input('Masukkan nama item baru tersebut: ')
    return [nama_item, update_nama_item]

def update_item_qty(nama_item, update_jumlah_item, file):
    """
    Fungsi untuk update jumlah item di keranjang

    arg:
        nama_item (str): item yang ingin diubah
        update_jumlah_item (str): jumlah qty yang baru
        file (str): variable untuk menyimpan file csv
    
    return:
        None
    """

    with open(file=file, mode='r') as csvfile:
        csv_reader = csv.reader(csvfile)
        
        lines = list(csv_reader)
        
        for line in lines:
            if line[0] == nama_item: 
                line[1] = update_jumlah_item 
            
    with open(file='transaction.csv', mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(lines)

def choice_update_item_qty():
    """
    Fungsi untuk mengolah input jika memilih untuk update_item_qty 

    arg:
        None

    return:
        nama_item (str): nama item yang ingin diubah
        update_jumlah_item (str): jumlah qty yang baru
    """

    nama_item = input('Masukkan nama item yang ingin diubah: ')
    update_jumlah_item = input('Masukkan jumlah qty baru tersebut: ')
    return [nama_item, update_jumlah_item]

def update_item_price(nama_item, update_harga_item, file):
    """
    Fungsi untuk update harga item di keranjang

    arg:
        nama_item (str): nama item yang ingin diubah
        update_harga_item (str): harga baru item tersebut
        file (str): variable untuk menyimpan file csv
    
    return:
        None
    """

    with open(file=file, mode='r') as csvfile:
        csv_reader = csv.reader(csvfile)
        
        lines = list(csv_reader)
        
        for line in lines:
            if line[0] == nama_item: 
                line[2] = update_harga_item
            
    with open(file='transaction.csv', mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(lines)

def choice_update_item_price():
    """
    Fungsi untuk mengolah input jika memilih untuk update_item_price

    arg:
        None

    return:
        nama_item (str): nama item yang ingin diubah
        update_harga_item (str): harga baru item tersebut
    """

    nama_item = input('Masukkan nama item yang ingin diubah: ')
    update_harga_item = input('Masukkan harga baru item tersebut: ')
    return [nama_item, update_harga_item]

def delete_item(nama_item, file):
    """
    Fungsi untuk update nama item di keranjang

    arg:
        nama_item (str): nama item yang ingin dihapus
        file (str): variable untuk menyimpan file csv
    
    return:
        None
    """
    with open(file=file, mode='r') as csvfile:
        csv_reader = csv.reader(csvfile)
        
        lines = list(csv_reader)
        new_lines = list()
        
        for line in lines:
            if line[0] != nama_item:
                new_lines.append(line)
                
    with open(file='transaction.csv', mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(new_lines)

def choice_delete_item():
    """
    Fungsi untuk mengolah input jika memilir untuk delete_item 

    arg:
        None

    return:
        nama_item (str): nama item yang ingin dihapus
    """

    nama_item = input('Masukkan nama item yang ingin dihapus: ')
    return nama_item

def check_order(file):
    """
    Fungsi untuk mengecek item yang dimasukkan sudah benar

    arg:
        file (str): variable untuk menyimpan file csv

    return:
        is_passed (bool) = melakukan validasi input user sudah sesuai 
    """
    with open(file=file, mode='r') as csvfile:
        
        csv_dict_reader = csv.DictReader(csvfile)
        cols = csv_dict_reader.fieldnames
        cols.append('total_harga') 
        
        is_passed = True

        for row in csv_dict_reader:

            # joining str tanpa space
            nama_split = row['nama'].split()
            nama_join = ''.join(nama_split)
            
            if not nama_join.isalpha():
                # mengganti nilai is_passed
                is_passed = False

                # menampilkan pemberitahuan ke user
                print('-'*60)
                print(f"Kesalahan input pada item {row['nama']}, nama tidak boleh mengandung karater spesial") 
                print('-'*60) 

            elif not row['jumlah'].isnumeric():
                # mengganti nilai is_passed
                is_passed = False

                # menampilkan pemberitahuan ke user
                print('-'*60)
                print(f"Kesalahan input pada item {row['nama']}, jumlah harus bilangan bulat")
                print('-'*60)
                
            elif not row['harga'].isnumeric():
                # mengganti nilai is_passed
                is_passed = False

                # menampilkan pemberitahuan ke user
                print('-'*60)
                print(f"Kesalahan input pada item {row['nama']}, harga harus bilangan bulat")
                
            else:
                print('-'*60)
                print(f"Pesanan untuk item {row['nama']} sudah benar")
                print('-'*60)

        return is_passed

def field_total_harga(file, final_file):
    """
    Fungsi untuk menambahkan field total_harga

    arg:
        file (str): variable untuk menyimpan file csv
        final_file (str): variable untuk menyimpan hasil akhir file csv

    return:
        None
    """

    with open(file=file, mode='r') as csvfile:
        
        csv_dict_reader = csv.DictReader(csvfile)
        cols = csv_dict_reader.fieldnames
        cols.append('total_harga')
        
        lines = list()
        
        for row in csv_dict_reader:
            jumlah = int(row['jumlah'])
            harga = int(row['harga'])
            total_harga = jumlah * harga
            row['total_harga'] = total_harga
            
            lines.append(row)
        
    with open(file=final_file, mode='w', newline='') as csvfile:
        cols = ['nama','jumlah','harga', 'total_harga']
        
        csv_dict_writer = csv.DictWriter(f=csvfile, fieldnames=cols)
        
        csv_dict_writer.writeheader()
        csv_dict_writer.writerows(lines)

def field_diskon(file):
    """
    Fungsi untuk menambahkan field diskon

    arg:
        file (str): variable untuk menyimpan file csv

    return:
        None
    """

    with open(file=file, mode='r') as csvfile:        
        csv_dict_reader = csv.DictReader(csvfile)
        cols = csv_dict_reader.fieldnames
        cols.append('diskon')
        
        lines = list()
        
        for row in csv_dict_reader:
            
            jumlah = int(row['jumlah'])
            harga = int(row['harga'])
            
            if harga > 500_000:
                diskon = harga*0.07
                row['diskon'] = int(diskon)
                
            elif harga > 300_000:
                diskon = harga*0.06
                row['diskon'] = int(diskon)
                
            elif harga > 200_000:
                diskon = harga*0.05
                row['diskon'] = int(diskon)
                
            else:
                row['diskon'] = 0
            
            lines.append(row)
            
    with open(file=file, mode='w', newline='') as csvfile:
        cols = ['nama','jumlah','harga', 'total_harga', 'diskon']
        
        csv_dict_writer = csv.DictWriter(f=csvfile, fieldnames=cols)
        
        csv_dict_writer.writeheader()
        csv_dict_writer.writerows(lines)

def field_harga_diskon(file):
    """
    Fungsi untuk menambahkan field harga_diskon

    arg:
        file (str): variable untuk menyimpan file csv

    return:
        None
    """

    with open(file=file, mode='r') as csvfile:
        
        csv_dict_reader = csv.DictReader(csvfile)
        cols = csv_dict_reader.fieldnames
        cols.append('harga_diskon')
        
        lines = list()
        
        for row in csv_dict_reader:
            
            jumlah = int(row['jumlah'])
            harga = int(row['harga'])
            diskon = int(row['diskon'])
           
            row['harga_diskon'] = harga - diskon
            row['total_harga'] = row['harga_diskon'] * jumlah
            
            lines.append(row)
        
    with open(file=file, mode='w', newline='') as csvfile:
        cols = ['nama','jumlah','harga', 'total_harga', 'diskon', 'harga_diskon']
        
        csv_dict_writer = csv.DictWriter(f=csvfile, fieldnames=cols)
        
        csv_dict_writer.writeheader()
        csv_dict_writer.writerows(lines)

def show_data(table):
    """
    Fungsi untuk menampilkan data

    arg:
        - table (dict) : data dictionary yang ingin ditampilkan

    return:
        None
    """
    tab = tabulate(tabular_data = table,
                   headers = table.keys(),
                   tablefmt = "psql",
                   numalign = "center")
    print(tab)

def csv_to_dict(filename):
    """
    Fungsi untuk ekstrak file csv menjadi list of dictionary

    arg:
        - filename (str) : nama file csv yang akan dibuka
    return:
        - data  (list) :  list of dictionary
    """

    # buka file csv
    with open(f'{filename}', mode='r', encoding='utf-8-sig') as file:
        csv_reader = csv.DictReader(file)

        # simpan dalam bentuk list of dictionary
        data = {}
        for row in csv_reader:
            for key, value in row.items():
                # setdefault() untuk menambahkan key ke result_dict
                # value dari key diisi dengan empty list dulu
                # empty list diisi dengan method append per baris data
                data.setdefault(key, []).append(value)

    return data

def greeting(greet):
    """
    Fungsi untuk menampilkan salam
    
    arg:
        greet (str): Salam yang ingin ditampilkan

    return:
        None
    """
    
    print("-"*60)
    print(greet.upper())
    print("-"*60)

def menu():
    """
    Fungsi untuk menampilkan daftar tugas.
    
    arg:
        None

    return:
        None
    """ 

    print("1. Tambahkan item ke keranjang")
    print("2. Perbarui nama item yang berada di keranjang")
    print("3. Perbarui jumlah item yang berada di keranjang")
    print("4. Perbarui harga item yang berada di keranjang")
    print("5. Hapus salah satu item")
    print("6. Hapus semua item di keranjang")
    print("7. Cek input item sudah sesuai dengan sistem\n")
