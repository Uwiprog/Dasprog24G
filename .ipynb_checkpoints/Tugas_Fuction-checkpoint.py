def Reverse_kata(kalimat):
    kata_list = kalimat.split()
    return ' '.join([kata [::-1] for kata in kata_list])

def urut_kata(kalimat, urutan):
    kata_list = kalimat.split()
    return ' '.join([kata_list[i - 1] for i in urutan])

def ganti_vokal(kalimat, opsi):
    vokalkecil = {'a':'4','i':'1','u':'|_|','e':'3','o':'0'}
    vokalbesar = {'A':'4','I':'1','U':'|_|','E':'3','O':'0'}
    hasil = ''
    for huruf in kalimat:
        if opsi == 1 and huruf in vokalkecil:
            hasil += vokalkecil[huruf]
        elif opsi == 2 and huruf in vokalbesar:
            hasil += vokalbesar[huruf]
        else:
            hasil += huruf
    return hasil

print("Ini adalah output perintah langsung menggunakan print() atau HARDCODE")
print("1. Ubah kata 'AKU CINTA KAMU'")
print(Reverse_kata("AKU CINTA KAMU"))
print("2. Urutkan kata 'HARI INI SEDANG BELAJAR PYTHON'")
print(urut_kata("HARI INI SEDANG BELAJAR PYTHON", [5,1,4,3,2]))
print("3. ganti huruf fokal kecil dari kata ""Aku Cinta Kamu")
print(ganti_vokal ("Aku Cinta Kamu", 1))
print("4. ganti huruf vokal besar dari kata" "Aku Cinta Kamu")
print(ganti_vokal ("Aku Cinta Kamu", 2))