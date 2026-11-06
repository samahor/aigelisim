def kelime_say(metin):
    sayac = {}
    for kelime in metin.lower().split():
        kelime = kelime.strip(",.!?;:\"'()[]{}")  # Noktalama işaretlerini temizle
        if kelime == "":
            continue
        sayac[kelime] = sayac.get(kelime, 0) + 1
    return sayac

metin = "Merhaba dünya! Merhaba Python. Python çok güzel, değil mi? Evet, çok güzel."
sonuc = kelime_say(metin)
print(sonuc)