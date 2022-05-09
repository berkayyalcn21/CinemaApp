from random import *
import sys

global allFilms
global category

allFilms = []
films = ["Şeytanın Avukatı", "Nefesini Tut", "Arınma Gecesi", "Cinnet", "Alive", "Oyun",
                              "Üç Harfliler 2",
                              "Felekten Bir Gece", "Tam Gaz", "Green Book", "Şipşak Aile", "Fokus", "Tatil",
                              "V", "Lucy", "Başlangıç", "Yıldızlar Arası", "BIRD BOX"]
for i in films:
    allFilms.append(i)

def user():
    members = {"1": "123", "ali": "2580", "can": "can123", "berk": "1234"}
    rightOfEntry = 2
    while(1):
        user = input("Kullanıcı adı: ")
        password = input("Şifre: ")
        if (user in members.keys() and password in members.values()):
            print("Başarıyla Giriş Yapıldı.")
            print(""" ****** Hoşgeldiniz ******
            İşlemleri Numara Seçerek Yapabilirsiniz!
            1- Tüm filmleri görüntüle
            2- Günün önerilen filmini görüntüle
            3- Kategorileri görüntüle
            4- İstenilen kategori adını yazarak filmi gör
            5- İzlemek istediğin filmi ara
            6- Film değerlendirmlerini gör
            7- Çıkış için 'Ç' harfine basabilirsiniz""")

            while 1:
                print("")
                horror = ["Şeytanın Avukatı", "Nefesini Tut", "Arınma Gecesi", "Cinnet", "Alive", "Oyun", "Üç Harfliler 2"]
                randomHorror = choice(horror)
                comedy = ["Felekten Bir Gece", "Tam Gaz", "Green Book", "Şipşak Aile", "Fokus", "Tatil"]
                randomComedy = choice(comedy)
                scienceFiction = ["V", "Lucy", "Başlangıç", "Yıldızlar Arası", "BIRD BOX"]
                category = {
                    'korku': horror,
                    'kodemi': comedy,
                    'bilim kurgu': scienceFiction}

                for key, value in category.items():
                    print(key, ": ", end="")
                    for i in value:
                        print(i, sep=", ", end="")

                randomScience = choice(scienceFiction)
                categories = randomScience, randomHorror, randomComedy
                movieScore = ["Şeytanın Avukatı: 4.3", "Nefesini Tut: 3.2", "Cinnet: 4.1", "Fokus: 4.9", "Alive: 4.8"]
                choose = input("Yapmak istediğiniz işlemi seçin: ")

                if choose == "1":
                    for i in allFilms:
                        print("Sitemizde ki mevcut films = ", i)

                elif choose == "2":
                    print("Bugünün Önerisi: ", categories)

                elif choose == "3":
                    print("Mevcut Kategoriler:\nKorku\nKomedi\nBilim Kurgu")

                elif choose == "4":
                    request = input("Görmek istediğiniz kategori: ")
                    if request == "korku" or request == "Korku" or request == "KORKU":
                        print(horror)
                    elif request == "komedi" or request == "Komedi" or request == "KOMEDİ":
                        print(comedy)
                    elif request == "bilim kurgu" or request == "Bilim kurgu" or request == "BİLİM KURGU" or request == "Bilim Kurgu":
                        print(scienceFiction)
                    else:
                        print("Hatala Giriş Yaptınız!")

                elif choose == "5":
                    requestMovie = input("Aramak istediğiniz filmin adı: ")
                    if requestMovie in allFilms:
                        print("")
                        print(requestMovie + " Adlı filminiz oynatılıyor...")
                        print("İyi seyirler...")
                        evaluate= input("Filmi değerlendirmek ister misiniz? (E ya da H): ")
                        if evaluate == "E" or evaluate == "e":
                            while 1:
                                point= int(input("1-5 arası bir puan verin lütfen: "))
                                if point == 1 or point == 2 or point == 3 or point == 4 or point == 5:
                                    print("Değerlendirme için teşekkürler.")
                                    break
                                else:
                                    print("Hatalı giriş lütfen 1-5 arası bir değer girin!!!")
                        else:
                            print("Değerlendirmeleriniz sizi daha iyi tanıyabilmemizi sağlamakta başka bir zaman için değerlendimeyi unutmayın!")
                    else:
                        print("Aradığınız film mevcut değil!")

                elif choose == "6":
                    for i in movieScore:
                        print(i)

                elif choose == "Ç" or choose == "ç":
                    sys.exit()

                else:
                    print("Hatalı giriş yaptınız!!!")
        else:
            print("Kullanıcı adınız ya da Parolanız Hatalı!")
            rightOfEntry -= 1
        if rightOfEntry == 0:
            print("Giriş hakkınız dolmuştur 1 saat sonra tekrar deneyin!")
            break

def admin():
    admin = "berkay"
    password = "123456"
    while 1:
        userName = input("Admin: ")
        password2 = input("Şifre: ")
        if userName == admin and password == password2:
            print("Başarıyla Giriş Yapıldı.")
            print(""" 
            1- Film ekleme
            2- Panel değiştir""")
            process = input("İşlemi seçiniz: ")
            if process == "1":
                movieName = input("Eklemek istediğiniz film: ")
                allFilms.append(movieName)
            elif process == "2":
                user()
        else:
            print("Kullanıcıadı veya Şifre Hatalı!!")

print("""
1- Admin
2- Kullanıcı
Seçimleri numara ile yapınız!!!""")
loginPanel = input("Hangi paneli seçemek istiyorsunuz: ").lower()
if loginPanel == "1":
    admin()
elif loginPanel == "2":
    user()
else:
    print("Hatalı tuşlama")