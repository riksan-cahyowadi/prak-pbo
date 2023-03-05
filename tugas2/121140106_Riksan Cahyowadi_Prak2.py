#buat kelas, konstruktor, method, attribut (min 4), objek
#minimal atribut yang harus ada: Nama, NIM, Kelas PBO SIAKAD, jumlah SKS

#Ini class dengan nama "Diri"
class Diri:
    #constructor __init__ untuk membuat objek dan memiliki 4 atribut objek
    def __init__(self, nama, prodi, NIM, kelasPBO, sks):
        self.nama = nama
        self.NIM = NIM
        self.kelasPBO = kelasPBO
        self.sks = sks
        self.prodi = prodi

#method untuk mencetak data
    def cetak_data(self):
        print(" Nama saya " , self.nama)
        print(" program studi " , self.prodi)
        print(" dengan NIM " , self.NIM)
        print(" kelas PBO saya ada di "+ self.kelasPBO)
        print(" total sks yang diambil sebanyak ", self.sks, " sks")

#objek data_diri untuk mewakili class "Diri"
data_diri = Diri("Riksan Cahyowadi", "Teknik Informatika", 121140106, "RB", 22)

#menampilkan data ke layar
data_diri.cetak_data()
