import time
def tekrar(a):
    b = int(input("0-Çıkış Yap\n1-Farklı İşlemler\nYapmak İstediğiniz İşlemi Tuşlayınız:"))
    while b != 1 and b != 0:
        b = int(input("0-Çıkış Yap\n1-Farklı İşlemler\nHatalı Tuşlama! Yapmak İstediğiniz İşlemi Tekrar Tuşlayınız:"))
    return b
i = 0
k = 0
y = bool(1)
j = 3
check = 0
bakiye = int(1000)
x = bool(1)
while y:
    print("1-Giriş Yap\n2-Kayıt ol\n0-Çıkış")
    p_islem = int(input("Yapmak İstediğiniz İşlemi Tuşlayınız:"))
    if p_islem == 1:
        while j >= 0:
            k = 0
            id = input("Kullanıcı Adı:")
            pas = int(input("Şifre:"))
            f = open("data.txt", "r")
            while k < 10:
                file = f.readline()
                while i < len(file):  # Ayrımları Bulur
                    if file[i] == '+':
                        n_index = i
                    if file[i] == '-':
                        s_index = i
                    if file[i] == '/':
                        i_index = i
                    i += 1
                i = 0
                name_check = file[:n_index]  # İsim
                s_name_check = file[n_index + 1:s_index]  # Soyisim
                id_check = file[s_index + 1:i_index]  # Kullanıcı Adı
                pas_check = file[i_index + 1:]  # Şifre
                if id!=id_check:
                    id_k = bool(0)
                if pas!=pas_check:
                    pas_k= bool(0)
                if id == id_check and pas == int(pas_check):
                    print("\033[0;32;40mGiriş Başarılı\033[0;35;39m")
                    check = 1
                    y = bool(0)
                    j = -1
                    break
                else:
                    k += 1
                    if k == 9:
                        print("\033[1;31;40mHatalı Kullanıcı Adı veya Şifre(Kalan Hak sayısı:{}\033[0;35;39m)".format(j))
                        if(j == 0):
                            print("Art Arda Çok Fazla İşlem Gerçekleştirdiniz İşlem Sonlandırılıyor...")
                            time.sleep(3)
                            exit(0)
                        j -= 1
        f.close()

    elif p_islem == 2:
        name = input("İsim:")
        s_name = input("Soyad:")
        id = input("Kullanıcı Adi:")
        pas = input("Şifre:")
        temp = ["\n", name, '+', s_name, '-', id, '/', pas]
        d = open("data.txt", "a")
        d.writelines(temp)
        d.flush()
    elif p_islem == 0:
        exit(0)
    else:
        print("Hatalı Tuşlama")

if check == 1:
    print("\033[1;33;40mHoşgeldiniz {} {}\033[0;35;39m".format(name_check,s_name_check))
    while x:
        print("İşlemler:\n1-Bakiye Sorgulama\n2-Para Çekme\n3-Para Yatırma\n0-Çıkış")
        islem = int(input("Lütfen Yapmak İstediğiniz İşleri Rakamlar İle Belirtiniz:"))
        if 1 == islem:
            print("Bakiyeniz:", bakiye)
            x = tekrar(x)
        elif 2 == islem:
            tutar = int(input("Çekmek İstediğiniz Tutarı Giriniz:"))
            while tutar > bakiye:
                print("Bakiye Yetersiz")
                tutar = int(input("Çekmek İstediğiniz Tutarı Giriniz:"))
            bakiye -= tutar
            print("Yeni Bakiyeniz:", bakiye)
            x = tekrar(x)
        elif 3 == islem:
            tutar = int(input("Yatırmak İstediğiniz Tutarı Giriniz:"))
            bakiye += tutar
            print("Yeni Bakiyeniz:", bakiye)
            x = tekrar(x)
        elif 0 == islem:
            x = 0
        else:
            print("Hatalı İşlem")
            x = tekrar(x)