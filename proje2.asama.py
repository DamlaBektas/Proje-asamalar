
sozluk_ic={}
sozluk_dis={}
dongu=1

while dongu==1:

    def Iptal():
        mekan_iptal=input("Hangi mekanda rezervasyon oluşturmuştunuz?")
        if mekan_iptal=="iç":
            ad_iptal = input("Adınızı Giriniz:")
            if (ad_iptal in sozluk_ic.keys()):
                del sozluk_ic[ad_iptal]
                print("Rezarvasyon iptal talebiniz gerçekleştirilmiştir.")
            else:
                print("Böyle Bir Kayıt Yok")

        if mekan_iptal=="dış":
            ad_iptal = input("Adınızı Giriniz:")
            if (ad_iptal in sozluk_dis.keys()):
                del sozluk_dis[ad_iptal]
                print("Rezarvasyon iptal talebiniz gerçekleştirilmiştir.")
            else:
                print("Böyle Bir Kayıt Yok")
        return

    def Kayıt():
        AdSoyad = input("Adınızı ve Soyadınızı Giriniz:")
        Mekan = input("İç veya Dış Mekan Seçiniz:")
        if Mekan == "iç":
            Ickapasite = 600
            while True:
                kisi = int(input("Gelecek Kişi Sayısını Giriniz:"))
                if kisi > Ickapasite:
                    print("Kapasite Üzerinde Kişi Girdiniz!!!")
                    continue
                else:
                    print("Oluşturuluyor...")
                    break

            while True:
                from datetime import datetime
                tarih_str = str(input("Düğün Tarihini-Saatini Giriniz(yyyy-aa-gg ss:dd):"))
                Tarih = datetime.strptime(tarih_str, "%Y-%m-%d %H:%M")

                if (Tarih in sozluk_ic.values()):
                    print("REZERVE EDİLMİŞ!!")
                    continue
                else:
                    sozluk_ic.setdefault(AdSoyad,Tarih)
                    print("    ----MENÜ----  "" \n 1-Kokteyl (kişi başı fiyat 50tl)"" \n"
                          " 2-Yemekli (kişi başı fiyat 30tl)"" \n 3-Çerez+içecek(kişi başı fiyat 10tl)")
                    secim = int(input("Menüden Kategori Seçiniz:"))
                    if secim == 1:
                        # iç mekan fiyatı 1000 tl olduğu için herbirine ekliyorum.
                        fiyat = (kisi * 50) + 1000
                    elif secim == 2:
                        fiyat = (kisi * 30) + 1000
                    elif secim == 3:
                        fiyat = (kisi * 10) + 1000
                    print("{} {}  TARİHİNDE REZERVASYONUNUZ OLUŞTURULDU.".format(AdSoyad, Tarih))
                    print("Toplam Ücret:{} TL dir.".format(fiyat))
                    dosya = open("Kayıt Dosyası.txt", "a")
                    dosya.write("AD:{}  TARİH:{}   FİYAT:{} TL\n".format(AdSoyad, Tarih, fiyat))
                    dosya.close()
                    break

        elif Mekan == "dış":
            Diskapasite = 900
            while True:
                kisi1 = int(input("Gelecek Kişi Sayısını Giriniz:"))
                if kisi1 > Diskapasite:
                    print("Kapasite Üzerinde Kisi Girdiniz!!!")
                    continue
                else:
                    print("Oluşturuluyor...")
                    break
            while True:
                from datetime import datetime
                tarih_str = str(input("Düğün Tarihini-Saatini Giriniz(yyyy-aa-gg ss:dd):"))
                Tarih = datetime.strptime(tarih_str, "%Y-%m-%d %H:%M")

                if (Tarih in sozluk_dis.values()):
                    print("REZERVE EDİLMİŞ!!")
                    continue
                else:
                    sozluk_dis.setdefault(AdSoyad,Tarih)
                    print("    ----MENÜ----  "" \n 1-Kokteyl (kişi başı fiyat 50tl)"" \n "
                          "2-Yemekli (kişi başı fiyat 30tl)"" \n 3-Çerez+içecek(kişi başı fiyat 10tl)")

                    secim = int(input("Menüden Kategori Seçiniz:"))
                    if secim == 1:
                        # dış mekan fiyatı 2000 tl olduğu için herbirine ekliyorum.
                        fiyat = (kisi1 * 50) + 2000
                    elif secim == 2:
                        fiyat = (kisi1 * 30) + 2000
                    elif secim == 3:
                        fiyat = (kisi1 * 10) + 2000

                    print("{} {}  TARİHİNDE REZERVASYONUNUZ OLUŞTURULDU.".format(AdSoyad, Tarih))
                    print("Toplam Ücret:{} TL dir.".format(fiyat))
                    dosya = open("Kayıt Dosyası.txt", "a")
                    dosya.write("AD:{}  TARİH:{}  FİYAT:{} TL\n".format(AdSoyad, Tarih, fiyat))
                    dosya.close()
                    return


    islem = input(print("HANGİ İŞLEMİ YAPACAĞINIZI SEÇİNİZ:\n""1) Kayıt\n" "2)Rezervasyon İptal\n" "3)Çıkış-Kayıt Dosyası Gör\n"))
    if islem == "1":
        Kayıt()
    elif islem == "2":
        Iptal()
    elif islem == "3":
        dongu = 2
        oku=open("Kayıt Dosyası.txt","r")
        a=oku.read()
        print(a)