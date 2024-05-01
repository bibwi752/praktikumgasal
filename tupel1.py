
# #Cara mengakses nilai tuple

# tup1 = ('fisika', 'kimia', 1993, 2017)
# tup2 = (1, 2, 3, 4, 5, 6, 7 )

# print ("tup1[3]: ", tup1[3])
# print ("tup2[1:5]: ", tup2[1:2])


 


# tup5 = (12, 34.56)
# tup6 = ('abc', 'xyz')
# tup7 = tup5 + tup6
# print (tup7)



# tup = ('fisika', 'kimia', 1993, 2017)
# print(tup)

# # hapus tuple dengan statement del

# del tup

# # lalu buat kembali tuple yang baru dengan elemen yang diinginkan

# tup = ('Bahasa', 'Literasi', 2020)
# print("Setelah menghapus tuple :", tup)



# Definisikan tuple
nama_hewan = ("Kucing", "Anjing", "Burung", "Ikan")

# Akses elemen dalam tuple
print("Elemen pertama dalam tuple:", nama_hewan[0])
print("Elemen kedua dalam tuple:", nama_hewan[1])

# Menggabungkan dua tuple
nama_hewan_baru = nama_hewan + ("Ulat",)
print("Tuple yang telah digabungkan:", nama_hewan_baru)

# Menghitung jumlah elemen dalam tuple
jumlah_hewan = len(nama_hewan)
print("Jumlah elemen dalam tuple:", jumlah_hewan)

# Mengganti elemen dalam tuple
nama_hewan = ("Kucing", "Anjing", "Burung", "Ikan")
nama_hewan = nama_hewan[:2] + ("Ulat",) + nama_hewan[3:]
print("Tuple setelah mengganti elemen:", nama_hewan)



# nama_hewan = ("Kucing", "Anjing", "Burung", "Ikan"): Kita membuat tuple bernama nama_hewan yang berisi nama-nama hewan.

# print("Elemen pertama dalam tuple:", nama_hewan[0]): Kita akses elemen pertama dalam tuple menggunakan indeks 0 dan mencetaknya.

# print("Elemen kedua dalam tuple:", nama_hewan[1]): Kita akses elemen kedua dalam tuple menggunakan indeks 1 dan mencetaknya.

# nama_hewan_baru = nama_hewan + ("Ulat",): Kita menggabungkan tuple nama_hewan dengan tuple baru yang berisi nama hewan "Ulat".

# print("Tuple yang telah digabungkan:", nama_hewan_baru): Kita mencetak tuple yang telah digabungkan.

# jumlah_hewan = len(nama_hewan): Kita menghitung jumlah elemen dalam tuple nama_hewan menggunakan fungsi len().

# print("Jumlah elemen dalam tuple:", jumlah_hewan): Kita mencetak jumlah elemen dalam tuple.

# nama_hewan = nama_hewan[:2] + ("Ulat",) + nama_hewan[3:]: Kita mengganti elemen ketiga dalam tuple nama_hewan dengan nama hewan "Ulat".

# print("Tuple setelah mengganti elemen:", nama_hewan): Kita mencetak tuple setelah mengganti elemen.

# nama_hewan = nama_hewan[:2] + nama_hewan[3:]: Kita menghapus elemen ketiga dalam tuple nama_hewan.

# print("Tuple setelah menghapus elemen:", nama_hewan): Kita mencetak tuple setelah menghapus elemen.