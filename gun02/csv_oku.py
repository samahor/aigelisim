import csv

toplam_gram = 0
toplam_sure = 0

with open("gun02/baskilar.csv", encoding="utf-8") as dosya:
    okuyucu = csv.DictReader(dosya)

    for satir in okuyucu:
        gram = int(satir["gram"])
        sure = int(satir["sure_dk"])

        print(f"{satir['parca']}: {gram} g {satir['malzeme']}, {sure} dakika")

        toplam_gram += gram
        toplam_sure += sure
print("-" * 40)
print(f"Toplam filament: {toplam_gram} g")
print(f"Toplam süre: {toplam_sure} dakika ({toplam_sure / 60:.1f} saat)")