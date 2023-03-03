print("Soal 1")

n = int(input("Masukkan n: "))

for i in range(n):
    print("*" * n)

print("\nSoal 2")
for i in range(3):
    username = str(input("Username anda : "))
    password = int(input("Password anda : "))

    if username == "informatika" and password == 12345678:
        print("Berhasil login!")
        break
    elif i == 2:
        print("Akun anda terblokir!")
    else:
        print("Username atau password anda salah Coba lagi")
