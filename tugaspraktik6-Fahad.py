print("=" * 55)
print("Program Hitung Jumlah Kata dan Karakter dengan Python")
print("=" * 55)

kalimat = input("Masukkan Sebuah Kata: ")

kata = kalimat.split()

jumlah_kata = len(kata)

jumlah_karakter = len(kalimat)

hasil = []
for k in reversed(kata):
    hasil.append(k[::-1])

kalimat_terbalik = " ".join(hasil)

print("Jumlah Kata:", jumlah_kata)
print("Jumlah Karakter:", jumlah_karakter)
print("Jika dibalik akan menampilkan kata :", kalimat_terbalik)
print("=" * 55)
