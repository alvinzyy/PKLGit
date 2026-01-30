# Program Sederhana Python
# Tugas Akhir GamelaB

while True:
    print("==============================================")
    print("Selamat Datang di Program Sederhana dengan Python")
    print()
    print("Pilihlah pilihan dibawah ini :")
    print("1. Persegi Panjang")
    print("2. Rata-rata Nilai")
    print("3. Cek Bilangan ganjil atau genap")
    print("4. Jumlah Huruf Vokal")
    print("5. Keluar")

    pilihan = input("Masukkan pilihan kamu: ")

    # PERSEGI PANJANG
    if pilihan == "1":
        try:
            panjang = int(input("Masukkan panjang: "))
            lebar = int(input("Masukkan lebar: "))
            luas = panjang * lebar
            print("Luas persegi panjang:", luas)
        except:
            print("Input tidak valid! Harus berupa angka.")

    # RATA-RATA NILAI
    elif pilihan == "2":
        try:
            jumlah = int(input("Masukkan jumlah nilai (maks 5): "))

            if jumlah > 5 or jumlah <= 0:
                print("Jumlah nilai harus antara 1 sampai 5!")
            else:
                total = 0
                for i in range(jumlah):
                    nilai = int(input("Nilai ke-" + str(i+1) + ": "))
                    total = total + nilai

                rata = total / jumlah
                print("Rata-rata nilai:", rata)
        except:
            print("Input tidak valid! Masukkan angka.")

    # GANJIL GENAP
    elif pilihan == "3":
        try:
            angka = int(input("Masukkan angka: "))
            if angka % 2 == 0:
                print("Angka", angka, "adalah genap")
            else:
                print("Angka", angka, "adalah ganjil")
        except:
            print("Input tidak valid! Masukkan angka.")

    # HURUF VOKAL
    elif pilihan == "4":
        teks = input("Tuliskan teks: ")
        teks = teks.lower()

        print("Jumlah huruf:", len(teks))
        print("vokal a ada sebanyak", teks.count("a"))
        print("vokal i ada sebanyak", teks.count("i"))
        print("vokal u ada sebanyak", teks.count("u"))
        print("vokal e ada sebanyak", teks.count("e"))
        print("vokal o ada sebanyak", teks.count("o"))

    # KELUAR
    elif pilihan == "5":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia! Masukkan angka 1-5.")

# LOOPING
    ulang = input("Coba lagi [Y/N]? ")
    if ulang.lower() != "y":
        print("Program selesai.")
        break
