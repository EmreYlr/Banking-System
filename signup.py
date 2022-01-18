name = input("İsim:")
s_name = input("Soyad:")
id = input("Kullanıcı Adi:")
pas = input("Şifre:")
temp = ["\n", name, '+', s_name, '-', id, '/', pas]
d = open("data.txt", "a")
d.writelines(temp)
d.flush()


"""d.write('\n')
d.write(name)
d.write('+')
d.write(s_name)
d.write('+')
d.write(id)
d.write('+')
d.write(pas)
"""
