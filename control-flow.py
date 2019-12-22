number = 23
running = True

while running:
    guess = int(input('Masukan Angka Tebakan : '))

    if guess == number:
        print('Tebakan kamu benar!')
        running = False
    elif guess < number:
        print('Masih salah. Clue: Angka lebih besar dari', guess)
    else:
        print('Masih salah. Clue: Angka lebih kecil dari', guess)

else:
    print('Program berakhir.')

print('Selesai')