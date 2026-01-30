try:
    angka = int(input("Masukkan bilangan: "))
    hasil = 10 / angka
    print("Hasil:", hasil)
except ZeroDivisionError:
    print("Error: division by zero (pembagian dengan nol)")
