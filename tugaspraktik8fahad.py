
def input_angka(pesan):
    while True:
        try:
            nilai = float(input(pesan))
            return nilai
        except ValueError:
            print("⚠️  Peringatan: Input harus berupa angka! Silakan coba lagi.")


def fungsi_total_nilai(nilai_harian, uts, uas):
    nilai_harian = nilai_harian * 0.3
    uts = uts * 0.3
    uas = uas * 0.4

    total = nilai_harian + uts + uas
    return total


def fungsi_cek_nilai(total):
    if total >= 80:
        return "A"
    elif total >= 70:
        return "B"
    elif total >= 60:
        return "C"
    elif total >= 50:
        return "D"
    else:
        return "E"


def fungsi_nilai():
    total_semua = 0

    print("===================================")
    print(" Program Hitung Nilai dengan Fungsi ")
    print("===================================")

    for i in range(1, 3):
        print(f"\n------ Nilai Ke {i} ------")

        nilai_harian = input_angka("Nilai Harian : ")
        uts = input_angka("Nilai UTS    : ")
        uas = input_angka("Nilai UAS    : ")

        total = fungsi_total_nilai(nilai_harian, uts, uas)
        total_semua += total

    rata_rata = total_semua / 2
    nilai_huruf = fungsi_cek_nilai(rata_rata)

    print("\n------ Total Nilai ------")
    print(f"Total nilai didapat : {rata_rata}")
    print(f"Total nilai dalam huruf : {nilai_huruf}")
    print("===================================")

fungsi_nilai()
