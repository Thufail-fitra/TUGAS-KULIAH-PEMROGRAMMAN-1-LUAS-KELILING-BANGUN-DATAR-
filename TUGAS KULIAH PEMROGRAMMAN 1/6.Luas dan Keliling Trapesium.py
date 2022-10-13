print("PROGRAM PYTHON MENGHITUNG LUAS TRAPESIUM")


# Diagonal_1  = float(input("\nMasukan Diagonal 1   : "))
# Diagonal_2 = float(input("Masukan Diagonal 2 : "))
tinggi = float(input("Masukan Tinggi TRAPESIUM : "))


sisi1 = float(input("Masukan sisi Atas TRAPESIUM: "))
sisi2 = float(input("Masukan sisi Bawah TRAPESIUM: "))
sisi3 = float(input("Masukan sisi kanan TRAPESIUM: "))
sisi4 = float(input("Masukan sisi Kiri TRAPESIUM: "))

keliling = sisi1 + sisi2 + sisi3 +sisi4
luas = (((sisi1 + sisi2)/2)*tinggi) 

Nama = 'Thufail Fitra'
print ("\nNAMA MAHASISWA \t\t\t= ",Nama)
print("\nLuas TRAPESIUM  \t\t= %0.2f" %  luas)
print("Keliling TRAPESIUM \t\t= ", keliling)