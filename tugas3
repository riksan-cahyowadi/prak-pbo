class AkunBank:
    #List berisi data setiap pelanggan
    list_pelanggan = []

    #Membuat atrribut pada objek
    def __init__(self, no_pelanggan, nama_pelanggan, jumlah_saldo):
        self.no_pelanggan = no_pelanggan
        self.nama_pelanggan = nama_pelanggan
        self.jumlah_saldo = jumlah_saldo

        #Mengakses list pada atribut class
        AkunBank.list_pelanggan.append(self)

    #Display informasi tentang saldo pelanggan
    def lihat_saldo(self):
        print(f"Jumlah saldo saat ini yaitu: Rp. {self.jumlah_saldo}\n")

    #Penarikan saldo
    def tarik_tunai(self, jumlah_tarik):
        if jumlah_tarik <= self.jumlah_saldo:
            self.jumlah_saldo -= jumlah_tarik
            print(f"Penarikan tunai sebesar Rp. {jumlah_tarik} berhasil.")
            print(f"Jumlah saldo anda sekarang adalah: Rp. {self.jumlah_saldo}\n")
        else:
            print("Jumlah saldo anda tidak cukup!\n")

    #Transfer saldo ke akun lain
    def transfer(self, no_tujuan, jumlah_transfer):
        for pelanggan in AkunBank.list_pelanggan:

            if pelanggan.no_pelanggan == no_tujuan:
                if jumlah_transfer <= self.jumlah_saldo:
                    self.jumlah_saldo -= jumlah_transfer
                    pelanggan.jumlah_saldo += jumlah_transfer
                    print(f"Transfer sebesar Rp. {jumlah_transfer} ke pelanggan {pelanggan.nama_pelanggan} berhasil.")

                else:
                    print("Jumlah transfer melebihi saldo anda!\n")
                    return print("Rekening tujuan tidak ditemukan!\n")

    #Display menu yang akan dipilih oleh user
    def lihat_menu(self):
        print(f"\nSelamat datang di Bank BRI, {self.nama_pelanggan}")
        print("1. Cek saldo")
        print("2. Tarik Tunai")
        print("3. Transfer")
        print("4. Keluar\n")

akun1 = AkunBank(1234, "Riksan Cahyowadi", 5000000000)
akun2 = AkunBank(2345, "Ukraina", 7000000000)
akun3 = AkunBank(3456, "Elon Musk", 9000000000)

#Ini merupakan opsi pilihan akun oleh user
account = input("Akun mana yang ingin anda pilih?\nNote : (Pilih 1 untuk Akun1, 2 untuk Akun2, 3 untuk Akun3) \nPilihan anda:")

if account == "1":
    while True:
        akun1.lihat_menu()

        pilihan = input("Pilih no menu yang ingin diakses: ")

        if pilihan == "1":
            akun1.lihat_saldo()

        elif pilihan == "2":
            jumlah_tarik = int(input("Masukkan jumlah nominal yang ingin ditarik: "))
            akun1.tarik_tunai(jumlah_tarik)

        elif pilihan == "3":
            jumlah_transfer = int(input("Masukkan nominal yang ingin di transfer: "))
            no_tujuan = int(input("Masukkan nomor rekening tujuan: "))
            akun1.transfer(no_tujuan, jumlah_transfer)

        elif pilihan == "4":
            print("Program selesai")
            break

        else:
            print("Input salah ! Silahkan coba lagi")

elif account == "2":
    while True:
        akun2.lihat_menu()

        pilihan = input("Pilih no menu yang ingin diakses: ")

        if pilihan == "1":
            akun2.lihat_saldo()

        elif pilihan == "2":
            jumlah_tarik = int(input("Masukkan jumlah nominal yang ingin ditarik: "))
            akun2.tarik_tunai(jumlah_tarik)

        elif pilihan == "3":
            jumlah_transfer = int(input("Masukkan nominal yang ingin di transfer: "))
            no_tujuan = int(input("Masukkan nomor rekening tujuan: "))
            akun1.transfer(no_tujuan, jumlah_transfer)

        elif pilihan == "4":
            print("Program selesai")
            break

        else:
            print("Input salah ! Silahkan coba lagi")

elif account == "3":
    while True:
        akun3.lihat_menu()

        pilihan = input("Pilih no menu yang ingin diakses: ")

        if pilihan == "1":
            akun3.lihat_saldo()
        elif pilihan == "2":
            input_jumlah = input(
                "Masukkan jumlah nominal yang ingin ditarik: ")
            jumlah_tarik = int(input_jumlah)
            akun3.tarik_tunai(jumlah_tarik)

        elif pilihan == "3":
            input_transfer = input(
                "Masukkan nominal yang ingin di transfer: ")
            jumlah_transfer = int(input_transfer)
            input_tujuan = input("Masukkan nomor rekening tujuan: ")
            no_tujuan = int(input_tujuan)
            akun3.transfer(no_tujuan, jumlah_transfer)

        elif pilihan == "4":
            print("Program selesai")
            break

        else:
            print("Input salah ! Silahkan coba lagi")

else:
    print("Input salah ! Silahkan coba lagi")
