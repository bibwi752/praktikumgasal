# inisialisasi pesantren sebagainrumus (dictionary) untuk menyimpan data santri
pesantren = {}

while True:
    print("\nMenu:")
    print("1. Tambah Data Santri")
    print("2. Lihat Data Santri")
    print("3. Keluar")

    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == 'i':
        nama = input("Masukkan nama santri: ")
        usia = int(input("Masukkan usia santri: "))
        kelas = input ("Masukkan Kelas santri: ")
        Pesantren[nama] = {'Usia': usia, 'Kelas': Kelas}
        print(f"Data santri {nama} telah ditambah.") 

    elif pilihan == '2':
        if len(pesantren) == 0:
            print("Tidak ada data santri yang trsedia.")
        else:
                print("\nData santri:")
                for name, data in pesantren.items():
                    print(f"Nama: {nama}, usia: {data['usia']}, kelas: {data['kelas']}")

     elif pilihan == '3':
         print("Terima Kasih, program selesai.")
        break

     else:
        print("Pilihan tidak valid. silahkan pilihan 1, 2, atau 3.")




