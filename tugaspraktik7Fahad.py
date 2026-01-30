print("=" * 60)
print("Program Data Siswa dengan Python")
print("=" * 60)

data_siswa = []

while True:
    print("\n========================")
    print("1. Tambah data siswa")
    print("2. Tampilkan data siswa")
    print("3. Hapus data siswa")
    print("0. Keluar")
    print("========================")

    pilihan = input("Masukan pilihan kamu : ")

    if pilihan == "1":
        input_nis = input("Masukan NIS : ")
        nis_ada = False
        for siswa in data_siswa:
            if siswa["nis"] == input_nis:
                nis_ada = True
                break

        if nis_ada:
            print("NIS sudah terdaftar. Data tidak boleh sama.")
        else:
            input_nama = input("Masukan Nama Siswa : ")
            input_asal = input("Masukan Asal Sekolah : ")

            data_siswa.append({
                "nis": input_nis,
                "nama": input_nama,
                "asal": input_asal
            })

            print("Data siswa berhasil ditambahkan!")

    elif pilihan == "2":
        if len(data_siswa) == 0:
            print("Data siswa masih kosong.")
        else:
            print("\nData Siswa:")
            for i in range(len(data_siswa)):
                print("------------------------")
                print("NIS  :", data_siswa[i]["nis"])
                print("Nama :", data_siswa[i]["nama"])
                print("Asal :", data_siswa[i]["asal"])

    elif pilihan == "3":
        hapus_nis = input("Masukan NIS yang akan dihapus : ")
        ditemukan = False

        for i in range(len(data_siswa)):
            if data_siswa[i]["nis"] == hapus_nis:
                del data_siswa[i]
                ditemukan = True
                print("Data siswa berhasil dihapus.")
                break

        if not ditemukan:
            print("Data siswa dengan NIS tersebut tidak ditemukan.")

    elif pilihan == "0":
        print("Terima kasih, program selesai.")
        break

    else:
        print("Pilihan tidak valid!")
