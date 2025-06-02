pemilih = []

def tambah_pemilih():
    id = input("Masukkan nomor ID mu: ")
    nama = input("Masukkan nama anda: ")
    jurusan = input("Masukkan prodi atau jurusan: ")

    # Cek apakah ID sudah ada
    for p in pemilih:
        if p["id"] == id:
            print("ID sudah terdaftar!")
            return

    pemilih.append({
        "id": id,
        "nama": nama,
        "jurusan": jurusan,
        "sudah_memilih": False
    })

    print("Pemilih berhasil ditambahkan.")