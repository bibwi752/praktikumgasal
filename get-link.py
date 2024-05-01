import pyshorteners

Link_asli = input("Masukkan Link: ")
Shortener = pyshorteners.Shortener()
result = Shortener.tinyurl.short(Link_asli)
print(result)
