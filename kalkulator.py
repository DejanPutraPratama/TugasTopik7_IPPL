# Menghasilkan Output berupa menu
print("Operasi Matematika")
print(" 1. Jumlah \t [+]")
print(" 2. Kurang \t [-]")
print(" 3. Kali \t [*]")
print(" 4. Pembagian \t [/]")
print ('=' * 25)

# Menghasilkan Output berupa inputan 
operasi = input('Pilih operasi (1/2/3/4) \t : ')
print ('=' * 25)
bilangan1 = eval(input("Masukkan bilangan pertama \t : "))
bilangan2 = eval(input("Masukkan bilangan kedua \t : ")) 

print ('=' * 25)

# Function untuk perhitungan mulai dari penambahan, pengurangan, pembagian, dan perkalian 
# Menggunakan tiga parameter yaitu operasi, bilangan1, dan bilangan2
def hitung(operasi, bilangan1, bilangan2):
    
    try:
        if operasi == '1' :
            hasil = int(bilangan1) + int(bilangan2)
            print(f'Hasil dari {bilangan1} + {bilangan2} = ', hasil)
            return hasil
        elif operasi == '2' :
            hasil = int(bilangan1) - int(bilangan2)
            print(f'Hasil dari {bilangan1} - {bilangan2} = {hasil}')
            return hasil
        elif operasi == '3' :
            hasil = int(bilangan1) * int(bilangan2)
            print(f'Hasil dari {bilangan1} * {bilangan2} = {hasil}')
            return hasil
        elif operasi == '4' :
            hasil = int(bilangan1) / int(bilangan2)
            print(f'Hasil dari {bilangan1} / {bilangan2} = {int(hasil)}')
            return hasil
        else :
            print("Gak jelass")
            raise
        
    except Exception as e:
        raise ValueError('Invalid nilai')

hitung(operasi, bilangan1, bilangan2)