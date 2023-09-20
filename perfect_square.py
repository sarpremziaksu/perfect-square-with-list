from math import ceil, sqrt
 
# Belilenen aralıkta bütün tam kare sayıları yazdıran fonksiyon tanımı
def tamKare(ilk, son) :
 
 
    # İlk sayıyı elde etme
    n1 = ceil(sqrt(ilk));
 
    # İlk sayının karesini çıkarma
    n2 = n1 * n1;
 
    # İkinci sayıyı elde edecek fonksiyon
    n1 = (n1 * 2) + 1;
 
    # Aralıktaki tam kare sayıları işleyen döngünün tanımlanması
    while ((n2 >= ilk and n2 <= son)) :
 
        # Tam kareyi yazdırma
        print(n2, end= " ");
 
        # Bir sonraki numarayı elde etme
        n2 = n2 + n1;
 
        # Eklenecek tek sayıyı ilave etme
        n1 += 2;
 
# Sürücü kod
if __name__ == "__main__" :
 
    ilk = int(input("Ilk aralik sayisini giriniz: ")); 
    son = int(input("Son aralik sayisini giriniz: "));
 
    tamKare(ilk, son);
