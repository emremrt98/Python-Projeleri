import sqlite3


con = sqlite3.connect("yayinevi.db")
cursor = con.cursor()

def kitapSilme(kitapAdi):
    cursor.execute("DELETE  FROM kitaplik WHERE Adı = (?)", kitapAdi)
    con.commit()
    
