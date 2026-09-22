# Program menentukan jenis segitiga berdasarkan sudut
# Algoritma dan Pemrograman | S1 Pendidikan Matematika FKIP Untirta | 2026/2027 Ganjil

# Input sudut segitiga
a = float(input("Sudut A: "))
b = float(input("Sudut B: "))
c = float(input("Sudut C: "))

# Validasi masukan
if a <= 0 or b <= 0 or c <= 0:
    print("Masukan ditolak: setiap sudut harus lebih dari 0 derajat.")
elif abs(a + b + c - 180) > 1e-9:
    print("Masukan ditolak: jumlah ketiga sudut harus 180 derajat.")
else:
    # Tentukan jenis segitiga berdasarkan sudut terbesar
    terbesar = max(a, b, c)
    if terbesar > 90:
        print("Segitiga tumpul")
    elif terbesar == 90:
        print("Segitiga siku-siku")
    else:
        print("Segitiga lancip")
