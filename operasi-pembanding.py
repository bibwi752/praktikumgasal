bil1=float(input("masukan bilangan pertama: "))
bil2=float(input("masukan bilangan kedua: "))
if bil1>bil2:
    print(f"{bil1} lebih besar{bil2}")
elif bil1<bil2:
    print(f"{bil1}lebih kecil dari{bil2}")
else:
    print(f"{bil1}sama dengan{bil2}")
    


# prgram 2
# input nilai ujian dari pengguna
nilai_ujian = float(input("masukkan nilai ujian: "))

# menentukan kategori berdasarkan nilai ujian menggunakan operator perbandingan
if nilai_ujian >= 90:
    kategori = "A"
elif nilai_ujian >= 80:
    kategori = "B"
elif nilai_ujian >= 70:
    kategori = "C"
elif nilai_ujian >= 60:
    kategori = "D"
else:
    kategori = "E"

# menampilkan hasil kategori
print(f"nilai ujian anda adalah {nilai_ujian}, sehingga masuk kategori: {kategori}")



#nilai ujian
nilai_ujian = str(input("masukan nilai ujian: "))

if nilai_ujian=="A":
    kategori="luar biasa"
elif nilai_ujian=="B":
     kategori="baik"
elif nilai_ujian=="C":
    kategori="cukup"
elif nilai_ujian=="D":
    kategori="kurang"
else:
     kategori="mengulangi"


