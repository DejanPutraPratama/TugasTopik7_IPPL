# Function untuk menentukan nilai_maksimal
def nilai_maksimal(DeretBilangan):
    NilaiTerbesar = DeretBilangan[0]

    for nilai in DeretBilangan:
        if nilai > NilaiTerbesar:
            NilaiTerbesar = nilai

    return NilaiTerbesar

# Function untuk menentukan nilai_minimum
def nilai_minimal(DeretBilangan):
    NilaiTerkecil = DeretBilangan[0]

    for nilai in DeretBilangan:
        if nilai < NilaiTerkecil:
            NilaiTerkecil=nilai
    
    return NilaiTerkecil

# Berisi list-list angka
angka = [3,20,100,-35,50]

print(angka)
print("Nilai terkecil ialah : ", nilai_minimal(angka))
print("Nilai terbesar ialah : ", nilai_maksimal(angka))

