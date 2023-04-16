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
       None

    return:
        True (bool): melakukan validasi untuk membuat column baru
    """
    with open(file=file, mode='r') as csvfile:
        
        csv_dict_reader = csv.DictReader(csvfile)
        cols = csv_dict_reader.fieldnames
        cols.append('total_harga') 
        
        for row in csv_dict_reader:
            
            nama_split = row['nama'].split()
            nama_join = ''.join(nama_split)
            
            if not nama_join.isalpha():
                print('-'*60)
                print(f"Kesalahan input pada item {row['nama']}, nama tidak boleh mengandung karater spesial") 
                print('-'*60)

            elif not row['jumlah'].isnumeric():
                print('-'*60)
                print(f"Kesalahan input pada item {row['nama']}, jumlah harus bilangan bulat")
                print('-'*60)
                
            elif not row['harga'].isnumeric():
                print('-'*60)
                print(f"Kesalahan input pada item {row['nama']}, harga harus bilangan bulat")
                
            else:
                print('-'*60)
                print(f"Pesanan untuk item {row['nama']} sudah benar")
                print('-'*60)
        
        return True

def add_total_harga(file):
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
        
    with open(file='transaction_total.csv', mode='w', newline='') as csvfile:
        cols = ['nama','jumlah','harga', 'total_harga']
        
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

def menu():
    """
    Fungsi untuk menampilkan daftar tugas.
    
    arg:
        None

    return:
        None
    """

    print("-"*60)
    print("SELAMAT DATANG DI SUPERMARKET PACMANN ")
    print("-"*60)

    print("1. Tambahkan item ke keranjang")
    print("2. Perbarui nama item yang berada di keranjang")
    print("3. Perbarui jumlah item yang berada di keranjang")
    print("4. Perbarui harga item yang berada di keranjang")
    print("5. Hapus salah satu item")
    print("6. Hapus semua item di keranjang")
    print("7. Cek input item sudah sesuai dengan sistem")
    # print("9. Exit\n")
    

# mereset tabel transaction
reset_transaction('transaction.csv')
transaction_table = 'transaction.csv'

# var untuk memilih ulang transaksi atau selesai
again = True

while again:
    menu()

    choice = int(input('Masukkan Nomor Tugas : '))

    if choice == 1:
        list_item = choice_add_item()
        add_item(list_item, file=transaction_table)

    elif choice == 2:
        nama_item, update_nama_item = choice_update_item_name() 
        update_item_name(nama_item, update_nama_item, file=transaction_table)

    elif choice == 3:
        nama_item, update_jumlah_item = choice_update_item_qty() 
        update_item_qty(nama_item, update_jumlah_item, file=transaction_table)

    elif choice == 4:
        nama_item, update_harga_item = choice_update_item_price() 
        update_item_price(nama_item, update_harga_item, file=transaction_table)

    elif choice == 5:
        nama_item= choice_delete_item()
        delete_item(nama_item, file=transaction_table)
    
    elif choice == 6:
        reset_transaction(file=transaction_table)

    elif choice == 7:
        cek = check_order(file=transaction_table)
        if cek:
            add_total_harga(file=transaction_table)
            transaction_table = csv_to_dict('transaction_total.csv')
            show_data(transaction_table)

    again = input("Lanjut untuk melakukan transaksi (y/n)? ")
    if again.lower() == 'y':
        again = True
    else: 
        again = False


