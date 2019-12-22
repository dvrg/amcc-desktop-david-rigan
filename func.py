def square(x):
    """Calculate Square Value"""
    print("luas persegi dengan x =", x)
    return x*x

def password(x):
    if len(x) >= 8:
        print('password berhasil dibuat. Jumlah karakter', len(x))
    else:
        print('password gagal dibuat. Jumlah karakter', len(x))
