# Studi_Kasus_3_Adhwa_Maysura
Nama : Adhwa Maysura<br>
Nim : 2609116103<br>
Golongan : Ganjil<br> 

# Peminjaman Buku Perpustakaan FT
<img width="1920" height="401" alt="1" src="https://github.com/user-attachments/assets/09ed797f-4ec8-4f83-9381-f930c3ec7f1e"> 

 1. Membuat daftar buku
Bagian ini membuat tuple bernama daftar_buku.
Tuple digunakan karena daftar buku perpustakaan dianggap tetap dan tidak akan diubah selama program berjalan.<br>

 2. Membuat tempat untuk menyimpan buku yang dipinjam
pinjaman = []
pinjaman adalah list kosong.Berbeda dengan daftar_buku, isi pinjaman akan berubah-ubah.<br>

 3. Menampilkan daftar buku
print("DAFTAR BUKU PERPUSTAKAAN", daftar_buku)
Kode ini menampilkan isi daftar_buku ke layar.<br>

 4. Membuat perulangan menu
while True:
while True digunakan untuk membuat program terus berjalan.
Program akan terus menampilkan menu sampai pengguna memilih pilihan 'selesai'<br>

 5. Meminta pilihan pengguna
pilihan = input("Silakan pilih opsi (1/2/3): ")
input() digunakan untuk menerima masukan dari pengguna.<br>


<img width="1920" height="242" alt="2" src="https://github.com/user-attachments/assets/4aa56f2f-b7a4-4777-91c6-464bcfb3f601" /><br>

 1. lalu untuk if pilihan == "1":
Artinya:
Jika pengguna memilih angka 1, jalankan perintah di bawahnya.
Kemudian:
buku = input("Masukkan judul buku yang ingin dipinjam: ")
Program meminta pengguna memasukkan judul buku,<br>

 2. if buku in daftar_buku:
            pinjaman.append(buku)
maka dengan code ini pengguna bebas menentukan buku yang akan dipinjam di perpustakan FT tersebut. Namun buku tidak masuk dalam menu maka output akan otomatis menampilkan "Buku Tidak Tersedia"<br>

<img width="1920" height="225" alt="3" src="https://github.com/user-attachments/assets/80885ff2-e45b-4be2-b20e-940074192067" /><br>

 1. Jika memilih menu 2
elif pilihan == "2":<br>
Jadi kalau pengguna memilih: 2
program akan otomatis menghapus list buku sesuai dengan permintaan pengguna.<br>

 2. Lalu untuk menggunakan for dan enumerate
for i, buku in enumerate(pinjaman, start=1):
    print(f"{i}. {buku}")
Ini digunakan untuk menampilkan daftar buku beserta nomor urutnya<br>


<img width="1918" height="241" alt="4" src="https://github.com/user-attachments/assets/d098bdc8-7916-44c7-8f16-b9c49686b9fe" /><br>

  1. Namun jika pengguna meminta beberapa list buku yang ingin dihapus bisa menggunakan code berikut :<br>
  *hapus = input("Masukkan judul buku yang ingin dihapus: ")* <br>
maka sistem akan otomatis menghapus buku dari list pinjaman sesuai dengan permintaan pengguna, sebelum itu sistem akan mengecek terlebih dahulu apakah buku ada di daftar pinjaman melalui code :<br>
  *if hapus in pinjaman*


<img width="1920" height="190" alt="5" src="https://github.com/user-attachments/assets/82833913-4f04-4c4d-999f-d389140d4e1a" /><br>

 1. Jika pengguna memilih menu 3<br>
elif pilihan == "3":
    break<br>
akan menghentikan while True.

<img width="1920" height="283" alt="6" src="https://github.com/user-attachments/assets/36a2feb7-f239-49fc-b3a0-79d168ee4eae" /><br>

 1. Menampilkan daftar akhir
Setelah pengguna memilih 3, program keluar dari while.<br>
Kemudian:<br>
print("\nDAFTAR AKHIR PINJAMAN BUKU:")
Program menampilkan daftar buku yang akhirnya dipinjam. <br>

 2. Lalu akan mengecek apakah daftar pinjaman kosong<br>
*if len(pinjaman) == 0:*<br>
    print("Tidak ada buku yang dipinjam.")
Jika tidak ada buku:<br>

 3. Jika ada buku yang dipinjam, pinjaman tidak kosong:<br>
else:
    *for i, buku in enumerate(pinjaman, start=1):
        print(f"{i}. {buku}")*<br>
        Program akan menampilkan seluruh buku yang masih ada dalam daftar pinjaman.

 4. Menampilkan ucapan terakhir<br>
*print("\nTerima kasih telah meminjam buku di perpustakaan.")*<br>
Ini merupakan pesan penutup program:
*Terima kasih telah meminjam buku di perpustakaan.*

















