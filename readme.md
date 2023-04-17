# supermarket-self-service
Program sederhana untuk user yang akan melakukan transaksi mandiri dan langsung terhubung dengan database SQLite

# Tujuan Project
1. Membuat system sederhana yang dapat melakukan:
    - Mempermudah user dalam input item 
    - Mempermudah user dalam edit data jika data sudah diinput
    - Mempermudah user dalam menghapus data jika terjadi salah input
    - Menampilkan daftar input user pada saat melakukan transaksi
    - Menampilkan kesalahan jika terjadi salah input data pada saat checkout
2. Membuat bahasa pemrograman python yang dapat langsung meyimpan data ke database SQLite
3. Menerapkan clean code, dan melakukan modularisasi

# Fungsi Setiap File
1. File 'main.py' berfungsi sebagai file utama dalam menjalankan/menghubungkan semua file lainnya
2. File 'start.py' berfungsi untuk melakukan pembuatan database data.db
3. File 'function.py' berfungsi sebagai tempat menyimpan semua function yang dibuat
4. File 'requirements.txt' merupakan file yang berisi library yang digunakan dalam membuat project
5. File 'transaction.csv' merupakan file yang digunakan dalam menyimpan transaksi sementara 
6. File 'transaction_final.csv' merupakan file yang digunakan untuk menyimpan hasil transaksi yang akan diinput kedalam database
7. File '.gitignore' file khusus yang menyimpan daftar file yang perlu diabaikan pada saat melakukan versioning (git/github)
8. File 'data.db' file yang digunakan untuk menyimpan hasil transaksi yang sudah dilakukan oleh user

# Cara Menggunakan Program
1. Buka terminal dan sesuaikan dengan lokasi direktori lokal
1. Sebelum memulai program, diwajibkan untuk menginstall library dengan menjalankan program 
    - `pip install requirements.txt`
2. Jika pada saat ingin menjalankan program ini terdapat file 'data.db', dapat menghapus file tersebut terlebih dahulu
3. Jalankan file 'start.py' pada terminal
    - `python start.py`
4. Jalankan file 'main.py' pada terminal
    - `python main.py`
