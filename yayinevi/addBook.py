import sqlite3


con = sqlite3.connect("yayinevi.db")
cursor = con.cursor()

def kitapEkle(kitapAdi, yazarAdi, sayfaSayisi, yayinevi, fiyat):
    cursor.execute("CREATE TABLE IF NOT EXISTS kitaplik (Adı, Yazar Adı, Sayfa No, Yayınevi, Fiyat)")
    cursor.execute("INSERT INTO kitaplik VALUES (?, ? , ? , ?, ?)", (kitapAdi, yazarAdi, sayfaSayisi, yayinevi, fiyat))
    con.commit()





