# import time; # Digunakan untuk meng-import modul time
# ticks = time.time()
# print ("Berjalan sejak 12:00am, January 1, 1970:", ticks) #untuk python 3 gunakan tanda kurung, print()


# import time; # Digunakan untuk meng-import modul time
# ticks = time.time()
# print ("Berjalan sejak 12:00am, January 1, 1970:", ticks) #untuk python 3 gunakan tanda kurung, print()


import time

localtime = time.localtime(time.time())
print("Waktu lokal saat ini :", localtime) #gunakan tanda kurung, print()



import time

localtime = time.asctime( time.localtime(time.time()) )
print("Waktu lokal saat ini :", localtime)




import calendar

cal = calendar.month(2024, 3)
print("Dibawah ini adalah kalender:")
print(cal)



import calendar

tahun = 2024

for bulan in range(1, 13):
    cal = calendar.month(tahun, bulan)
    print(f"\nDibawah ini adalah kalender untuk bulan {bulan} tahun {tahun} :")
    print(cal)