list1=[]
list2=[]
dongu=1
while dongu==1:
    AdSoyad=input("Adınızı ve Soyadınızı Giriniz:")
    Adres=input("Adresinizi Giriniz:")
    TelNo = int(input("Telefon Numaranızı Giriniz:"))
    Mekan=input("İç veya Dış Mekan Seçiniz:")
    if Mekan=="iç":
        kapasite=450
        while True:
            IcKapasite=int(input("Gelecek Kişi Sayısını Giriniz:"))
            if IcKapasite>kapasite:
                print("Kapasite Üzerinde Kişi Girdiniz!!!")
                continue
            else:
                print("Oluşturuluyor...")
                break
        while True:
            Tarih = input("Düğün Tarihini Gİriniz:")
            if (Tarih in list1):
                print("REZERVE EDİLMİŞ!!")
                continue
            else:
                list1.append(Tarih)
                print("REZERVASYONUNUZ OLUŞTURULDU.")
                break
    elif Mekan== "dış":
        kapasite1=700
        while True:
            DisKapasite = int(input("Gelecek Kişi Sayısını Giriniz:"))
            if DisKapasite>kapasite1:
                print("Kapasite Üzerinde Kişi Girdiniz!!!")
                continue
            else:
                print("Oluşturuluyor...")
                break
        while True:
            Tarih=input("Düğün Tarihini Gİriniz:")
            if (Tarih in list2):
                print("REZERVE EDİLMİŞ!!")
                continue
            else:
                list2.append(Tarih)
                print("REZERVASYONUNUZ OLUŞTURULDU.")
                break
    cevap=input("Devam Edilecek Mi?:")
    if cevap=="evet":
        continue
    elif cevap=="hayır":
        dongu=2