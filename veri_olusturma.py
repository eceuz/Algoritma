import random

def esya_uret(esya_sayisi, max_agirlik=100, max_deger=100):
    """
    Belirtilen sayıda rastgele eşya (ağırlık ve değer) üretir.
    Çanta kapasitesini toplam ağırlığın %50'si olarak belirler.
    """
    agirliklar = [random.randint(1, max_agirlik) for _ in range(esya_sayisi)]
    degerler = [random.randint(1, max_deger) for _ in range(esya_sayisi)]
    
    # Çantanın kapasitesini, tüm eşyaların toplam ağırlığının yarısı kadar yapıyoruz
    kapasite = int(sum(agirliklar) * 0.5)
    
    return agirliklar, degerler, kapasite

# Test Bloğu: Bu dosya doğrudan çalıştırıldığında burası devreye girer.
# Başka bir dosyadan çağrıldığında (import edildiğinde) sessizce bekler.
if __name__ == '__main__':
    print("Veri üretici test ediliyor...")
    test_agirliklar, test_degerler, test_kapasite = esya_uret(5)
    
    print(f"Eşya Ağırlıkları: {test_agirliklar}")
    print(f"Eşya Değerleri: {test_degerler}")
    print(f"Çanta Kapasitesi: {test_kapasite}")