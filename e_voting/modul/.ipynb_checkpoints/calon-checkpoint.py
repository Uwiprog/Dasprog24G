calon = []

def tambah_calon():
    id_calon = input("Masukkan ID calon (misal CL001): ")
    nama = input("Masukkan nama calon: ")
    visi = input("Masukkan visi dan misi calon: ")

    for c in calon:
        if c["id"] == id_calon:
            print("ID calon sudah terdaftar!")
            return

    calon.append({
        "id": id_calon,
        "nama": nama,
        "visi": visi,
        "jumlah_suara": 0
    })

    print("Calon berhasil ditambahkan.")