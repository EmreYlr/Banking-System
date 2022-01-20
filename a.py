#Projede Belirli Kısımları Deneme Yeri
"""

file = f.writelines(str(1))
f.close()

if file == '1':
    print("*")

"""
iban = str(72832)
with open("test.txt","r+") as f:
    new_f = f.readlines()
    f.seek(0)
    for line in new_f:
        if iban not in line:
            f.write(line)
    f.truncate()