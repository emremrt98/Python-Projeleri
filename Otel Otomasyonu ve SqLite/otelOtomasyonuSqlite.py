# =============================================================================
# 
#                        EMRE MERT
#                        203305028
#             MEKATRONİK MÜHENDİSLİĞİ 2.SINIF
#          GÖRSEL PROGRAMLAMA SQLITE OTEL OTOMASYONU
# 
# =============================================================================


import sqlite3
vt = sqlite3.connect("otel.sqlite")
im = vt.cursor()
im.execute("CREATE TABLE IF NOT EXISTS rezervasyon (Ad, Soyad, 'TC No','Meslek', 'Giris Tarihi', 'Cikis Tarihi', 'Oda No' )")


def kullaniciKaydi(m_Oda, s_Oda, d_Oda):
    
    print("Kullanici Kayit Ekrani")
    print("__________________________")
     
    ad = input("Adınız : ")
    soyad = input("Soyad : ")
    tcNO = input("TC No : ")
    meslek = input("Mesleginiz (Sayisal Meslekler : M - Sozel Meslekler : S - Devlet Calisanlari : D ) : ")
    gTarih = input("Giris Tarihi : ")
    cTarih = input("Cikis Tarihi : ")  
    
    
    if(meslek == "M"):
       
        print("Size Ozel Oda No : ", end=(" "))
        odaSayisiM = 10
        print(m_Oda[0:odaSayisiM])
         
        
        tercih = int(input("Oda No Giriniz : "))
         
        if(odaSayisiM < 10):
             tercih -= 1
  
        m_Oda.pop(tercih-1)
        odaSayisiM -= 1
     
    elif(meslek == "S"):
         
        print("Size Ozel Oda No : ", end=(" "))
        odaSayisiS = 10
        print(s_Oda[0:odaSayisiS])
         
        tercih = int(input("Oda No Giriniz : "))
         
        if(odaSayisiS < 10):
            tercih -= 1
                 
        s_Oda.pop(tercih-11)
        odaSayisiS -= 1
         
    elif(meslek == "D"):
         
        print("Size Ozel Oda No : ", end=(" "))
        odaSayisiD = 10
        print(d_Oda[0:odaSayisiD])
        tercih = int(input("Oda No Giriniz : "))
         
        if(odaSayisiD < 10):
            tercih -= 1
         
        d_Oda.pop(tercih-21)
        odaSayisiD -= 1
    
    tercih = str(tercih)
    im.execute("INSERT INTO rezervasyon VALUES(?,?,?,?,?,?,?)", (ad, soyad, tcNO, meslek, gTarih, cTarih, tercih))
    vt.commit()
    


def bilgiKontrol():
    print("Rezerv Bilgi Kontrolü")
    
    im.execute("SELECT * FROM rezervasyon")
    veriler = im.fetchall()
    print(veriler)

def odaNo():
    odalar = list()
    odalar.extend(m_Oda)
    odalar.extend(s_Oda)
    odalar.extend(d_Oda)
    print(odalar)



liste = list()
m_Oda = list() 
s_Oda = list()
d_Oda = list()  
for i in range(1,11):
    m_Oda.append(i)     

for j in range(11, 21):
    s_Oda.append(j)
    
for k in range(21, 31):
    d_Oda.append(k)
    

    
while(1):
    
    print("1-)Rezervasyon Kaydı\n2-)Rezervasyon Kontrolü\n3-)Bos Oda\n4-)Cikis")    
    islem = int(input("Yapmak Istediginiz Islem : "))   
    
    if(islem == 1):
        kullaniciKaydi(m_Oda,s_Oda,d_Oda)
        
    elif(islem == 2):
        bilgiKontrol()
    
    elif(islem == 3):
        odaNo()
        print("")
    
    elif(islem == 4):
        print("Sistem Kapatiliyor...")
        vt.close()
        break
    else:
        print("Yanlis Islem")
        break
    



