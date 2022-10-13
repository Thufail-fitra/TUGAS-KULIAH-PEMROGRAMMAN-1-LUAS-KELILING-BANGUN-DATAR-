print("PROGRAM PYTHON MENGHITUNG LUAS Belah Ketupat")


Diagonal_1  = float(input("\nMasukan Diagonal 1   : "))
Diagonal_2 = float(input("Masukan Diagonal 2 : "))

luas = 0.5* Diagonal_1 * Diagonal_2   

sisi1 = float(input("Masukan sisi 1 Belah Ketupat: "))
sisi2 = float(input("Masukan sisi 2 Belah Ketupat: "))
sisi3 = float(input("Masukan sisi 3 Belah Ketupat: "))
sisi4 = float(input("Masukan sisi 4 Belah Ketupat: "))

keliling = sisi1 + sisi2 + sisi3 +sisi4

Nama = 'Thufail Fitra'
print ("\nNAMA MAHASISWA \t\t\t= ",Nama)
print("\nLuas Belah Ketupat  \t\t= %0.2f" %  luas)
print("Keliling Belah Ketupat \t\t= ", keliling)