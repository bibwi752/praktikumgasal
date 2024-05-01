# dict = {'Name': 'Habib', 'Age': 16, 'Class': '1 int'}
# print ("dict['Name']: ", dict['Name'])
# print ("dict['Age']: ", dict['Age'])
# print(dict)



# biodata = {'Name': 'Habib', 'Age': 16, 'Class': '1 int'}
# biodata['Name'] = 'Habib wicaksono' 
# biodata['School'] = "Pesantren Teknologi Majapahit" 
# print(biodata)



# del biodata ['Name']
# print (biodata)
# biodata .clear()
# print (biodata )
# del biodata
# print (biodata)



# Membuat dictionary sederhana
mahasiswa = {
    "nama": "Alice",
    "nim": "12345678",
    "prodi": "Sistem Informasi",
    "ipk": 3.5
}

# Mengakses nilai dalam dictionary
print("Nama:", mahasiswa["nama"])
print("NIM:", mahasiswa["nim"])
print("Prodi:", mahasiswa["prodi"])
print("IPK:", mahasiswa["ipk"])

# Mengubah nilai dalam dictionary
mahasiswa["nim"] = "87654321"
mahasiswa["ipk"] = 3.7

# Menghapus nilai dalam dictionary
del mahasiswa["prodi"]

# Mengakses nilai yang telah diubah atau dihapus
print("NIM:", mahasiswa["nim"])
print("IPK:", mahasiswa["ipk"])

# Menggunakan loop untuk mengakses nilai dalam dictionary
for key, value in mahasiswa.items():
    print(f"{key}: {value}")




    




