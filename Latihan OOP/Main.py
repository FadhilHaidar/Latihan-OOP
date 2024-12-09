# Main.py
from data.mahasiswa import Mahasiswa, DataMahasiswa
from view.input_form import InputForm
from view.mahasiswa import ViewMahasiswa

# Inisialisasi DataMahasiswa
data_mahasiswa = DataMahasiswa()

def menu():
    print("\nMenu:")
    print("[1] Tambah Mahasiswa")
    print("[2] Tampilkan Semua Mahasiswa")
    print("[3] Cari Mahasiswa")
    print("[4] Ubah Mahasiswa")
    print("[5] Hapus Mahasiswa")
    print("[0] Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nim, nama, jurusan = InputForm.input_data()
        mahasiswa = Mahasiswa(nim, nama, jurusan)
        data_mahasiswa.tambah_data(mahasiswa)
        print("Data berhasil ditambahkan!")

    elif pilihan == "2":
        ViewMahasiswa.tampilkan_list(data_mahasiswa.data)

    elif pilihan == "3":
        nim = input("Masukkan NIM yang dicari: ")
        mahasiswa = data_mahasiswa.cari_data(nim)
        ViewMahasiswa.tampilkan_detail(mahasiswa)

    elif pilihan == "4":
        nim = input("Masukkan NIM mahasiswa yang ingin diubah: ")
        nama_baru = input("Masukkan nama baru (kosongkan jika tidak ingin mengubah): ")
        jurusan_baru = input("Masukkan jurusan baru (kosongkan jika tidak ingin mengubah): ")
        if data_mahasiswa.ubah_data(nim, nama_baru, jurusan_baru):
            print("Data berhasil diubah!")
        else:
            print("Mahasiswa tidak ditemukan!")

    elif pilihan == "5":
        nim = input("Masukkan NIM mahasiswa yang ingin dihapus: ")
        if data_mahasiswa.hapus_data(nim):
            print("Data berhasil dihapus!")
        else:
            print("Mahasiswa tidak ditemukan!")

    elif pilihan == "0":
        print("Keluar dari program.")
        break

    else:
        print("Pilihan tidak valid!")
