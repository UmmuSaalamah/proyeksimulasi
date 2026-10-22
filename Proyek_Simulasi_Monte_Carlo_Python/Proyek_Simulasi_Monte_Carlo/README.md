# Simulasi Monte Carlo: Proses Pencucian

## Deskripsi
Proyek ini memperkirakan jumlah proses pencucian komponen yang dapat diselesaikan dalam waktu kerja 8 jam ketika durasi tiap tahap berubah-ubah.

## Masalah ketidakpastian
Durasi pengisian air, pencucian, pembilasan, dan pengeringan tidak selalu sama. Karena itu, jumlah proses yang selesai dalam satu hari juga dapat berubah.

## Metode dan pemodelan
Metode yang digunakan adalah Monte Carlo. Setiap percobaan mengambil durasi acak untuk empat tahap proses, menjumlahkannya, lalu mengulangi proses selama total waktu tidak melebihi 480 menit. Percobaan diulang sebanyak 5.000 kali.

## Sumber data dan asumsi
Belum menggunakan data operasional nyata. Rentang durasi berikut adalah data asumsi untuk demonstrasi dan perlu diganti jika data lapangan tersedia:
- Isi air: uniform 4–8 menit
- Pencucian: triangular 12, 16, 20 menit (minimum, nilai paling mungkin, maksimum)
- Pembilasan: uniform 5–9 menit
- Pengeringan: uniform 6–12 menit

Workbook referensi yang diberikan untuk tugas mencakup `988 Washers Simulation`, yang membahas simulasi Monte Carlo proses pencucian. Angka dalam program ini adalah asumsi ilustratif, bukan salinan hasil workbook.

## Bahasa dan tools
- Python
- NumPy untuk sampling acak
- Pandas untuk tabel dan ekspor CSV
- Matplotlib untuk grafik

## Cara menjalankan
1. Instal Python 3.
2. Jalankan `pip install numpy pandas matplotlib`.
3. Jalankan `python simulasi_monte_carlo.py`.
4. Program menampilkan ringkasan, menyimpan `hasil_simulasi.csv`, dan menghasilkan `distribusi_hasil.png`.

## Hasil demonstrasi
Dengan seed 42 dan 5.000 percobaan, rata-rata hasil sekitar 12.08 proses per 8 jam. Hasil bisa berbeda jika asumsi durasi atau seed diubah. Ini adalah hasil model, bukan jaminan kapasitas aktual.

## Keterlibatan AI dan bukti
Isi persentase berdasarkan kontribusi aktual. Contoh format deklarasi (jangan digunakan tanpa verifikasi):
- AI: [isi persentase aktual, maksimal sesuai ketentuan dosen]
- Pekerjaan mandiri: [sisa persentase]
- Penggunaan AI: membantu menyusun kerangka penjelasan dan/atau debugging.
- Bukti: simpan riwayat prompt yang relevan, commit GitHub, perubahan kode yang dibuat sendiri, dan catatan pengujian. Jangan mengklaim persentase yang tidak dapat dibuktikan.

## Pelaporan GitHub
Unggah kode, README, grafik, dan contoh CSV. Gunakan commit bertahap dengan pesan jelas, misalnya `buat model awal`, `tambah ekspor hasil`, dan `rapikan dokumentasi`. Commit harus mencerminkan pekerjaan yang benar-benar dilakukan.
