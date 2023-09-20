import math

# Listeyi oluşturma
list =[]
num = float(input("Kac tane rakam uzerinden islem yapmak istiyorsunuz?: "))
for n in range(num)
liste = float(input("Listede yer almasini istediginiz sayilari giriniz: "))
list.append(liste)

# Girilen sayıları yazdırma
print("Girilen Sayilar: ", list)


# Listeye ilave edilen sayıların tam kare olmadığını tespit eden metod
tamKare = [k for k in list if (
   math.sqrt(k) == math.floor(math.sqrt(k)))]

# Listedeki bütün tam kare sayıları yazdırma
print("Listedeki tam kare sayilar: ", tamKare)
