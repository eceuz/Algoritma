import matplotlib.pyplot as plt
import numpy as np

# Deneyden elde ettiğimiz gerçek süre verileri
n_degerleri = ['N=100', 'N=1000', 'N=10000']
dp_sureleri = [0.1142, 13.2931, 0] # N=10000'de çöktüğü için 0 verdik
ga_sureleri = [0.1638, 1.4138, 14.3506]

x = np.arange(len(n_degerleri))
genislik = 0.35

fig, ax = plt.subplots(figsize=(8, 5))

# Çubuk grafikleri (Bar chart) oluşturma
cubuk1 = ax.bar(x - genislik/2, dp_sureleri, genislik, label='Dinamik Programlama (DP)', color='#e63946')
cubuk2 = ax.bar(x + genislik/2, ga_sureleri, genislik, label='Genetik Algoritma (GA)', color='#457b9d')

ax.text(2 - genislik/2, 0.5, 'Memory\nError', ha='center', va='bottom', color='red', fontweight='bold')

# Eksen ve Başlık Ayarları
ax.set_ylabel('Çalışma Süresi (Saniye)', fontweight='bold')
ax.set_title('Sırt Çantası Probleminde Zaman Karmaşıklığı Karşılaştırması', fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(n_degerleri, fontweight='bold')
ax.legend()

# Grafiği kaydet
plt.tight_layout()
plt.savefig('sure_karsilastirmasi.png', dpi=300) 
print("Harika! Grafik 'sure_karsilastirmasi.png' adıyla klasöre kaydedildi.")