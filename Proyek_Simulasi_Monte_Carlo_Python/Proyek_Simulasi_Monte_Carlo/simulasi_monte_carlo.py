"""
Simulasi Monte Carlo: jumlah proses pencucian komponen dalam 8 jam.
Catatan: seluruh durasi di bawah adalah DATA ASUMSI untuk demonstrasi,
bukan data operasional pabrik.
Jalankan: python simulasi_monte_carlo.py
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

SEED = 42
JUMLAH_SIMULASI = 5000
JAM_KERJA_MENIT = 8 * 60
rng = np.random.default_rng(SEED)

hasil = []
for simulasi in range(1, JUMLAH_SIMULASI + 1):
    waktu_terpakai = 0
    jumlah_proses = 0

    while True:
        # Durasi asumsi dalam menit:
        isi_air = rng.uniform(4, 8)
        pencucian = rng.triangular(12, 16, 20)
        pembilasan = rng.uniform(5, 9)
        pengeringan = rng.uniform(6, 12)
        durasi_total = isi_air + pencucian + pembilasan + pengeringan

        if waktu_terpakai + durasi_total > JAM_KERJA_MENIT:
            break
        waktu_terpakai += durasi_total
        jumlah_proses += 1

    hasil.append({
        "simulasi": simulasi,
        "jumlah_proses": jumlah_proses,
        "waktu_terpakai_menit": round(waktu_terpakai, 2)
    })

df = pd.DataFrame(hasil)
df.to_csv("hasil_simulasi.csv", index=False)

print("RINGKASAN HASIL SIMULASI")
print(f"Jumlah simulasi: {JUMLAH_SIMULASI}")
print(f"Rata-rata proses per 8 jam: {df['jumlah_proses'].mean():.2f}")
print(f"Median proses: {df['jumlah_proses'].median():.0f}")
print(f"Persentil ke-10: {df['jumlah_proses'].quantile(0.10):.0f}")
print(f"Persentil ke-90: {df['jumlah_proses'].quantile(0.90):.0f}")
print(f"Peluang minimal 30 proses: {(df['jumlah_proses'] >= 30).mean()*100:.2f}%")

plt.figure(figsize=(8, 5))
plt.hist(df["jumlah_proses"], bins=range(
    int(df["jumlah_proses"].min()), int(df["jumlah_proses"].max()) + 2
), edgecolor="black")
plt.title("Distribusi Jumlah Proses Pencucian per 8 Jam")
plt.xlabel("Jumlah proses pencucian")
plt.ylabel("Frekuensi simulasi")
plt.tight_layout()
plt.savefig("distribusi_hasil.png", dpi=150)
plt.show()
