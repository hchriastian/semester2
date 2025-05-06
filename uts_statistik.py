import pandas as pd
import numpy as np
from scipy import stats

# Load dataset
file_path = 'iot_agr_2024.csv'  # Ganti path jika file berada di lokasi berbeda
df = pd.read_csv(file_path)

# Kolom yang akan dianalisis
kolom_analisis = ['tempreature', 'humidity', 'water_level', 'N', 'P', 'K']

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

# Jalankan analisis
hasil_analisis = analisis_pemusatan(df, kolom_analisis)

# Tampilkan hasil
print("Analisis Pemusatan Data:")
print(hasil_analisis)
