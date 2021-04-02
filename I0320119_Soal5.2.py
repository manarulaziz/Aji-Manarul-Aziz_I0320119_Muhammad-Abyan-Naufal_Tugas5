print("Konversi Nilai ")

nama = input("Masukkan Nama Anda : ")
nilai = float(input("Masukkan nilai angka Anda : "))

if 85 <= nilai <= 100:
    print('Halo, ', nama, '! Nilai anda setelah dikonversi adalah A' )
elif 80 <= nilai <= 84:
    print('Halo, ', nama, '! Nilai anda setelah dikonversi adalah A-' )
elif 75 <= nilai <= 79:
    print('Halo, ', nama, '! Nilai anda setelah dikonversi adalah B+' )
elif 70 <= nilai <= 74:
    print('Halo, ', nama, '! Nilai anda setelah dikonversi adalah B' )
elif 65 <= nilai <= 69:
    print('Halo, ', nama, '! Nilai anda setelah dikonversi adalah C+' )
elif 60 <= nilai <= 64:
    print('Halo, ', nama, '! Nilai anda setelah dikonversi adalah C' )
elif nilai < 60:
    print('Halo, ', nama, '! Nilai anda setelah dikonversi adalah E' ) 
else:
    print('Nilai yang anda masukkan tidak valid untuk dikonversi')