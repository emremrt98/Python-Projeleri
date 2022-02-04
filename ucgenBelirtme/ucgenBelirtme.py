# =============================================================================
#                       ÜÇGENİN İÇ AÇILARINI BULMA
# =============================================================================
import math

print("\n--------------------------")
print("Ad ve Soyad : Emre MERT\nOkul No : 203305028")
print("--------------------------")

while(1):
    
    kenarA = int(input("1.Kenari Gir : "))
    kenarB = int(input("2.Kenari Gir : "))
    kenarC = int(input("3.Kenari Gir : "))
    
    
    radyanA = math.acos((kenarB**2 + kenarC**2 - kenarA**2) / (2 * kenarB * kenarC))
    
    radyanB = math.acos((kenarA**2 + kenarC**2 - kenarB**2) /(2 * kenarA * kenarC))
    
    radyanC = math.acos((kenarB**2 + kenarA**2 - kenarC**2) /(2 * kenarA * kenarB))
    
    dereceA = math.degrees(radyanA)
    
    dereceB = math.degrees(radyanB)
    
    dereceC = math.degrees(radyanC)
    
    toplam = dereceA + dereceB + dereceC
    
    if(toplam != 180):
        print("Girdiginiz Aci Degerleri Bir Ucgen Belirtmiyor!!!\a")
        break
    
    print("Radyan cinsi A : {} Derece Cinsi A : {}\n".format(radyanA, dereceA))
    print("Radyan cinsi B : {} Derece Cinsi B : {}\n".format(radyanB, dereceB))
    print("Radyan cinsi C : {} Derece Cinsi C : {}\n".format(radyanC, dereceC))

    
