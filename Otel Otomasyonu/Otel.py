# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 15:06:16 2021

@author: emrem
"""


# =============================================================================
# 
# Emre Mert
# 203305028
# Mekatronik Mühendisliği 2.sınıf
# =============================================================================



def kullaniciKaydi(m_Oda,s_Oda,d_Oda):
    
    dosya = open("bilgiler.txt", "r+")
    dosya.close()
    
    
    print("Kullanici Kayit Ekrani")
    print("__________________________")
    
    bilgiler = input("Sirasiyla Ad, Soyad, TCKno, Giris Tarihi, Cikis Tarihi : ")    
    liste = bilgiler.split(",")
    
    meslek = input("Mesleginiz (Sayisal Meslekler : M - Sozel Meslekler : S - Devlet Calisanlari : D ) : ")
    
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
    
   
    dosya = open("bilgiler.txt", "a")
    
    for j in liste:
       dosya.write(j)
       dosya.write("\n")
    tercih = str(tercih)
    dosya.write(tercih)
    dosya.write("\n----------------------------\n\n")
    
    dosya.close()
    print("Rezervasyon Sisteme Kaydedildi...")
    
# =============================================================================
#    
#     
#    
# =============================================================================

def bilgiKontrol():

    print("Rezerv Kontrol")
    print("__________________")
    
    rezervBilgi = open("bilgiler.txt", "r")
    
    print(rezervBilgi.read())
    
    rezervBilgi.close()
    
# =============================================================================
#     
#     
#     
# =============================================================================

def odaNo():
    odalar = list()
    odalar.extend(m_Oda)
    odalar.extend(s_Oda)
    odalar.extend(d_Oda)
    print(odalar)

# =============================================================================
# 
# 
# 
# =============================================================================

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
        break
    else:
        print("Yanlis Islem")
        break
    



