class Biodata:
    def __init__(self, nama, umur):
        self.public_nama = nama  # atribut public
        self._protected_umur = umur  # atribut protected
        self.__private_gender = "Unknown"  # atribut private
    
    # Mencetak public method
    def public_method(self):
        print("Ini adalah public method.")
    
    # Mencetak protected method
    def _protected_method(self):
        print("Ini adalah protected method.")
    
    # Mencetak private method
    def __private_method(self):
        print("Ini adalah private method.")
    
    # Getter dan Setter untuk memanipulasi value gender
    def get_private_gender(self):
        return self.__private_gender
    
    def set_private_gender(self, gender):
        self.__private_gender = gender


biodata = Biodata("Riksan", 20)

# mengakses atribut publik
print(biodata.public_nama)

# mengakses atribut protected
print(biodata._protected_umur)

# mengakses atribut private
# akan menghasilkan AttributeError karena atribut private tidak dapat diakses secara langsung dari luar kelas
print(biodata.__private_gender) #Beri komentar saja biar tidak terjadi error

# memanggil metode publik
biodata.public_method()

# memanggil metode protected
biodata._protected_method()

# memanggil metode private menggunakan metode publik
biodata._Biodata__private_method()

# mengubah nilai atribut private menggunakan metode publik
biodata.set_private_gender("laki-laki")

# mendapatkan nilai atribut private menggunakan metode publik
print(biodata.get_private_gender())
