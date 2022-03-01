import time
import random


def sleep():  # Bekleme ekranı
    print("\033[1;34;40mİşleminiz Gerçekleştiriliyor Lütfen Bekleyiniz...\033[0;35;39m")
    time.sleep(2)
    print("\n" * 100)


def tekrar(a):  # İşlem sonrası ekran fonksiyon
    b = int(input("0-Çıkış Yap\n1-Farklı İşlemler\nYapmak İstediğiniz İşlemi Tuşlayınız:"))
    sleep()
    print("\n" * 100)
    while b != 1 and b != 0:
        b = int(input("0-Çıkış Yap\n1-Farklı İşlemler\nHatalı Tuşlama! Yapmak İstediğiniz İşlemi Tekrar Tuşlayınız:"))
    return b


def data():
    f_2 = open("data.txt", "a")
    sil(iban)
    sil_1()
    temp_gonderen = ["\n", name_check, '+', s_name_check, '-', id_check, '/', pas_check,
                     '*', iban, '=', str(sum_2), '%']
    f_2.writelines(temp_gonderen)
    f_2.close()


def sil(girdi):
    with open("data.txt", "r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if girdi not in line:
                f.write(line)
        f.truncate()
    with open("data.txt", "r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if " " not in line:
                f.write(line)
        f.truncate()


def sil_1():
    with open("data.txt", "r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if " " not in line:
                f.write(line)
        f.truncate()


i = 0  # Ayrımların indisleri
k = 0  # Kişi sayısı döngüsündeki eleman
y = bool(1)  # Genel Döngü Değeri
j = 3  # Hatalı İşlem Sonrası Döngü Değeri
check = 0  # Sisteme Giriş Değeri
bakiye = 1000  # Mevcut Kişi Bakiyesi
x = bool(1)  # Sistem İçi Döngü
while y:
    print("1-Giriş Yap\n2-Kayıt ol\n0-Çıkış")  # Giriş Paneli
    p_islem = int(input("Yapmak İstediğiniz İşlemi Tuşlayınız:"))
    if p_islem == 1:  # Giriş Yap
        while j >= 0:
            k = 0
            id = input("Kullanıcı Adı:")
            pas = int(input("Şifre:"))
            f = open("data.txt", "r")
            while k < 10:  # 10 Kişiye Kadar Kontrol Eder
                file = f.readline()
                while i < len(file):  # Ayrımları Bulur
                    if file[i] == '+':
                        n_index = i
                    if file[i] == '-':
                        s_index = i
                    if file[i] == '/':
                        i_index = i
                    if file[i] == '*':
                        iban_index = i
                    if file[i] == '=':
                        bakiye_index = i
                    if file[i] == '%':
                        slash_1 = i
                    i += 1
                i = 0
                name_check = file[:n_index]  # İsim
                s_name_check = file[n_index + 1:s_index]  # Soyisim
                id_check = file[s_index + 1:i_index]  # Kullanıcı Adı
                pas_check = file[i_index + 1:iban_index]  # Şifre
                iban = file[iban_index + 1:bakiye_index]  # iban
                bakiye_check = file[bakiye_index + 1:slash_1]  # bakiye

                if id == id_check and pas == int(pas_check):  # Giriş
                    sleep()
                    print("\033[0;32;40mGiriş Başarılı\033[0;35;39m")
                    check = 1
                    y = bool(0)
                    j = -1
                    break
                else:
                    k += 1
                    if k == 9:
                        sleep()
                        print("\033[1;31;40mHatalı Kullanıcı Adı veya Şifre(Kalan Hak sayısı:{}\033[0;35;39m)".format(
                            j))  # Hata
                        if (j == 0):
                            print("Art Arda Çok Fazla Hatalı İşlem Gerçekleştirdiniz İşlem Sonlandırılıyor...")
                            time.sleep(3)
                            exit(0)
                        j -= 1
        f.close()

    elif p_islem == 2:  # Kayıt Yeri
        name = input("İsim:")
        s_name = input("Soyad:")
        id = input("Kullanıcı Adi:")
        pas = input("Şifre:")
        iban = str(random.randint(9999, 100000))  # int olarak alındığında hata veriyor !
        temp = ["\n", name, '+', s_name, '-', id, '/', pas, '*', iban, '=', str(bakiye), '%']
        d = open("data.txt", "a")
        d.writelines(temp)
        d.flush()  # Bilgileri anında dosyaya göndermek için kullanılır
        sleep()
        print("\033[0;32;40mKaydınız Başarılı Bir Şekilde Gerçekleştirilmiştir\033[0;35;39m")

    elif p_islem == 0:
        sleep()
        print("\033[1;35;40mİyi Günler Dileriz\033[0;35;39m")
        exit(0)
    else:
        print("Hatalı Tuşlama")
k = 0
if check == 1:  # Sistem İçi
    new_grades_gonderen = [int(g) for g in bakiye_check]
    c = 0
    sum_2 = 0
    while c < len(new_grades_gonderen):
        sum_2 = sum_2 * 10 + new_grades_gonderen[c]
        c += 1
    print("\033[1;33;40mHoşgeldiniz {} {}\033[0;35;39m".format(name_check, s_name_check))
    while x:
        print(
            "İşlemler:\n1-Bakiye Sorgulama\n2-Para Çekme\n3-Para Yatırma\n4-İban Sorgulama\n5-Para Transferi\n0-Çıkış")
        islem = int(input("Lütfen Yapmak İstediğiniz İşleri Rakamlar İle Belirtiniz:"))
        if 1 == islem:
            sleep()
            print("Bakiyeniz:", sum_2)
            data()
            x = tekrar(x)
        elif 2 == islem:
            tutar = int(input("Çekmek İstediğiniz Tutarı Giriniz:"))
            sleep()
            while tutar > bakiye:
                print("\033[0;31;40mBakiye Yetersiz\033[0;35;39m")
                tutar = int(input("Çekmek İstediğiniz Tutarı Giriniz(0-Geri Gel):"))
                if tutar == 0:
                    x = 1
                    break
            sum_2 -= tutar
            print("Yeni Bakiyeniz:", sum_2)
            data()
            x = tekrar(x)
        elif 3 == islem:
            tutar = int(input("Yatırmak İstediğiniz Tutarı Giriniz:"))
            sleep()
            sum_2 += tutar
            print("Yeni Bakiyeniz:", sum_2)
            data()
            x = tekrar(x)
        elif 4 == islem:
            sleep()
            print("İban:", iban)
            x = tekrar(x)
        elif 5 == islem:
            transfer = int(input("Ne Kadar göndermek istersiniz:"))
            alici = input("Göndermek İstediğiniz Kişinin İban'ını Giriniz:")
            f_1 = open("data.txt", "r")
            if transfer < sum_2 and alici != iban:
                while k < 10:
                    file = f_1.readline()
                    while i < len(file):  # Ayrımları Bulur
                        if file[i] == '+':
                            n_index = i
                        if file[i] == '-':
                            s_index = i
                        if file[i] == '*':
                            iban_index = i
                        if file[i] == '=':
                            bakiye_index = i
                        if file[i] == '%':
                            slash = i
                        i += 1
                    i = 0
                    name_transfer = file[:n_index]  # İsim
                    s_name_transfer = file[n_index + 1:s_index]  # Soyisim
                    id_transfer = file[s_index + 1:i_index]  # Kullanıcı Adı
                    pas_transfer = file[i_index + 1:iban_index]  # Şifre
                    iban_transfer = file[iban_index + 1:bakiye_index]  # iban
                    bakiye_trasfer = file[bakiye_index + 1:slash]  # bakiye
                    new_grades = [int(g) for g in bakiye_trasfer]
                    c = 0
                    sum = 0
                    while c < len(new_grades):
                        sum = sum * 10 + new_grades[c]
                        c += 1
                    if iban_transfer == alici:
                        f_1.close()
                        sum += transfer
                        sil(iban_transfer)
                        sil_1()
                        temp_transfer = ["\n", name_transfer, '+', s_name_transfer, '-', id_transfer, '/', pas_transfer,
                                         '*', iban_transfer, '=', str(sum), '%']
                        f_2 = open("data.txt", "a")
                        f_2.writelines(temp_transfer)
                        f_2.flush()
                        sum_2 -= transfer
                        sil(iban)
                        sil_1()
                        temp_gonderen = ["\n", name_check, '+', s_name_check, '-', id_check, '/', pas_check,
                                         '*', iban, '=', str(sum_2), '%']
                        f_2.writelines(temp_gonderen)
                        f_2.flush()
                        f_2.close()
                        sleep()
                        print(
                            "\033[0;33;40m{} {}\033[0;32;40m Adlı Kişiye Para Transferi Başarılı Bir Şekilde Gerçekleşti\033[0;35;39m"
                            .format(name_transfer, s_name_transfer))
                        x = tekrar(x)
                        break
                    else:
                        k += 1
                        if k == 9:
                            sleep()
                            print("\033[1;31;40mHatalı İban Numarası\033[0;35;39m")  # Hata
                            x = tekrar(x)

            else:
                sleep()
                print("\033[1;31;40mYetersiz Bakiye veya Kişisel İban'ınızı Girdiniz\033[0;35;39m")
                x = tekrar(x)

        elif 0 == islem:
            data()
            sleep()
            print("\033[1;33;40mHoşçakalın {} {}\033[0;35;39m".format(name_check, s_name_check))
            x = 0
        else:
            print("\033[1;31;40mHatalı İşlem\033[0;35;39m")
            x = tekrar(x)
