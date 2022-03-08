class Mahasiswa:
    def __init__(self, nama, nim, prodi, thn_masuk, alamat):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.thn_masuk = thn_masuk
        self.__alamat = alamat


m1 = Mahasiswa('Udin', '10120371', 'Sistem Informasi', 2020, 'Yogyakarta')
m2 = Mahasiswa('ayla sauna', '521075849', 'Informatika', 2021,'purworejo')
m3 = Mahasiswa('unaya haniya', '5210411897', 'Informatika', 2021,'kalimantan barat')
m4 = Mahasiswa('Bella triana','5210411175','informatika',2021,'cilacap')

data_mahasiswa = [m1, m2, m3,m4]

print('Daftar Mahasiswa')
for i in data_mahasiswa:
        print(f'{i.nama} adalah mahasiswa {i.prodi} angkatan {i.thn_masuk} dengan nim {i.nim} dan beralamat di {i._Mahasiswa__alamat}')




print('bybell')