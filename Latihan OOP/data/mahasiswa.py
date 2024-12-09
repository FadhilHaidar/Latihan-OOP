# data/mahasiswa.py
class Mahasiswa:
    def __init__(self, nim: str, nama: str, jurusan: str):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan


class DataMahasiswa:
    def __init__(self):
        self.data = []

    def tambah_data(self, mahasiswa: Mahasiswa):
        self.data.append(mahasiswa)

    def cari_data(self, nim: str):
        for mhs in self.data:
            if mhs.nim == nim:
                return mhs
        return None

    def hapus_data(self, nim: str):
        for mhs in self.data:
            if mhs.nim == nim:
                self.data.remove(mhs)
                return True
        return False

    def ubah_data(self, nim: str, nama_baru: str = None, jurusan_baru: str = None):
        mahasiswa = self.cari_data(nim)
        if mahasiswa:
            if nama_baru:
                mahasiswa.nama = nama_baru
            if jurusan_baru:
                mahasiswa.jurusan = jurusan_baru
            return True
        return False
