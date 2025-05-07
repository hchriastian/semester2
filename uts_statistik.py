import pandas as pd
import numpy as np
from scipy import stats

# Load data
df = pd.read_csv('dataset_cancer_paru.csv')

# Pilih kolom numerik
kolom_numerik = df.select_dtypes(include=[np.number]).columns.tolist()

# Fungsi analisis pemusatan data
def analisis_pemusatan(df, kolom):
    hasil = []
    for kol in kolom:
        data = df[kol].dropna()
        mean = np.mean(data)
        median = np.median(data)
        mode = stats.mode(data, keepdims=True)[0][0]
        hasil.append({
            'Variabel': kol,
            'Mean': round(mean, 2),
            'Median': round(median, 2),
            'Modus': mode
        })
    return pd.DataFrame(hasil)
   
# Jalankan analisis dan tampilkan hasil
hasil_analisis = analisis_pemusatan(df, kolom_numerik)
print(hasil_analisis)

# Fungsi analisis penyebaran data
def analisis_penyebaran(df, kolom):
    hasil = []
    for kol in kolom:
        data = df[kol].dropna()
        std_dev = np.std(data, ddof=1)
        variance = np.var(data, ddof=1)
        range_data = np.ptp(data)
        hasil.append({
            'Variabel': kol,
            'Standar Deviasi': round(std_dev, 2),
            'Varians': round(variance, 2),
            'Range': round(range_data, 2)
        })
    return pd.DataFrame(hasil)

# Jalankan analisis penyebaran dan tampilkan hasil
hasil_penyebaran = analisis_penyebaran(df, kolom_numerik)
print(hasil_penyebaran)

# Fungsi analisis pendugaan parameter rata-rata
def analisis_pendugaan_rata_rata(df, kolom, alpha=0.01):
    hasil = []
    z_score = stats.norm.ppf(1 - alpha / 2)  # Z-score untuk tingkat signifikan
    for kol in kolom:
        data = df[kol].dropna()
        mean = np.mean(data)
        std_dev = np.std(data, ddof=1)
        n = len(data)
        margin_of_error = z_score * (std_dev / np.sqrt(n))
        lower_bound = mean - margin_of_error
        upper_bound = mean + margin_of_error
        hasil.append({
            'Variabel': kol,
            'Rata-rata': round(mean, 2),
            'Batas Bawah': round(lower_bound, 2),
            'Batas Atas': round(upper_bound, 2)
        })
    return pd.DataFrame(hasil)

# Jalankan analisis pendugaan rata-rata dan tampilkan hasil
hasil_pendugaan = analisis_pendugaan_rata_rata(df, kolom_numerik)
print(hasil_pendugaan)