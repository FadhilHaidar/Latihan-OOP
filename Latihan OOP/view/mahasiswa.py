# view/mahasiswa.py
class ViewMahasiswa:
    @staticmethod
    def tampilkan_list(data_mahasiswa):
        print("\nDaftar Mahasiswa:")
        print("=================================================================")
        for mhs in data_mahasiswa:
            print(f"NIM: {mhs.nim} | Nama: {mhs.nama} | Jurusan: {mhs.jurusan} |")
        print("=================================================================")

    @staticmethod
    def tampilkan_detail(mahasiswa):
        if mahasiswa:
            print("\nDetail Mahasiswa:")
            print("===========================")
            print(f"NIM: {mahasiswa.nim}")
            print(f"Nama: {mahasiswa.nama}")
            print(f"Jurusan: {mahasiswa.jurusan}")
            print("===========================")
        else:
            print("Mahasiswa tidak ditemukan!")
