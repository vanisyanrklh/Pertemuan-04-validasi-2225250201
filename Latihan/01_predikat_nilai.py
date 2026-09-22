# Program menentukan predikat nilai mahasiswa
# Algoritma dan Pemrograman | S1 Pendidikan Matematika FKIP Untirta | 2026/2027 Ganjil

# Input nilai akhir
nilai = float(input("Nilai akhir (0-100): "))

# Seleksi kondisi untuk predikat
if nilai >= 85:
    predikat = "A"
elif nilai >= 70:
    predikat = "B"
elif nilai >= 60:
    predikat = "C"
elif nilai >= 50:
    predikat = "D"
else:
    predikat = "E"

# Output hasil
print(f"Nilai {nilai:.2f} memperoleh predikat {predikat}.")
