import random
import time

def ga_ile_coz(agirliklar, degerler, kapasite, populasyon_boyutu=50, jenerasyon_sayisi=100, mutasyon_orani=0.1):
    """
    Genetik Algoritma ile 0/1 Knapsack problemini (yaklaşık olarak) çözer.
    """
    n = len(agirliklar)
    baslangic_zamani = time.perf_counter()

    # 1. Başlangıç Popülasyonunu Oluşturma (Rastgele 0 ve 1'lerden oluşan bireyler)
    populasyon = []
    for _ in range(populasyon_boyutu):
        birey = [random.choice([0, 1]) for _ in range(n)]
        populasyon.append(birey)

    # 2. Uygunluk (Fitness) Fonksiyonu: Çantanın değerini hesaplar
    def fitness(birey):
        toplam_agirlik = sum(birey[i] * agirliklar[i] for i in range(n))
        toplam_deger = sum(birey[i] * degerler[i] for i in range(n))
        
        if toplam_agirlik > kapasite:
            return 0  # Kapasite aşılırsa birey elenir (puanı 0 olur)
        return toplam_deger

    # 3. Evrim Döngüsü
    for jenerasyon in range(jenerasyon_sayisi):
        fitness_degerleri = [fitness(birey) for birey in populasyon]
        yeni_populasyon = []
        
        # Elitizm: En iyi bireyi doğrudan yeni nesle aktaralım ki kaybolmasın
        en_iyi_index = fitness_degerleri.index(max(fitness_degerleri))
        en_iyi_birey = populasyon[en_iyi_index]
        yeni_populasyon.append(en_iyi_birey)

        # Yeni bireyleri üretme
        while len(yeni_populasyon) < populasyon_boyutu:
            # Seçim (Turnuva Seçimi - Rastgele iki kişi seçip iyisini alıyoruz)
            rakip1 = random.randint(0, populasyon_boyutu - 1)
            rakip2 = random.randint(0, populasyon_boyutu - 1)
            ebeveyn1 = populasyon[rakip1] if fitness_degerleri[rakip1] > fitness_degerleri[rakip2] else populasyon[rakip2]

            rakip1 = random.randint(0, populasyon_boyutu - 1)
            rakip2 = random.randint(0, populasyon_boyutu - 1)
            ebeveyn2 = populasyon[rakip1] if fitness_degerleri[rakip1] > fitness_degerleri[rakip2] else populasyon[rakip2]

            # Çaprazlama (Crossover - Ebeveynleri ortadan bölüp birleştiriyoruz)
            kesim_noktasi = random.randint(1, n - 1) if n > 1 else 1
            cocuk = ebeveyn1[:kesim_noktasi] + ebeveyn2[kesim_noktasi:]

            # Mutasyon (Ufak bir ihtimalle genleri değiştiriyoruz)
            for i in range(n):
                if random.random() < mutasyon_orani:
                    cocuk[i] = 1 - cocuk[i] # 0 ise 1, 1 ise 0 yap
            
            yeni_populasyon.append(cocuk)
        
        populasyon = yeni_populasyon

    # Son durumdaki en iyi bireyi bulma
    son_fitness_degerleri = [fitness(birey) for birey in populasyon]
    en_iyi_sonuc = max(son_fitness_degerleri)
    
    bitis_zamani = time.perf_counter()
    gecen_sure = bitis_zamani - baslangic_zamani
    
    return en_iyi_sonuc, gecen_sure

# Test Bloğu
if __name__ == '__main__':
    print("GA Algoritması test ediliyor...")
    test_agirliklar = [10, 20, 30]
    test_degerler = [60, 100, 120]
    test_kapasite = 50
    
    en_iyi_deger, sure = ga_ile_coz(test_agirliklar, test_degerler, test_kapasite)
    print(f"Bulunan En İyi Değer: {en_iyi_deger}")
    print(f"Çözüm Süresi: {sure:.6f} saniye")