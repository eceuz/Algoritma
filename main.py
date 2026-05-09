from veri_olusturma import esya_uret
from dp_cozumu import dp_ile_coz
from ga_cozumu import ga_ile_coz

def deneyleri_baslat():
    test_boyutlari = [100, 1000, 10000]

    print("=" * 60)
    print("KNAPSACK (SIRT ÇANTASI) ALGORİTMA KARŞILAŞTIRMASI")
    print("=" * 60)

    for n in test_boyutlari:
        print(f"\n>>> N = {n} İÇİN TEST BAŞLIYOR <<<")

        # 1. Aşama: Rastgele eşyaların ve çanta kapasitesinin üretilmesi
        # 'n' adet eşya üretilir ve kapasite, toplam ağırlığın %50'si olarak hesaplanır
        agirliklar, degerler, kapasite = esya_uret(n)

        print(f"Hesaplanan Çanta Kapasitesi: {kapasite}")

        # 2. Aşama: Dinamik Programlama (Kesin Çözüm) Çalıştırılması[cite: 1]
        print("\n[DP Çalışıyor...]")
        dp_sonuc, dp_sure = dp_ile_coz(agirliklar, degerler, kapasite)

        # DP'nin N=10000 gibi büyük değerlerde çökme (MemoryError) ihtimalinin kontrolü[cite: 1]
        if dp_sonuc is None:
            print("DP Sonuç: BELLEK YETERSİZ (MemoryError) - Algoritma patladı!")
        else:
            print(f"DP Sonuç: {dp_sonuc}")
            print(f"DP Süre: {dp_sure:.4f} sn")

        # 3. Aşama: Genetik Algoritma (Sezgisel Çözüm) Çalıştırılması[cite: 1]
        print("\n[GA Çalışıyor...]")
        
        ga_sonuc, ga_sure = ga_ile_coz(agirliklar, degerler, kapasite, populasyon_boyutu=100, jenerasyon_sayisi=100)

        print(f"GA Sonuç: {ga_sonuc}")
        print(f"GA Süre: {ga_sure:.4f} sn")

        # 4. Aşama: Performans ve Doğruluk Analizi
        # Karşılaştırma yapabilmek için DP'nin çökmemiş ve bir sonuç bulmuş olması gerekir
        if dp_sonuc is not None:
            
            # Doğruluk Oranı: GA'nın bulduğu sonucun, DP'nin bulduğu en iyi sonuca yüzdesel oranı
            accuracy = (ga_sonuc / dp_sonuc) * 100
            
            gap = (dp_sonuc - ga_sonuc) / dp_sonuc

            print(f"\n=> Analiz Sonuçları:")
            print(f"Accuracy (Doğruluk): %{accuracy:.2f}")
            print(f"Accuracy Gap (Doğruluk Sapması): {gap:.4f}")

            # Sürelere bakılarak hangi algoritmanın ne kadar daha hızlı olduğunun hesaplanması
            if ga_sure < dp_sure:
                print(f"Hız: GA, DP'den {(dp_sure/ga_sure):.2f} kat daha hızlı.")
            else:
                print(f"Hız: DP, GA'dan {(ga_sure/dp_sure):.2f} kat daha hızlı.")

        print("-" * 60)

if __name__ == '__main__':
    deneyleri_baslat()