import matplotlib.pyplot as plt
import numpy as np

# Sadece DP'nin sonuç verebildiği N=100 ve N=1000 için elde ettiğimiz gerçek veriler
n_degerleri = ['N=100', 'N=1000']
dp_degerler = [4302, 41018]  # DP'nin bulduğu %100 kesin (optimum) sonuçlar
ga_degerler = [3670, 28215]  # GA'nın bulduğu yaklaşık sonuçlar

x = np.arange(len(n_degerleri))
genislik = 0.35

fig, ax = plt.subplots(figsize=(7, 5))

# Çubuk grafikleri oluşturma 
cubuk1 = ax.bar(x - genislik/2, dp_degerler, genislik, label='Dinamik Programlama (Kesin Sonuç)', color='#2a9d8f')
cubuk2 = ax.bar(x + genislik/2, ga_degerler, genislik, label='Genetik Algoritma (Yaklaşık Sonuç)', color='#f4a261')

# Çubukların tepe noktasına değerleri yazdıralım ki makalede okuması kolay olsun
for i, v in enumerate(dp_degerler):
    ax.text(i - genislik/2, v + 500, str(v), ha='center', va='bottom', fontweight='bold')
for i, v in enumerate(ga_degerler):
    ax.text(i + genislik/2, v + 500, str(v), ha='center', va='bottom', fontweight='bold')

# Eksen ve Başlık Ayarları
ax.set_ylabel('Bulunan Toplam Değer', fontweight='bold')
ax.set_title('Algoritmaların Çözüm Kalitesi (Accuracy Gap) Karşılaştırması', fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(n_degerleri, fontweight='bold')
ax.legend()

# Grafiği yüksek çözünürlüklü kaydet
plt.tight_layout()
plt.savefig('cozum_kalitesi.png', dpi=300)
print("İkinci grafik 'cozum_kalitesi.png' adıyla klasöre kaydedildi.")