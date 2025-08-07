import random

print("Zar atmak icin 1 e basin.")

cevap = int(input())

if cevap == 1:
    print("Zariniz atiliyor.")
else:
    print("Lutfen dogru sayiyi giriniz.")

kullanici_zari = random.randint(1, 6)
bilgisayar_zari = random.randint(1, 6)

print(f"Kullanici zar atisi: {kullanici_zari}")
print(f"Bilgisasyar zar atisi: {bilgisayar_zari}")

if kullanici_zari > bilgisayar_zari:
    print("Kazandiniz!")
else:
    print("Kaybettiniz!")