list1=[]
list2=[]
hasilat=0
dongu=1
while dongu==1:
    AdSoyad=input("Adınızı ve Soyadınızı Giriniz:")
    Adres=input("Adresinizi Giriniz:")
    TelNo = int(input("Telefon Numaranızı Giriniz:"))
    Mekan=input("İç veya Dış Mekan Seçiniz:")
    if Mekan=="iç":
        Ickapasite=600
        while True:
            kisi=int(input("Gelecek Kişi Sayısını Giriniz:"))
            if kisi>Ickapasite:
                print("Kapasite Üzerinde Kişi Girdiniz!!!")
                continue
            else:
                print("Oluşturuluyor...")
                break

        while True:
            from datetime import datetime
            tarih_str = str(input("Düğün Tarihini-Saatini Griniz(yyyy-aa-gg ss:dd):"))
            Tarih=datetime.strptime(tarih_str,"%Y-%m-%d %H:%M")

            if (Tarih in list1):
                print("REZERVE EDİLMİŞ!!")
                continue
            else:
                list1.append(Tarih)
                print("    ----MENÜ----  "" \n 1-Kokteyl (kişi başı fiyat 50tl)"" \n"
                      " 2-Yemekli (kişi başı fiyat 30tl)"" \n 3-Çerez+içecek(kişi başı fiyat 10tl)")
                secim=int(input("Menüden Kategori Seçiniz:"))
                if secim==1:
                    # iç mekan fiyatı 1000 tl olduğu için herbirine ekliyorum.
                    fiyat=(kisi*50)+1000
                elif secim==2:
                    fiyat=(kisi*30)+1000
                elif secim==3:
                    fiyat=(kisi*10)+1000
                hasilat+=fiyat
                print("{} {}  TARİHİNDE REZERVASYONUNUZ OLUŞTURULDU.".format(AdSoyad, Tarih))
                print("Toplam Ücret:{} TL dir.".format(fiyat))
                break
    elif Mekan== "dış":
        Diskapasite=900
        while True:
            kisi1 = int(input("Gelecek Kişi Sayısını Giriniz:"))
            if kisi1>Diskapasite:
                print("Kapasite Üzerinde Kişi Girdiniz!!!")
                continue
            else:
                print("Oluşturuluyor...")
                break
        while True:
            from datetime import datetime
            tarih_str = str(input("Düğün Tarihini-Saatini Giriniz(yyyy-aa-gg ss:dd):"))
            Tarih = datetime.strptime(tarih_str, "%Y-%m-%d %H:%M")

            if (Tarih in list2):
                print("REZERVE EDİLMİŞ!!")
                continue
            else:
                list2.append(Tarih)
                print("    ----MENÜ----  "" \n 1-Kokteyl (kişi başı fiyat 50tl)"" \n "
                      "2-Yemekli (kişi başı fiyat 30tl)"" \n 3-Çerez+içecek(kişi başı fiyat 10tl)")
                secim = int(input("Menüden Kategori Seçiniz:"))
                if secim == 1:
                    # dış mekan fiyatı 2000 tl olduğu için herbirine ekliyorum.
                    fiyat = (kisi1*50)+2000
                elif secim==2:
                    fiyat=(kisi1*30)+2000
                elif secim==3:
                    fiyat=(kisi1*10)+2000
                hasilat+=fiyat
                print("{} {}  TARİHİNDE REZERVASYONUNUZ OLUŞTURULDU.".format(AdSoyad,Tarih))
                print("Toplam Ücret:{} TL dir.".format(fiyat))
                break

    cevap=input("Devam Edilecek Mi?:")
    if cevap=="evet":
        continue
    elif cevap=="hayır":
        import datetime
        bugun=datetime.date.today()
        print("{} Tarihinin Hasılatı:{} TL'dir.".format(bugun,hasilat))
        dongu=2