class Robot:
    nama = None
    health = None
    damage = None

    def __init__(self):
        self.jumlah_turn = 0
        self.nama = 0
        self.health = 0
        self.damage = 0

    # Digunakan untuk menghitung hasil eksekusi health robot
    def __sub__(self, value):
        self.health -= value.damage
        return self.health

    # Digunakan untuk memudahkan display informasi dan angka
    def __str__(self):
        return f"({self.nama}) menyerang! mengakibatkan {self.damage} DMG \nWin counter : "

    def lakukan_aksi(self, value):
        value.health -= self.damage
        return value.health


class Antares(Robot):
    def __init__(self):
        self.nama = "Antares"
        self.health = 50000
        self.damage = 5000

    def lakukan_aksi(self, value, turn):
        if turn % 3 == 0:
            self.damage *= 1.5
        elif turn % 3 == 1 and turn > 3:
            self.damage = 5000
        Robot.lakukan_aksi(self, value)


class Alphasetia(Robot):
    def __init__(self):
        self.nama = "Alphasetia"
        self.health = 40000
        self.damage = 6000

    def lakukan_aksi(self, value, turn):
        if turn % 2 == 0:
            self.health += 4000
        Robot.lakukan_aksi(self, value)


class Lecalicus(Robot):
    def __init__(self):
        self.nama = "Lecalicus"
        self.health = 45000
        self.damage = 5500

    def lakukan_aksi(self, value, turn):
        if turn % 4 == 0:
            self.health += 7000
            self.damage *= 2
        elif turn % 4 == 1 and turn > 4:
            self.damage = 5500
        Robot.lakukan_aksi(self, value)


print("==============Pertandingan robot Yamako akan segera dimulai !!!==============\nSilahkan pilih robot")
robot = int(input("Pilih my_robot (1 = Antares, 2 = Alphasetia, 3 = Lecalicus): "))
if robot == 1:
    my_robot = Antares()
elif robot == 2:
    my_robot = Alphasetia()
elif robot == 3:
    my_robot = Lecalicus()

robot = int(
    input("Pilih robot lawan (1 = Antares, 2 = Alphasetia, 3 = Lecalicus): "))
if robot == 1:
    opponent_robot = Antares()
elif robot == 2:
    opponent_robot = Alphasetia()
elif robot == 3:
    opponent_robot = Lecalicus()

print("\n==============Aturan main:==============\n pilih 1 untuk batu, 2 untuk kertas, dan 3 untuk gunting\n")

# Turn awal
turn = 1
your_wins = 0
opponent_wins = 0

while (True):
    print(
        f"Turn saat ini : {turn}")
    print(
        f"Robotmu ({my_robot.nama} - {my_robot.health} HP), Robot lawan ({opponent_robot.nama} - {opponent_robot.health} HP)")
    your_choice = int(input("Pilih tangan robotmu : "))
    opponent_choice= int(input("Pilih tangan robot lawan : "))

    if (your_choice == 1 and opponent_choice== 3) or (your_choice == 2 and opponent_choice== 1) or (your_choice == 3 and opponent_choice== 2):
        your_wins += 1
        my_robot.lakukan_aksi(opponent_robot, your_wins)
        print("my_robot", my_robot.__str__(), your_wins)

    elif (your_choice == 1 and opponent_choice== 2) or (your_choice == 2 and opponent_choice== 3) or (your_choice == 3 and opponent_choice== 1):
        opponent_wins += 1
        opponent_robot.lakukan_aksi(my_robot, opponent_wins)
        print("Robot lawan", opponent_robot.__str__(), opponent_wins)

    elif (your_choice == 1 and opponent_choice== 1) or (your_choice == 2 and opponent_choice== 2) or (your_choice == 3 and opponent_choice== 3):
        print("Hasil Seri, silahkan pilih ulang")

    print("\n")

    if my_robot.health <= 0 or opponent_robot.health <= 0:
        print(f"Jumlah turn yang dilakukan : {turn}")
        if my_robot.health > opponent_robot.health:
            print(f"(HP {opponent_robot.nama}) habis !!!\nLawan menyatakan kekalahan")
            print(
                f"\nPemenangnya adalah robotmu yaitu ({my_robot.nama})")
        else:
            print(f"HP ({my_robot.nama}) habis !!!\nKamu menyatakan kekalahan")
            print(
                f"\nPemenangnya adalah robot lawan yaitu ({opponent_robot.nama})")
        break
    turn += 1
