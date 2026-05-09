import numpy as np
import time

def dp_ile_coz(agirliklar, degerler, kapasite):
    """
    Dinamik Programlama ile 0/1 Knapsack problemini çözer.
    Kesin ve en iyi sonucu garanti eder.
    """
    n = len(agirliklar)
    
    try:
        # Bellek hatasını (MemoryError) yakalamak için try-except kullanıyoruz.
        dp_tablosu = np.zeros((n + 1, kapasite + 1), dtype=np.int32)
        
        baslangic_zamani = time.perf_counter()
        
        for i in range(1, n + 1):
            for w in range(1, kapasite + 1):
                if agirliklar[i-1] <= w:
                    dp_tablosu[i][w] = max(degerler[i-1] + dp_tablosu[i-1][w-agirliklar[i-1]], dp_tablosu[i-1][w])
                else:
                    dp_tablosu[i][w] = dp_tablosu[i-1][w]
                    
        bitis_zamani = time.perf_counter()
        gecen_sure = bitis_zamani - baslangic_zamani
        
        return dp_tablosu[n][kapasite], gecen_sure
        
    except MemoryError:
        return None, -1

# Test Bloğu
if __name__ == '__main__':
    print("DP Algoritması test ediliyor...")
    # Basit bir test verisi 
    test_agirliklar = [10, 20, 30]
    test_degerler = [60, 100, 120]
    test_kapasite = 50
    
    en_iyi_deger, sure = dp_ile_coz(test_agirliklar, test_degerler, test_kapasite)
    print(f"Bulunan En İyi Değer: {en_iyi_deger}")
    print(f"Çözüm Süresi: {sure:.6f} saniye")