nis = input("MASUKKAN NIS = ")
nama = input("MASUKKAN NAMA SISWA = ")
mapel = input("MASUKKAN MATA PELAJARAN = ")

absensi = float(input("MASUKKAN NILAI ABSENSI = "))
tugas = float(input("MASUKKAN NILAI TUGAS = "))
uts = float(input("MASUKKAN NILAI UTS = "))
uas = float(input("MASUKKAN NILAI UAS = "))

nilai_akhir = (0.20 * absensi) + (0.25 * tugas) + (0.25 * uts) + (0.30 * uas)

if nilai_akhir >= 90:
    keterangan = "Memuaskan"
elif nilai_akhir >= 80:
    keterangan = "Baik"
elif nilai_akhir >= 70:
    keterangan = "Cukup"
else:
    keterangan = "Tidak Lulus"
str = '='
print (str * 49)
print("Program Hitung Nilai Mata Pelajaran dengan Python")
print (str * 49)
print("NIS            =", nis)
print("NAMA           =", nama)
print("MATA PELAJARAN =", mapel)
print("")
print("NILAI AKHIR    =", round(nilai_akhir, 2))
print("")
print("Keterangan     :", keterangan)