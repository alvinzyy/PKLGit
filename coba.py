buah = ["apel", "jeruk", "mangga", "pisang"]

print("Daftar buah:")
for i in range(len(buah)):
    print(f"{i+1}. {buah[i]}")

pilih = int(input("Pilih nomor buah yang mau diganti: "))
buah_baru = input("Masukkan nama buah baru: ")

buah[pilih - 1] = buah_baru

print("Hasil akhir:", buah)
