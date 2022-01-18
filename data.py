import time
i = 0
k = 0
y = bool(1)
j = 3
while y:
    print("1-Sign in\n2-Sign up")
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
                    print("Giriş Başarılı")
                    y = bool(0)
                    j = -1
                    break
                else:
                    k += 1
                    if k == 9:
                        print("Hatalı Kullanıcı Adı veya Şifre(Kalan Hak sayısı:{})".format(j))
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
    else:
        print("Hatalı Tuşlama")






