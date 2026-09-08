
daftar_buku = ("Dasar Pemrograman", "Pengantar Teknologi Informasi", "Konsep Sistem Informasi", "Jaringan Komputer", "Pengenalan Basis Data")
pinjaman = []
print("DAFTAR BUKU PERPUSTAKAAN", daftar_buku)

while True:
    print("\n--- MENU PINJAMAN BUKU PERPUSTAKAAN ---")
    print("1. List buku pinjaman")
    print("2. Hapus buku dari list pinjaman")
    print("3. Selesai")

    pilihan = input("Silakan pilih opsi (1/2/3): ")

    if pilihan == "1":
        buku = input("Masukkan judul buku yang ingin dipinjam: ")

        if buku in daftar_buku:
            pinjaman.append(buku)
            print("Buku telah berhasil dipinjam.")
        else:
            print("Buku tidak tersedia.")
    
    elif pilihan == "2":
        if len(pinjaman) == 0:
            print("Belum ada buku yang dipinjam.")
        else:
            print("\nBuku yang sedang dipinjam:")
            for i, buku in enumerate(pinjaman, start=1):
                print(f"{i}. {buku}")

            hapus = input("Masukkan judul buku yang ingin dihapus: ")

            if hapus in pinjaman:
                pinjaman.remove(hapus)
                print("Buku berhasil dihapus dari daftar pinjaman.")
            else:
                print("Buku tersebut tidak ada didalam daftar pinjaman.")

    elif pilihan == "3":
        break

    else:
        print("Buku tidak ditemukan.")

print("\nDAFTAR AKHIR PINJAMAN BUKU:")

if len(pinjaman) == 0:
    print("Tidak ada buku yang dipinjam.")
else:
    for i, buku in enumerate(pinjaman, start=1):
        print(f"{i}. {buku}")

print("\nTerima kasih telah meminjam buku di perpustakaan.")