def square(x):
    """Calculate Square Value"""
    print("luas persegi dengan x =", x)
    return x*x

def password(x):
    if len(x) >= 8:
        print('password berhasil dibuat. Jumlah karakter', len(x))
    else:
        print('password gagal dibuat. Jumlah karakter', len(x))

def area(a, b=8):
    return a*b

#print(area(a=7)) # Parameter dengan argument

def mean(*args):
    return sum(args)

#def mean(**kwargs):

#print(mean(1,2,3))

#print(mean(x=1,y=2,z=3))

# buat sebuah fungsi, foo(10, 20, 30 40) dimana, nilai yang dikirimkan ini harus mengembalikan nilai 25,
# yaitu rata2 dari nilai yang dikirim


def foo(*args):
    return sum(args) / len(args)

#print(foo(10,20,30,40)) 

# buat sebuah fungsi dimana jika fungsi func("api", "air", "udara", "tanah") bakal mengembalikan ["API", "AIR", "UDARA", "TANAH"]
# buat urutan datanya ascending (A-Z) jadi ["AIR", "API", "TANAH", "UDARA"]

def func(*args):
    args = [x.upper() for x in args]
    return sorted(args, reverse=True)

print(func("api", "air", "udara", "tanah"))