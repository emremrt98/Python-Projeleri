liste = [1] * 100000000

liste[0] = 0
liste[1] = 0
a = 2

while(a < len(liste)):
    
    k = a
    

    
    while(k * a < len(liste)):
        liste[k*a] = 0    
        k += 1
        
    a += 1
    
print(liste)