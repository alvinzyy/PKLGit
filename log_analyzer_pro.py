# Program Log Filtering & Reporting
# Menyaring log berbahaya dari file security.log

def buat_laporan_txt():
    file_log = "security.log"
    file_laporan = "laporan_bahaya.txt"
    total_bahaya = 0

    with open(file_log, "r") as log:
        with open(file_laporan, "w") as laporan:
            laporan.write("-- LAPORAN PERINGATAN KEAMANAN ---\n\n")

            for baris in log:
                baris_lower = baris.lower()

                if "ditolak" in baris_lower or "salah" in baris_lower:
                    laporan.write(baris)
                    total_bahaya += 1

            laporan.write("\n---------------------------------\n")
            laporan.write(f"Total ancaman ditemukan: {total_bahaya}\n")

    print("Laporan berhasil dibuat:", file_laporan)


buat_laporan_txt()
