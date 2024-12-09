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

1. Program Python

- Modul data/mahasiswa.py

  ![image](https://github.com/user-attachments/assets/8942fe01-5b3c-404a-a5ca-f6ec96d18c36)
  
  ![image](https://github.com/user-attachments/assets/c5e26ebf-817d-486c-8220-8d065d1073a7)

- Modul view/input_form.py

  ![image](https://github.com/user-attachments/assets/b7c5b16e-93f8-4132-b5d8-7011e08eeb9f)

- Modul view/mahasiswa.py

  ![image](https://github.com/user-attachments/assets/eb809049-b407-4bf9-b224-3e3ca72e6f02)

- Main.py

  ![image](https://github.com/user-attachments/assets/2f0285e2-17e5-404d-8eb2-4f4fc02a1867)

  ![image](https://github.com/user-attachments/assets/784bdc2c-0b76-44fd-9d55-e50b220f4dc9)

  ![image](https://github.com/user-attachments/assets/dbf17abf-8473-434a-829c-dd7b525a1f43)

2. Penjelasan

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

3. Input & Output

  ![image](https://github.com/user-attachments/assets/40d06748-42d9-4d22-ae09-3049ec8524ad)

  ![image](https://github.com/user-attachments/assets/60f36d4c-52ac-4b55-bae3-9366a369a046)
