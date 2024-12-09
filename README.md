# Latihan OOP

Buatlah package dan modul dengan struktur seperti berikut:

- data -> mahasiswa.py

  berisi model data yang mendefinisikan class Mahasiswa dan class DataMahasiswa untuk proses pencarian data, tambah data, hapus data, dan ubah data. 

- view -> input_form.py

  berisi class untuk form input data mahasiswa 

- view -> mahasiswa.py

  berisi class untuk proses menapilkan list data dan detail data. 

- Main.py

  program utama yang menampilkan menu utama.

# Tampilan Program

1. Flowchart & Diagram Kelas

2. Program Python



3. Penjelasan

  Program ini dirancang untuk mengelola data mahasiswa menggunakan paradigma berorientasi objek (OOP). Program dibagi menjadi beberapa modul untuk memisahkan tugas:

  a. data/mahasiswa.py:
    
  - Mengelola representasi dan manipulasi data mahasiswa.
  
  - Terdiri dari dua kelas:

    - Mahasiswa
        
        - Model yang merepresentasikan data mahasiswa.
        
        - Model data yang mendefinisikan atribut nim, nama, dan jurusan.
        
        - Tidak memiliki metode khusus karena hanya menyimpan data.

    - DataMahasiswa

      - Pengelolaan data mahasiswa menggunakan metode CRUD:
          
          - tambah_data: Menambahkan objek mahasiswa ke daftar.
          
          - cari_data: Mencari mahasiswa berdasarkan NIM.
          
          - hapus_data: Menghapus mahasiswa dari daftar berdasarkan NIM.
          
          - ubah_data: Memperbarui data mahasiswa (nama/jurusan) berdasarkan NIM.
  
  b. view/input_form.py:
  
  - Mengambil input dari pengguna untuk data mahasiswa (NIM, Nama, dan Jurusan).
  
  - Mengembalikan data sebagai tuple.
  
  c. view/mahasiswa.py:
  
  - Menyediakan metode untuk menampilkan data mahasiswa:

    - tampilkan_list: Menampilkan daftar mahasiswa dalam format tabel sederhana.
   
    - tampilkan_detail: Menampilkan detail mahasiswa berdasarkan objek mahasiswa yang ditemukan.
  
  d. Main.py:
  
  - Program utama, menyatukan semua modul dan menampilkan menu utama.

  - Menu Interaktif: Menampilkan pilihan untuk menambah, menampilkan, mencari, mengubah, dan menghapus data mahasiswa.

  - Integrasi Modul: Menggunakan fungsi dari modul data dan view.

  - Looping: Program terus berjalan hingga pengguna memilih opsi keluar.

4. Input & Output
