import sqlite3
import time

con = sqlite3.connect("yayinevi.db")
cursor = con.cursor()


def kitapListesi():
 
    
    cursor.execute("SELECT * FROM kitaplik")
    veriler = cursor.fetchall()
    
    for i in veriler:
        print(i)
    
    
def cikis():
   
    print("Sistemden Cikiliyor...")    
    time.sleep(2)
    con.close()