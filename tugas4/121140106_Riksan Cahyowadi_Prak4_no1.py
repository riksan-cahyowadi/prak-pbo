class Komputer:
    def __init__(self, nama, jenis, harga, merk):
        self.nama = nama
        self.jenis = jenis
        self.harga = harga
        self.merk = merk
        
    def get_spek(self):
        return f"{self.nama} {self.jenis} produksi {self.merk}"
        
class Processor(Komputer):
    def __init__(self, nama, jenis, harga, merk, jumlah_core, kecepatan_processor):
        super().__init__(nama, jenis, harga, merk)
        self.jumlah_core = jumlah_core
        self.kecepatan_processor = kecepatan_processor
        
class RAM(Komputer):
    def __init__(self, nama, jenis, harga, merk, kapasitas):
        super().__init__(nama, jenis, harga, merk)
        self.kapasitas = kapasitas
        
class HDD(Komputer):
    def __init__(self, nama, jenis, harga, merk, kapasitas, rpm):
        super().__init__(nama, jenis, harga, merk)
        self.kapasitas = kapasitas
        self.rpm = rpm
        
class VGA(Komputer):
    def __init__(self, nama, jenis, harga, merk, kapasitas):
        super().__init__(nama, jenis, harga, merk)
        self.kapasitas = kapasitas
        
class PSU(Komputer):
    def __init__(self, nama, jenis, harga, merk, daya):
        super().__init__(nama, jenis, harga, merk)
        self.daya = daya
        
   
p1 = Processor('Processor', 'Core i7 7740X', 4350000, 'Intel', 4, '4.3GHz')
p2 = Processor('Processor', 'Ryzen 5 3600', 250000, 'AMD', 4, '4.3GHz')
ram1 = RAM('RAM', 'DDR4 SODimm PC19200/2400MHz', 328000, 'V-Gen', '4GB')
ram2 = RAM('RAM', 'DDR4 2400MHz', 328000, 'G.SKILL', '4GB')
hdd1 = HDD('HDD', 'HDD 2.5 inch', 295000, 'Seagate', '500GB', 7200)
hdd2 = HDD('HDD', 'HDD 2.5 inch', 295000, 'Seagate', '1000GB', 7200)
vga1 = VGA('VGA', 'VGA GTX 1050', 250000, 'Asus', '2GB')
vga2 = VGA('VGA', '1060Ti', 250000, 'Asus', '8GB')
psu1 = PSU('PSU', 'Corsair V550', 250000, 'Corsair', '500W')
psu2 = PSU('PSU', 'Corsair V550', 250000, 'Corsair', '500W')

komputers = [
    [p1, ram1, hdd1, vga1, psu1],
    [p2, ram2, hdd2, vga2, psu2]
]

for i, komputer in enumerate(komputers):
    print(f"Komputer {i+1}")
    for hardware in komputer:
        print(hardware.get_spek())
    print()
