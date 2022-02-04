import listBook
import addBook
import deleteBook
import time


print("X Yayinevine Hosgeldiniz")


while(1):
    
    print("Menu : ")
    print("1-) Kitap Listesi\n2-) Kitap Ekle\n3-) Kitap Sil\n4-) Cikis")
    
    secim = int(input("Islem Giriniz : "))
    
    if(secim == 1):
        print("Liste Getiriliyor...")
        time.sleep(2)
        listBook.kitapListesi()
    
    elif(secim == 2):
        
        kitapAdi = input("Kitap Adi : ")
        yazarAdi = input("Yazar Adi : ")
        sayfaSayisi = int(input("Sayfa Sayisi : "))
        yayinevi = input("Yayinevi : ")
        fiyat = float(input("Fiyat : "))
        
        print("Veriler Sisteme Isleniyor...")
        time.sleep(2)
        
        addBook.kitapEkle(kitapAdi, yazarAdi, sayfaSayisi, yayinevi, fiyat)
    
    elif(secim == 3):
        silinecekKitap = input("Silmek Istediginiz Kitap Adi : ")
        deleteBook.kitapSilme(silinecekKitap)
        
    
    elif(secim == 4):
        listBook.cikis()
        break
    else:
        print("Yanlis Secim Girdiniz!")
        time.sleep(2)
        continue

