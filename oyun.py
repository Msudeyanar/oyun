import random

def play_game():
    print("Taş Kağıt Makas oyununa hoş geldiniz! İyi eğlenceler.")
    print("Kurallar çok basit:")
    print("1. Taş, makası yener.")
    print("2. Makas, kağıdı yener.")
    print("3. Kağıt, taşı yener.")
    print("Oyun 3 oyundan oluşur.")
    print("İki oyunu kazanan galip gelir.")
    print("Her oyunda, 2 oyunu kazanan galip gelir.\n")
    
    oyuncu_adı = input("Adınızı ve soyadınızı girin: ").upper()
    
    oyuna_başla = input("Oyunu oynamak ister misiniz? (evet/hayır): ").lower()
    if oyuna_başla == "hayır":
        print("Oyun sonlandırıldı çabuk pes ettin!")
        return

    seçenekler = ["taş", "kağıt", "makas"]
    oyuncu_toplam_kazanma = 0
    bilgisayar_toplam_kazanma = 0

    while True:
        oyuncu_skoru = 0
        bilgisayar_skoru = 0

        while oyuncu_skoru < 2 and bilgisayar_skoru < 2:
            oyuncu_seçimi = input(f"{oyuncu_adı}, Taş, Kağıt veya Makas seçin: ").lower()
            if oyuncu_seçimi not in seçenekler:
                print("Geçersiz seçim. Lütfen tekrar deneyin.")
                continue

            bilgisayar_seçimi = random.choice(seçenekler)
            print(f"Bilgisayarın seçimi: {bilgisayar_seçimi}")

            if oyuncu_seçimi == bilgisayar_seçimi:
                print("Beraberlik!")
            elif (oyuncu_seçimi == "taş" and bilgisayar_seçimi == "makas") or \
                 (oyuncu_seçimi == "kağıt" and bilgisayar_seçimi == "taş") or \
                 (oyuncu_seçimi == "makas" and bilgisayar_seçimi == "kağıt"):
                oyuncu_skoru += 1
                print(f"{oyuncu_adı} bu turu kazandı!")
            else:
                bilgisayar_skoru += 1
                print("Bilgisayar bu turu kazandı!")

            print(f"Skor: {oyuncu_adı}:{oyuncu_skoru} - Bilgisayar: {bilgisayar_skoru}")

        if oyuncu_skoru == 2:
            print(f"Tebrikler {oyuncu_adı}, oyunu kazandınız!")
            oyuncu_toplam_kazanma += 1
        else:
            print(f"Üzgünüm {oyuncu_adı}, oyunu bilgisayar kazandı!")
            bilgisayar_toplam_kazanma += 1

        print(f"Toplam Skor: {oyuncu_adı} {oyuncu_toplam_kazanma} - Bilgisayar {bilgisayar_toplam_kazanma}")

        tekrar_oyna = input("Tekrar oynamak ister misiniz? (evet/hayır): ").lower()

        bilgisayar_tekrar_oynamak = random.choice(["evet", "hayır"])
        print(f"Bilgisayar tekrar oynamak istiyor mu? {bilgisayar_tekrar_oynamak.capitalize()}")

        if tekrar_oyna != "evet" or bilgisayar_tekrar_oynamak != "evet":
            print("Oyun bitti. Teşekkürler!")
            break

play_game()
    