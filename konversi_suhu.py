import os, sys

def mulai():
    pilihan = input('Masukan Pilihan (b) Binner ke Decimal, (s) Konversi Suhu. (b/s) ? :')
    pilihan_tolower = pilihan.lower()
    if pilihan_tolower == 's':
        nilai = float(input('Masukan suhu awal Celcius :'))
        tipe = input('Konversi ke k/f/r :')
        suhu(nilai, tipe)
    elif pilihan_tolower == 'b':
        biner = input('Masukan angka biner :')
        bin_to_dec(biner)
    else:
        print('Input salah!')

    confirm()

def suhu(nilai, tipe):
    tipe_lower = tipe.lower()
    if tipe_lower == 'k':
        kel = nilai + 273.15
        print(f'{nilai} Celcius, {kel} Kelvin')
    elif tipe_lower == 'f':
        fah = (nilai * (9/5)) + 32
        print(f'{nilai} Celcius, {fah} Fahreinheit')
    elif tipe_lower == 'r':
        rea = nilai * (4/5)
        print(f'{nilai} Celcius, {rea} Reamur')
    else:
        print('Tipe salah!')        
    
    confirm()

def bin_to_dec(param):
    bin = int(param, 2)
    print(f'{param} Biner = {bin}') 
    confirm()

def confirm():
    while True:
        s = input('Ulangi lagi? (y/t) : ')
        if s == 't':
            break
        elif s == 'y':
            cls()
            mulai()
        break          

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

if __name__ == '__main__':
    mulai()

