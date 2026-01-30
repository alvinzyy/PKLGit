from datetime import datetime
import time

# --- FASE 1: FUNGSI PENCATATAN LOG (APPEND) ---
def catat_log(aksi, user):
    """
    Fungsi ini mensimulasikan sistem yang sedang berjalan
    dan mencatat aktivitas ke file .log
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    nama_file_log = "security.log"
    
    # Menggunakan mode 'a' agar data lama tidak hilang
    with open(nama_file_log, "a") as f_log:
        f_log.write(f"[{timestamp}] EVENT: {aksi} | USER: {user}\n")
        print(f"Log dicatat: {aksi} oleh {user}")

# --- FASE 2: FUNGSI PEMBUATAN LAPORAN (READ -> WRITE) ---
def buat_laporan_txt():
    """
    Fungsi ini membaca file log mentah, dan memindahkannya
    ke file .txt dengan format laporan resmi.
    """
    print("\n--- Memulai Generasi Laporan ---")
    
    # Langkah A: Baca semua isi log
    try:
        with open("security.log", "r") as f_sumber:
            semua_data = f_sumber.readlines()
    except FileNotFoundError:
        print("Error: File log belum dibuat. Jalankan pencatatan dulu.")
        return

    # Langkah B: Tulis ke file laporan baru
    nama_file_laporan = "laporan_harian.txt"
    
    # Menggunakan mode 'w' untuk membuat file baru/menimpa laporan lama
    with open(nama_file_laporan, "w") as f_tujuan:
        # Menulis Header
        f_tujuan.write("========================================\n")
        f_tujuan.write(f"LAPORAN HARIAN KEAMANAN - {datetime.now().date()}\n")
        f_tujuan.write(f"Total Aktivitas: {len(semua_data)} kejadian\n")
        f_tujuan.write("========================================\n\n")
        
        # Memproses dan memindahkan data
        for baris in semua_data:
            # Membersihkan teks agar lebih rapi
            baris_rapi = baris.replace("EVENT:", "Kejadian:").replace("|", "-")
            f_tujuan.write(baris_rapi)
            
    print(f"Sukses! Laporan tersimpan di '{nama_file_laporan}'")

# --- EKSEKUSI PROGRAM ---

# 1. Simulasi aktivitas (Menulis ke .log)
catat_log("Pintu Utama Terbuka", "Satpam Budi")
time.sleep(1) # Jeda 1 detik agar timestamp beda
catat_log("Akses Ditolak (PIN Salah)", "Orang Asing")
time.sleep(1)
catat_log("Pintu Gudang Terkunci", "Admin Yanto")

# 2. Membuat Laporan (Baca .log -> Tulis .txt)
buat_laporan_txt()