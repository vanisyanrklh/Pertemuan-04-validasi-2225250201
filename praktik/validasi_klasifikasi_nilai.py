# Program Validasi dan Klasifikasi Nilai Akhir
# Algoritma dan Pemrograman | S1 Pendidikan Matematika FKIP Untirta | 2026/2027 Ganjil

print("Validasi dan Klasifikasi Nilai Akhir")

# Input nilai ujian, tugas, dan kehadiran
teks_ujian = input("Nilai ujian (0-100): ").strip()
teks_tugas = input("Nilai tugas (0-100): ").strip()
teks_hadir = input("Kehadiran persen (0-100): ").strip()

try:
    ujian = float(teks_ujian)
    tugas = float(teks_tugas)
    hadir = float(teks_hadir)
except ValueError:
    print("Masukan ditolak: seluruh data harus berupa angka.")
else:
    if not (0 <= ujian <= 100):
        print("Masukan ditolak: nilai ujian di luar rentang 0 sampai 100.")
    elif not (0 <= tugas <= 100):
        print("Masukan ditolak: nilai tugas di luar rentang 0 sampai 100.")
    elif not (0 <= hadir <= 100):
        print("Masukan ditolak: kehadiran di luar rentang 0 sampai 100.")
    else:
        # Hitung nilai akhir dengan bobot 60% ujian dan 40% tugas
        akhir = 0.6 * ujian + 0.4 * tugas
        print(f"Nilai akhir = {akhir:.2f}")
