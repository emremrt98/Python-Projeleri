# =============================================================================
#                           ASAL ÇARPAN BULMA
# =============================================================================

print("\n--------------------------")
print("Ad ve Soyad : Emre MERT\nOkul No : 203305028")
print("--------------------------")

while(1):
    
    sayi = input("Sayi Gir : ")
    
    if(sayi == 'q'):
        print("Islem Sonlandiriliyor...")
        break
    else:
        sayi = int(sayi)
        
        for i in range(2,sayi+1):
            while(sayi % i == 0):
                sayi = sayi / i
                print(i)
            

                
        
                
        
        