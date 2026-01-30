while True:
    try:
        angka1 = int(input("Masukkan angka pertama: "))
        angka2 = int(input("Masukkan angka kedua: "))

        assert angka1 >= 0 and angka2 >= 0, "Angka tidak boleh negatif"

        hasil = angka1 + angka2

        print("Hasil penjumlahan:", hasil)

        break  

    except ValueError:
        print(" Input harus berupa angka!")

    except AssertionError as e:
        print(" Error:", e)

    finally:
        print("Program selesai\n")
