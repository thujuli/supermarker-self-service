from function import *

# mereset tabel transaction
reset_transaction('transaction.csv')

# tabel menyimpan transaksi sementara
transaction_table = 'transaction.csv'

# tabel menyimpan transaksi akhir
transaction_final_table = 'transaction_final.csv'

# var untuk memilih ulang transaksi atau selesai
again = True

greeting("selamat datang di pacmann supermarket")

while again:
    menu()

    choice = input('Masukkan Nomor Tugas : ')

    if choice == '1':
        list_item = choice_add_item()
        add_item(list_item, file=transaction_table)
        dict_transaction_table = csv_to_dict('transaction.csv')
        show_data(dict_transaction_table)

    elif choice == '2':
        nama_item, update_nama_item = choice_update_item_name() 
        update_item_name(nama_item, update_nama_item, file=transaction_table)
        dict_transaction_table = csv_to_dict('transaction.csv')
        show_data(dict_transaction_table)

    elif choice == '3':
        nama_item, update_jumlah_item = choice_update_item_qty() 
        update_item_qty(nama_item, update_jumlah_item, file=transaction_table)
        dict_transaction_table = csv_to_dict('transaction.csv')
        show_data(dict_transaction_table)

    elif choice == '4':
        nama_item, update_harga_item = choice_update_item_price() 
        update_item_price(nama_item, update_harga_item, file=transaction_table)
        dict_transaction_table = csv_to_dict('transaction.csv')
        show_data(dict_transaction_table)

    elif choice == '5':
        nama_item= choice_delete_item()
        delete_item(nama_item, file=transaction_table)
        dict_transaction_table = csv_to_dict('transaction.csv')
        show_data(dict_transaction_table)
    
    elif choice == '6':
        reset_transaction(file=transaction_table)
        dict_transaction_table = csv_to_dict('transaction.csv')
        show_data(dict_transaction_table)

    elif choice == '7':
        cek = check_order(file=transaction_table)
        if cek:
            field_total_harga(file=transaction_table, final_file=transaction_final_table)
            dict_transaction_final_table = csv_to_dict(transaction_final_table)
            show_data(dict_transaction_final_table)

            is_checkout = input('input by sistem sudah benar, apa anda mau checkout? ')
            if is_checkout:
                field_diskon(file=transaction_final_table)
                field_harga_diskon(file=transaction_final_table)

                dict_transaction_final_table = csv_to_dict(transaction_final_table)
                show_data(dict_transaction_final_table)

                greeting("terimakasih sudah berbelanja di pacmann supermarket")
                again = 'n'

    else:
        print('invalid, mohon masukkan pilihan dari (1-7)')

    again = input("Lanjut untuk melakukan transaksi (y/n)? ")
    if again.lower() == 'y':
        again = True
    else: 
        again = False
