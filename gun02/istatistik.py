def istatistik(sayilar):
    if len(sayilar)== 0:
        return "Liste boş olamaz."
    
    ortalama= sum(sayilar) / len(sayilar)
    en_buyuk= max(sayilar)
    en_kucuk= min(sayilar)
    return ortalama, en_buyuk, en_kucuk

ort, buyuk, kucuk = istatistik([10, 43, 21, -8, 3])
print("Ortalama:", ort)
print("En Büyük:", buyuk)
print("En Küçük:", kucuk)