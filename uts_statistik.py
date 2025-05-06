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
