# Pertemuan 04 Seleksi Multi-Kondisi dan Validasi Input
Nama: vanisya Nur Khalimah
NIM: 2225250201
Kelas: 3B 

## Tujuan
Membangun program validasi dan klasifikasi nilai menggunakan rantai seleksi `if-elif-else` pada bahasa Python.

## Cara Menjalankan
Jalankan perintah berikut pada terminal di VS Code:

```bash
python3 praktik/validasi_klasifikasi_nilai.py

from tabulate import tabulate

## Tabel Keputusan
tabel_keputusan = [
    ["Tidak Valid", "Nilai < 0 atau Nilai > 100 (atau bukan angka)", "-10, 105, abc"],
    ["Sangat Memuaskan (A)", "85 <= Nilai <= 100", "90"],
    ["Memuaskan (B)", "70 <= Nilai < 85", "78"],
    ["Cukup (C)", "55 <= Nilai < 70", "62"],
    ["Kurang (D)", "40 <= Nilai < 55", "45"],
    ["Gagal (E)", "0 <= Nilai < 40", "25"],
]

headers_keputusan = ["Kategori", "Syarat Validasi / Nilai", "Contoh Masukan"]

# 2. Tabel Hasil Pengujian
tabel_pengujian = [
    [1, "92", "Kategori: Sangat Memuaskan (A)", "Kategori: Sangat Memuaskan (A)", "Lulus"],
    [2, "75", "Kategori: Memuaskan (B)", "Kategori: Memuaskan (B)", "Lulus"],
    [3, "60", "Kategori: Cukup (C)", "Kategori: Cukup (C)", "Lulus"],
    [4, "48", "Kategori: Kurang (D)", "Kategori: Kurang (D)", "Lulus"],
    [5, "30", "Kategori: Gagal (E)", "Kategori: Gagal (E)", "Lulus"],
    [6, "-5", "Error: Nilai harus berada dalam rentang 0 - 100", "Error: Nilai harus berada dalam rentang 0 - 100", "Lulus"],
    [7, "110", "Error: Nilai harus berada dalam rentang 0 - 100", "Error: Nilai harus berada dalam rentang 0 - 100", "Lulus"],
    [8, "xyz", "Error: Masukan harus berupa angka", "Error: Masukan harus berupa angka", "Lulus"],
]

headers_pengujian = ["No", "Masukan", "Keluaran Diharapkan", "Keluaran Aktual", "Status"]

print("=== TABEL KEPUTUSAN ===")
print(tabulate(tabel_keputusan, headers=headers_keputusan, tablefmt="github"))

print("\n=== TABEL HASIL PENGUJIAN ===")
print(tabulate(tabel_pengujian, headers=headers_pengujian, tablefmt="github"))

## Refleksi

Satu masukan tidak valid yang semula terlewat adalah **input berupa huruf, teks kosong, atau spasi tambahan yang tidak disengaja** (misalnya mengetik `"A"`, `" 80 "`, atau sekadar menekan Enter tanpa memasukkan angka).

**Masalah:**
Jika program hanya mengandalkan pengecekan rentang angka (`if nilai < 0 or nilai > 100:`), program akan langsung *crash* (berhenti paksa) dan memunculkan pesan error `ValueError`. Hal ini terjadi karena program tidak bisa mengubah karakter alfabet atau teks kosong menjadi tipe data angka desimal (*float*).

**Cara menanganinya:**
Saya melakukan dua perbaikan pada kode program:
1. Menambahkan fungsi `.strip()` pada perintah input untuk secara otomatis menghapus spasi awal dan akhir yang tidak disengaja.
2. Membungkus proses konversi teks ke angka menggunakan blok **`try-except ValueError`**. 

Dengan metode ini, saat program menerima masukan huruf, program tidak lagi *crash*. Error tersebut berhasil ditangkap oleh `except` dan program merespons dengan menampilkan peringatan *"Masukan ditolak: seluruh data harus berupa angka."* secara elegan.