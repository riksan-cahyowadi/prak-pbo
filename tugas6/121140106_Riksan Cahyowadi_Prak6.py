from abc import ABC, abstractmethod

class AkunBank(ABC):
    @abstractmethod
    def __init__(self, nama, tahun_daftar, saldo_pelanggan):
        self.nama = nama
        self.usia_akun = 2023 - tahun_daftar
        self.saldo_pelanggan = saldo_pelanggan
    
    @abstractmethod
    def transfer_saldo(self, transfer):
        pass
    
    @abstractmethod
    def lihat_suku_bunga(self):
        pass
    
class AkunGold(AkunBank):
    def transfer_saldo(self, transfer):
        if self.usia_akun >= 3 and transfer > 100000:
            print("biaya administrasi : gratis")
        elif self.usia_akun < 3 and transfer > 100000:
            print("biaya administrasi : Rp.2000")
        else:
            print("biaya administrasi : gratis")
            
    def lihat_suku_bunga(self):
        if self.usia_akun >= 3 and self.saldo_pelanggan >= 1000000000:
            print("bunga bulanan : {}".format(self.saldo_pelanggan * 0.01))
        elif self.usia_akun < 3 and self.saldo_pelanggan >= 1000000000:
            print("bunga bulanan : {}".format(self.saldo_pelanggan * 0.02))
        else:
            print("bunga bulanan : {}".format(self.saldo_pelanggan * 0.03))
            
class AkunSilver(AkunBank):
    def transfer_saldo(self, transfer):
        if self.usia_akun >= 3 and transfer > 100000:
            print("biaya administrasi : Rp.2000")
        elif self.usia_akun < 3 and transfer > 100000:
            print("biaya administrasi : Rp.5000")
        else:
            print("biaya administrasi : gratis")
            
    def lihat_suku_bunga(self):
        if self.usia_akun >= 3 and self.saldo_pelanggan >= 10000000:
            print("bunga bulanan : {}".format(self.saldo_pelanggan * 0.01))
        elif self.usia_akun < 3 and self.saldo_pelanggan >= 10000000:
            print("bunga bulanan : {}".format(self.saldo_pelanggan * 0.02))
        else:
            print("bunga bulanan : {}".format(self.saldo_pelanggan * 0.03))
