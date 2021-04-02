print("======== Hotel Cirebon ========")
print("------ Bersih Indah Asri ------")

nama = input("\nMasukkan Nama Anda : ")
umur = int(input("Masukkan Umur Anda : "))
print("Jenis Kelamin: [L/P] ")
gender = input().upper()
if gender == "L" and umur > 40:
    print("Selamat Datang di Hotel Cirebon Tuan", nama)
elif gender == "P" and umur > 40:
    print("Selamat Datang di Hotel Cirebon Nyonya", nama)
elif gender == "L" and 30 < umur <= 40:
    print("Selamat Datang di Hotel Cirebon Bapak ", nama)
elif gender == "P" and 30 < umur <= 40:
    print("Selamat Datang di Hotel Cirebon Ibu ", nama)
elif gender == "L" and  21 <= umur <= 30:
    print("Selamat Datang di Hotel Cirebon Bro ", nama)
elif gender == "P" and 21 <= umur <= 30:
    print("Selamat Datang di Hotel Cirebon Sist ", nama)
elif gender == "L " and umur < 21:
    print("Halo Adik", nama, "Mohon maaf kamu tidak bisa memesan hotel.")
elif gender == "P " and umur < 21:
    print("Halo Adik", nama, "Mohon maaf kamu tidak bisa memesan hotel.")
else:
    print("\n" * 100)
