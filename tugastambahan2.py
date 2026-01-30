# Program Log Filtering & Reporting
# Menyaring log berbahaya dari file security.log

def buat_laporan_txt():
    # Nama file input dan output
    file_log = "security.log"
    file_laporan = "laporan_bahaya.txt"

    # Counter untuk menghitung jumlah ancaman
    total_bahaya = 0

    # Membuka file log untuk dibaca
    with open(file_log, "r") as log:
        # Membuka file laporan untuk ditulis
        with open(file_laporan, "w") as laporan:
            # Header laporan
            laporan.write("-- LAPORAN PERINGATAN KEAMANAN ---\n\n")

            # Membaca file log baris per baris
            for baris in log:
                # Cek apakah baris mengandung kata berbahaya
                if "Ditolak" in baris or "Salah" in baris:
                    laporan.write(baris)
                    total_bahaya += 1

            # Menulis total ancaman di bagian bawah
            laporan.write("\n---------------------------------\n")
            laporan.write(f"Total ancaman ditemukan: {total_bahaya}\n")

    print("Laporan berhasil dibuat:", file_laporan)


# Memanggil fungsi
buat_laporan_txt()
