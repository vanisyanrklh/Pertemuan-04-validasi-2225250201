# Program menentukan jenis bilangan bulat
# Algoritma dan Pemrograman | S1 Pendidikan Matematika FKIP Untirta | 2026/2027 Ganjil

# Input bilangan bulat
x = int(input("Masukkan bilangan bulat: "))

# Seleksi kondisi
if x < 0:
    print("Bilangan negatif")
elif x == 0:
    print("Nol")
elif x % 2 == 0:
    print("Bilangan positif genap")
else:
    print("Bilangan positif ganjil")
