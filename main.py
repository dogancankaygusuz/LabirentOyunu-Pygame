import pygame
import random
import os
import json

GENİSLİK, YUKSEKLIK = 800, 600
KARE_BOYUT = 75

WHITE = (255, 255, 255)
oyuncu_poz = [1, 1]

levels = [
    [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 3, 1, 0, 2, 1],
        [1, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 3, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
    ],
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 3, 0, 2, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 1],
        [1, 3, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
    ],
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 3, 0, 1, 0, 0, 2, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 1],
        [1, 0, 0, 0, 3, 1, 0, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1],
    ],
    [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 3, 0, 0, 0, 1, 1],
        [1, 0, 1, 1, 1, 3, 1, 1],
        [1, 3, 1, 1, 1, 0, 2, 1],
        [1, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
    ],
    [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 3, 0, 1],
        [1, 1, 1, 0, 1, 1, 1],
        [1, 0, 3, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 2, 1],
    ],
    [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 3, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 3, 0, 0, 1],
        [1, 0, 1, 2, 1, 1, 0, 1],
        [1, 3, 1, 1, 1, 1, 2, 1],
    ],
    [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 3, 0, 0, 1],
        [1, 1, 1, 1, 1, 3, 1],
        [1, 3, 0, 1, 0, 0, 1],
        [1, 3, 0, 0, 0, 2, 1],
        [1, 1, 1, 1, 1, 1, 1],
    ],
    [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 3, 0, 0, 3, 1],
        [1, 1, 1, 0, 1, 1, 1, 1],
        [1, 3, 0, 0, 0, 3, 0, 1],
        [1, 0, 0, 1, 0, 0, 1, 1],
        [1, 1, 2, 1, 1, 1, 1, 1],
    ],
    [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 0, 3, 0, 0, 2, 1],
        [1, 1, 1, 1, 0, 1, 1],
        [1, 0, 0, 0, 3, 0, 1],
        [1, 1, 1, 1, 1, 1, 1],
    ],
    [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 3, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1],
        [1, 2, 3, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
    ],
]

mevcut_level = 0
labirent = levels[mevcut_level]
envanter = {"enerji": 0, "materyal": 0}
mesaj = ""
kullanici_input = ""
input_active = False
bulmaca_active = False
bulmaca_cevap = ""


DUVAR_ICON = pygame.image.load("icon\duvar.svg")
KAPI_ICON = pygame.image.load("icon\door.svg")
KAYNAK_ICON = pygame.image.load("icon\coin.svg")
OYUNCU_ICON = pygame.image.load("icon\\ronaldo.png")
ARKA_PLAN_ICON = pygame.image.load("icon\\bg.jpg")
DOGRU_ICON = pygame.image.load("icon\correct24.svg")
YANLIS_ICON = pygame.image.load("icon\\no.svg")
KUPA_ICON = pygame.image.load("icon\\bestscore.png")


DUVAR_ICON = pygame.transform.scale(DUVAR_ICON, (KARE_BOYUT, KARE_BOYUT))
KAPI_ICON = pygame.transform.scale(KAPI_ICON, (int(KAPI_ICON.get_width() * 0.15), int(KAPI_ICON.get_height() * 0.15)))
KAYNAK_ICON = pygame.transform.scale(KAYNAK_ICON,(int(KAYNAK_ICON.get_width() * 0.15), int(KAYNAK_ICON.get_height() * 0.15)))
OYUNCU_ICON = pygame.transform.scale(OYUNCU_ICON, (KARE_BOYUT, KARE_BOYUT))
ARKA_PLAN_ICON = pygame.transform.scale(ARKA_PLAN_ICON, (GENİSLİK, YUKSEKLIK))
DOGRU_ICON = pygame.transform.scale(DOGRU_ICON, (50, 50))
YANLIS_ICON = pygame.transform.scale(YANLIS_ICON, (50, 50))
KUPA_ICON = pygame.transform.scale(KUPA_ICON, (50, 50))

pygame.font.init()
FONT = pygame.font.Font(None, 36)


def metin_yaz(ekran, metin, x, y, color=WHITE):
    metin_font = FONT.render(metin, True, color)
    ekran.blit(metin_font, (x, y))


def bulmaca_çöz():
    soru_tipleri = ["mat", "mat1", "mantık"]
    secilen_soru_tipi = random.choice(soru_tipleri)

    if secilen_soru_tipi == "mat":
        num1, num2 = random.randint(1, 10), random.randint(1, 10)
        return f"Soru: {num1} + {num2} = ?", str(num1 + num2)

    elif secilen_soru_tipi == "mat1":
        num1, num2 = random.randint(5, 12), random.randint(1, 5)
        return f"Soru: {num1} - {num2} = ?", str(num1 - num2)

    elif secilen_soru_tipi == "mantık":
        mantık_sorular = [
            ("2, 4, 6, ?", "8"),
            ("1, 1, 2, 3, 5, ?", "8"),
            ("10, 9, 8, ?", "7"),
            ("1, 3, ?, 7", "5"),
        ]
        soru, cevap = random.choice(mantık_sorular)
        return f"Sayı Dizisi: {soru}", cevap


pygame.mixer.init()
level_ses = pygame.mixer.Sound("ses\levelup.mp3")


def kapı_kontrol():
    global mevcut_level, labirent, oyuncu_poz, mesaj, input_active, bulmaca_active, bulmaca_cevap
    x, y = oyuncu_poz
    if (labirent[y][x] == 2 and not bulmaca_active):
        soru, cevap = bulmaca_çöz()
        mesaj = soru
        bulmaca_cevap = cevap
        bulmaca_active = True
        input_active = True
        level_ses.play()


def kaynak_topla():
    global mesaj, skor
    x, y = oyuncu_poz
    if labirent[y][x] == 3:
        level_ses.play()
        envanter["enerji"] += 10
        envanter["materyal"] += 1
        skor += 1
        mesaj = "Kaynak toplandı! Enerji: +10, Malzeme: +1"
        labirent[y][x] = 0


def labirent_ciz(ekran, oyuncu_poz):
    offset_x = (GENİSLİK - len(labirent[0]) * KARE_BOYUT) // 2
    offset_y = (YUKSEKLIK - len(labirent) * KARE_BOYUT) // 2

    for y, sıra in enumerate(labirent):
        for x, kare in enumerate(sıra):
            if kare == 1:
                ekran.blit(DUVAR_ICON, (offset_x + x * KARE_BOYUT, offset_y + y * KARE_BOYUT))
            elif kare == 2:
                ekran.blit(KAPI_ICON, (offset_x + x * KARE_BOYUT, offset_y + y * KARE_BOYUT))
            elif kare == 3:
                ekran.blit(KAYNAK_ICON, (offset_x + x * KARE_BOYUT, offset_y + y * KARE_BOYUT))
            else:
                pygame.draw.rect(ekran, WHITE,(offset_x + x * KARE_BOYUT, offset_y + y * KARE_BOYUT, KARE_BOYUT, KARE_BOYUT))

    oyuncu_x, oyuncu_y = oyuncu_poz
    ekran_x = offset_x + oyuncu_x * KARE_BOYUT
    ekran_y = offset_y + oyuncu_y * KARE_BOYUT
    ekran.blit(OYUNCU_ICON, (ekran_x, ekran_y))

    return offset_x, offset_y


skor = 0
dogru_cevap = 0
yanlış_cevap = 0
en_yuksek_skor = 0
EN_YUKSEK_SKOR_FILE = "en_yuksek_skor.txt"


def istatistikler_yaz(ekran):
    margin = 20
    istatistik_bosluk = 30
    istatistik_y_poz = margin

    skor_metin = f"Skor: {skor}"
    skor_metin_genislik = FONT.size(skor_metin)[0]
    metin_yaz(ekran, skor_metin, margin, istatistik_y_poz, color=WHITE)

    dogru_cevap_metin = f"{dogru_cevap}"
    dogru_cevap_metin_genislik = FONT.size(dogru_cevap_metin)[0]
    metin_yaz(ekran, dogru_cevap_metin, margin + skor_metin_genislik + istatistik_bosluk + 160, istatistik_y_poz + 12, color=WHITE)
    ekran.blit(DOGRU_ICON, (margin + skor_metin_genislik + istatistik_bosluk + 100, istatistik_y_poz - 5))

    yanlış_cevap_metin = f"{yanlış_cevap}"
    metin_yaz(ekran, yanlış_cevap_metin, margin + skor_metin_genislik + dogru_cevap_metin_genislik + istatistik_bosluk * 2 + 350, 
              istatistik_y_poz + 12, color=WHITE)
    ekran.blit(YANLIS_ICON, (margin + skor_metin_genislik + dogru_cevap_metin_genislik + istatistik_bosluk * 2 - 10 + 300,
            istatistik_y_poz - 5))

    en_yuksek_skor1 = f"{en_yuksek_skor}"
    metin_yaz(ekran, en_yuksek_skor1, ekran.get_width() - margin - FONT.size(en_yuksek_skor1)[0], margin + 12, color=WHITE)
    ekran.blit(KUPA_ICON, (ekran.get_width() - margin - KUPA_ICON.get_width() - 35, margin - 5))


def mesaj_yaz(ekran, metin, duration=2000):
    ekran.blit(ARKA_PLAN_ICON, (0, 0))
    metin_yaz(ekran, metin, GENİSLİK // 2 - FONT.size(metin)[0] // 2, YUKSEKLIK // 2 - FONT.size(metin)[1] // 2, color=WHITE)
    pygame.display.flip()
    pygame.time.wait(duration)


def en_yuksek_skor_kaydet():
    global en_yuksek_skor
    with open(EN_YUKSEK_SKOR_FILE, "w") as file:
        file.write(str(en_yuksek_skor))

def oyun_bitti(ekran):
    global skor, en_yuksek_skor
    if skor > en_yuksek_skor:
        en_yuksek_skor = skor
        en_yuksek_skor_kaydet()
    bitti_mesaj = f"Oyun Bitti! Skorunuz: {skor}"
    en_yuksek_skor1 = f"En Yüksek Skor: {en_yuksek_skor}"
    bilgi_mesaj = "Tebrikler! Harika bir oyuna imza attınız."
    ekran.blit(ARKA_PLAN_ICON, (0, 0))

    metin_yaz(ekran, bitti_mesaj, GENİSLİK // 2 - FONT.size(bitti_mesaj)[0] // 2, YUKSEKLIK // 2 - 50, color=WHITE)
    metin_yaz(ekran, en_yuksek_skor1, GENİSLİK // 2 - FONT.size(en_yuksek_skor1)[0] // 2, YUKSEKLIK // 2, color=WHITE)
    metin_yaz(ekran, bilgi_mesaj, GENİSLİK // 2 - FONT.size(bilgi_mesaj)[0] // 2, YUKSEKLIK // 2 + 50, color=WHITE)

    pygame.display.flip()
    pygame.time.wait(5000)
    pygame.quit()
    exit()


def en_yuksek_skor_yukle():
    global en_yuksek_skor
    if os.path.exists(EN_YUKSEK_SKOR_FILE):
        with open(EN_YUKSEK_SKOR_FILE, "r") as file:
            try:
                en_yuksek_skor = int(file.read().strip())
            except ValueError:
                en_yuksek_skor = 0


DOSYA_KAYDET = "game_save.json"

def oyunu_kaydet():
    bilgi_kaydet = {
        "mevcut_level": mevcut_level,
        "oyuncu_poz": oyuncu_poz,
        "envanter": envanter,
        "skor": skor,
        "dogru_cevap": dogru_cevap,
        "yanlış_cevap": yanlış_cevap,
    }
    with open(DOSYA_KAYDET, "w") as file:
        json.dump(bilgi_kaydet, file)


def kayıtlı_oyunu_yukle():
    global mevcut_level, oyuncu_poz, envanter, skor, dogru_cevap, yanlış_cevap, labirent
    if os.path.exists(DOSYA_KAYDET):
        with open(DOSYA_KAYDET, "r") as file:
            bilgi_kaydet = json.load(file)
            mevcut_level = bilgi_kaydet["mevcut_level"]
            oyuncu_poz = bilgi_kaydet["oyuncu_poz"]
            envanter = bilgi_kaydet["envanter"]
            skor = bilgi_kaydet["skor"]
            dogru_cevap = bilgi_kaydet["dogru_cevap"]
            yanlış_cevap = bilgi_kaydet["yanlış_cevap"]
            labirent = levels[mevcut_level]
        print("Kaydedilmiş oyun yüklendi!")
    else:
        print("Kaydedilmiş bir oyun bulunamadı.")


def baslangıç_ekranı_göster(ekran):
    font = pygame.font.Font(None, 50)
    metin_renk = (0, 0, 0)
    while True:
        ekran.blit(ARKA_PLAN_ICON, (0, 0))
        metin = font.render("Hoş Geldiniz! Başlamak için bir tuşa basın.", True, metin_renk)
        metin_koordinat = metin.get_rect(center=(GENİSLİK // 2, YUKSEKLIK // 2))
        ekran.blit(metin, metin_koordinat)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                return


def main():
    global mesaj, kullanici_input, input_active, bulmaca_active, bulmaca_cevap, mevcut_level, labirent, oyuncu_poz, skor, dogru_cevap, yanlış_cevap

    pygame.init()

    pygame.mixer.init()
    pygame.mixer.music.load("ses\giris_ekrani.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    ekran = pygame.display.set_mode((GENİSLİK, YUKSEKLIK))
    pygame.display.set_caption("SIU Robot ve Zihin Labirenti")
    baslangıç_ekranı_göster(ekran)

    
    en_yuksek_skor_yukle()
    kayıtlı_oyunu_yukle()

    süre = pygame.time.Clock()
    çalışma = True

    mesaj_yaz(ekran, "SIU Robot ve Zihin Labirenti", 3000)
    while çalışma:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                çalışma = False
            elif event.type == pygame.KEYDOWN:
                if input_active:
                    if event.key == pygame.K_BACKSPACE:
                        kullanici_input = kullanici_input[:-1]
                    elif event.key == pygame.K_RETURN:
                        if kullanici_input.lower() == bulmaca_cevap.lower():
                            mesaj = "Kapı açıldı! Sonraki seviyeye geçiliyor."
                            dogru_cevap += 1
                            skor += 5
                            input_active = False
                            bulmaca_active = False
                            kullanici_input = ""
                            if mevcut_level < len(levels) - 1:
                                mevcut_level += 1
                                labirent = levels[mevcut_level]
                                oyuncu_poz = [1, 1]
                                mesaj_yaz(ekran, f"Bölüm {mevcut_level + 1}", 2000)
                            else:
                                oyun_bitti(ekran)
                        else:
                            mesaj = "Yanlış cevap! Yeni bir soru geliyor."
                            yanlış_cevap += 1
                            skor -= 1
                            soru, cevap = bulmaca_çöz()
                            mesaj = soru
                            bulmaca_cevap = cevap
                            kullanici_input = ""
                    else:
                        kullanici_input += event.unicode
                else:
                    if (event.key == pygame.K_UP and labirent[oyuncu_poz[1] - 1][oyuncu_poz[0]] != 1):
                        oyuncu_poz[1] -= 1
                    elif (event.key == pygame.K_DOWN and labirent[oyuncu_poz[1] + 1][oyuncu_poz[0]] != 1):
                        oyuncu_poz[1] += 1
                    elif (event.key == pygame.K_LEFT and labirent[oyuncu_poz[1]][oyuncu_poz[0] - 1] != 1):
                        oyuncu_poz[0] -= 1
                    elif (event.key == pygame.K_RIGHT and labirent[oyuncu_poz[1]][oyuncu_poz[0] + 1] != 1):
                        oyuncu_poz[0] += 1
                oyunu_kaydet()

        kaynak_topla()
        kapı_kontrol()

        ekran.blit(ARKA_PLAN_ICON, (0, 0))
        labirent_ciz(ekran, oyuncu_poz)
        metin_yaz(ekran, mesaj, 20, YUKSEKLIK - 60)
        
        if input_active:
            metin_yaz(ekran, f"Cevap: {kullanici_input}", 20, YUKSEKLIK - 30)

        istatistikler_yaz(ekran)

        pygame.display.flip()
        süre.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
