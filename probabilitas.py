from scipy.stats import norm

# Diketahui
mu = 200      # mean (rata-rata) dalam milidetik
sigma = 50    # standar deviasi dalam milidetik

# (a) Probabilitas waktu respons kurang dari 250 milidetik
x_a = 250
prob_a = norm.cdf(x_a, loc=mu, scale=sigma)

# (b) Probabilitas waktu respons antara 200 dan 270 milidetik
x_b1 = 200
x_b2 = 270
prob_b = norm.cdf(x_b2, loc=mu, scale=sigma) - norm.cdf(x_b1, loc=mu, scale=sigma)

print(f"(a) Probabilitas waktu respons kurang dari {x_a} ms: {prob_a:.4f} ({prob_a*100:.2f}%)")
print(f"(b) Probabilitas waktu respons antara {x_b1} ms dan {x_b2} ms: {prob_b:.4f} ({prob_b*100:.2f}%)")
