import math
from scipy.stats import norm

# Diketahui
n = 200             # ukuran sampel
x_bar = 1.8         # rata-rata sampel
mu_0 = 2.0          # rata-rata hipotesis nol
sigma = 0.5         # standar deviasi
alpha = 0.05        # tingkat signifikansi

# (a) Hipotesis
print("Hipotesis:")
print("H0: μ ≥ 2 (waktu respon tidak kurang dari 2 detik)")
print("H1: μ < 2 (waktu respon kurang dari 2 detik)")

# (b) Hitung nilai statistik uji
z = (x_bar - mu_0) / (sigma / math.sqrt(n))
print(f"\n(b) Nilai statistik uji (z): {z:.2f}")

# (c) Nilai kritis dan p-value
z_kritis = norm.ppf(alpha)  # untuk uji satu sisi kiri
p_value = norm.cdf(z)

print(f"(c) Nilai z kritis: {z_kritis:.2f}")
print(f"    p-value       : {p_value:.8f}")

# (d) Kesimpulan
print("\n(d) Kesimpulan:")
if z < z_kritis:
    print("Tolak H0: Ada cukup bukti bahwa rata-rata waktu respon < 2 detik.")
else:
    print("Gagal tolak H0: Tidak ada cukup bukti bahwa rata-rata waktu respon < 2 detik.")
