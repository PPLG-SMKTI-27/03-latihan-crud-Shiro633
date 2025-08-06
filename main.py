# data buku
books = [
    {"isbn":"9786237121144", "judul":"Kumpulan Solusi Pemrograman Python", "pengarang":"Budi Raharjo", "jumlah":6, "terpinjam":0},
    {"isbn":"9786231800718", "judul":"Dasar-Dasar PPLG Vol. 2", "pengarang":"Okta Purnawirawan", "jumlah":15, "terpinjam":0},
    {"isbn":"9786026163905", "judul":"Rupture : Eternal End", "pengarang":"Aditya Nurkhalid Indrawan", "jumlah":20, "terpinjam":19},
    {"isbn":"9786022912828", "judul":"Animal Farm", "pengarang":"George Orwell", "jumlah":4, "terpinjam":0}
]

# data peminjaman
records = [
    {"isbn":"9786022912828", "status":"Selesai", "tanggal_pinjam":"2025-03-21", "tanggal_kembali":"2025-03-28"},
    {"isbn":"9786026163905", "status":"Belum", "tanggal_pinjam":"2025-07-22", "tanggal_kembali":""}
]

def tampilkan_data():
    print("DAFTAR BUKU")
    print(f"{'No':<3} {'ISBN':<15} {'Judul':<45} {'Pengarang':<25} {'Jumlah':<6} {'Terpinjam':<9}")
    for i, book in enumerate(books, start=1):
        print(f"{i:<3} {book['isbn']:<15} {book['judul']:<45} {book['pengarang']:<25} {book['jumlah']:<6} {book['terpinjam']:<9}")

def tambah_data():
    print("Menambahkan Buku")
    isbn = input("ISBN : ")
    judul = input("Judul Buku : ")
    pengarang = input("Pengarang Buku : ")
    jumlah = input("Jumlah Buku : ")
    terpinjam = input("Terpinjam : ")
    book = {"isbn": isbn, "judul": judul, "pengarang": pengarang, "jumlah": int(jumlah), "terpinjam": int(terpinjam)}
    books.append(book)
    print("Data berhasil ditambahkan!\n")

def edit_data():
    tampilkan_data()
    try:
        index = int(input("Pilih nomor buku yang ingin diedit: ")) - 1
        if 0 <= index < len(books):
            print("Tinggalkan kosong jika tidak ingin mengubah.")
            isbn = input(f"ISBN buku ({books[index]['isbn']}): ") or books[index]['isbn']
            judul = input(f"Judul buku ({books[index]['judul']}): ") or books[index]['judul']
            pengarang = input(f"Pengarang buku ({books[index]['pengarang']}): ") or books[index]['pengarang']
            jumlah_buku = input(f"Jumlah buku ({books[index]['jumlah']}): ")
            jumlah = int(jumlah_buku) if jumlah_buku else books[index]['jumlah']
            buku_terpinjam = input(f"Buku Terpinjam ({books[index]['terpinjam']}): ")
            terpinjam = int(buku_terpinjam) if buku_terpinjam else books[index]['terpinjam']
            
            books[index] = {"isbn": isbn, "judul": judul, "pengarang": pengarang, "jumlah": jumlah, "terpinjam": terpinjam}
            print("Buku berhasil diubah!\n")
        else:
            print("Nomor tidak valid.\n")
    except ValueError:
        print("Input tidak valid.\n")

def hapus_data():
    tampilkan_data()
    try:
        index = int(input("Pilih nomor buku yang ingin dihapus: ")) - 1
        if 0 <= index < len(books):
            deleted = books.pop(index)
            print(f"Buku '{deleted['judul']}' berhasil dihapus.\n")
        else:
            print("Nomor tidak valid.\n")
    except ValueError:
        print("Input tidak valid.\n")

def tampilkan_peminjaman():
    print("DAFTAR PEMINJAMAN")
    print(f"{'No':<3} {'ISBN':<15} {'Status':<10} {'Tanggal Pinjam':<15} {'Tanggal Kembali':<15}")
    for i, record in enumerate(records, start=1):
        print(f"{i:<3} {record['isbn']:<15} {record['status']:<10} {record['tanggal_pinjam']:<15} {record['tanggal_kembali'] or '-':<15}")
    print()

def tampilkan_belum():
    print("DAFTAR PEMINJAMAN YANG BELUM DIKEMBALIKAN")
    print(f"{'No':<3} {'ISBN':<15} {'Tanggal Pinjam':<15}")
    found = False
    for i, record in enumerate(records, start=1):
        if record['status'].lower() == "belum":
            found = True
            print(f"{i:<3} {record['isbn']:<15} {record['tanggal_pinjam']:<15}")
    if not found:
        print("Semua buku telah dikembalikan.")
    print()

def peminjaman():
    isbn = input("Masukkan ISBN buku yang ingin dipinjam: ")
    tanggal_pinjam = input("Masukkan tanggal pinjam (YYYY-MM-DD): ")

    for book in books:
        if book['isbn'] == isbn:
            if book['terpinjam'] < book['jumlah']:
                book['terpinjam'] += 1
                records.append({
                    "isbn": isbn,
                    "status": "Belum",
                    "tanggal_pinjam": tanggal_pinjam,
                    "tanggal_kembali": ""
                })
                print("Peminjaman berhasil dicatat.\n")
                return
            else:
                print("Semua salinan buku sudah dipinjam.\n")
                return
    print("ISBN buku tidak ditemukan.\n")

def pengembalian():
    isbn = input("Masukkan ISBN buku yang dikembalikan: ")
    tanggal_kembali = input("Masukkan tanggal kembali (YYYY-MM-DD): ")

    for record in records:
        if record['isbn'] == isbn and record['status'].lower() == "belum":
            record['status'] = "Selesai"
            record['tanggal_kembali'] = tanggal_kembali

            for book in books:
                if book['isbn'] == isbn:
                    book['terpinjam'] -= 1
                    print("Pengembalian berhasil dicatat.\n")
                    return
    print("Peminjaman yang cocok tidak ditemukan atau sudah dikembalikan.\n")

while True:
    print("---=== MENU ===---")
    print("[1] Tampilkan Data")
    print("[2] Tambah Data")
    print("[3] Edit Data")
    print("[4] Hapus Data")
    print("------------------")
    print("[5] Tampilkan Semua Peminjaman")
    print("[6] Tampilkan Peminjaman Belum Kembali")
    print("[7] Peminjaman")
    print("[8] Pengembalian")
    print("[X] Keluar")
    menu = input("Masukkan pilihan menu (1-8 atau X): ").upper()

    match menu:
        case "1":
            tampilkan_data()
        case "2":
            tambah_data()
        case "3":
            edit_data()
        case "4":
            hapus_data()
        case "5":
            tampilkan_peminjaman()
        case "6":
            tampilkan_belum()
        case "7":
            peminjaman()
        case "8":
            pengembalian()
        case "X":
            print("Terima kasih! Keluar dari program.")
            break
        case _:
            print("Pilihan tidak tersedia.\n")
