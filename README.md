# amcc-desktop-david-rigan
Projek pelatihan python dan github amcc desktop

# Bagaimana clone repository ini ?
1. buka halaman https://github.com/dvrg/amcc-desktop-david-rigan
2. pada pojok kanan, klik tombol clone or download
3. pilih ssh atau copy alamat ini `git@github.com:dvrg/amcc-desktop-david-rigan.git`
4. pada komputer kamu, buka git bash/terminal
5. ketikan `git clone git@github.com:dvrg/amcc-desktop-david-rigan.git`

# Bagaimana cara commit dan push ?
1. setelah melakukan perubahan, pastikan perubahan file dengan cara `git status`
2. tambahkan/simpan perubahan pada file dengan cara `git commit -am "pesan commit"`
3. pastikan seluruh perubahan sudah ter commit dengan cara `git status`
4. kirim perubahan dari staging area ke github dengan cara `git push`

## Kenapa pilih clone lewat ssh dari pada https ?
alasannya adalah, user diminta untuk terus-terusan login ketika menggunakan https namun jika menggunakan ssh tidak perlu login

# Alasan menggunakan bahasa python
Efektifitas Python cukup terbukti dengan banyaknya jumlah pengguna Bahasa ini. Berbagai survei memasukkan Python dalam top-3 sebagai bahasa dengan penggunaan terbanyak, bersaing dengan Java dan PHP. Python dapat digunakan dalam mengakomodasi berbagai gaya pemrograman, termasuk structured, prosedural, berorientasi-objek, maupun fungsional. Python juga dapat berjalan pada berbagai sistem operasi yang tersedia. Beberapa pemanfaatan bahasa Python di antaranya:

1.Web development (server-side)
2.Software development
3.Mathematics & data science
4.Machine learning
5.System scripting

Dan lain-lain.

# Memulai dengan python
Pastikan python sudah terinstall pada komputermu. Untuk mengecek nya, ketikan perintah berikut ini:
`python --version`

## Bagaimana jika python belum ter-install ?
ikuti tautan berikut ini : https://www.dicoding.com/academies/86/tutorials/4738?from=4736 (daftar dahulu akun dicoding yaa)

## Hello World dengan python
Masuk ke direktori folder repository ini dengan cara:
```bash
cd /path/nama-direktori
```
catatan : path disini merupakan nama-nama direktori diatas direktori repository ini, seperti misalnya Document
1. buat sebuah file baru dengan nama main.py, caranya berikut ini
```bash
nano main.py
```
2. masukan code berikut di dalam main.py
```python
print('hello world!')
```
3. jalankan file tersebut dengan cara
```bash
python main.py
```
4. hasil output harusnya sesuai dengan inputnya, yaitu:
```bash
hello world!
```

## Python Interpreter
1. Python interpreter merupakan program yang dibaca & di eksekusi pada sebuah sesi pada command line. Untuk masuk ke python interpreter, caranya sebagai berikut :

Buka cmd (windows) atau terminal (Linux/MacOS), lalu ketikan `python`

```python
➜ python
Python 3.7.5 (default, Nov 15 2019, 13:43:34)
[GCC 9.2.1 20191115 gcc-9-branch@278291] on linux

Type "help", "copyright", "credits" or "license" for more information.
>>>
```

lalu untuk keluar cmd atau terminal ketikan `CTRL` `+` `D`

## Menggunakan Modul
Module merupakan set program yang sudah disediakan oleh python yang tinggal pakai, contohnya adalah seperti ini :

```python
>>> import datetime
>>> datetime.datetime.now()
datetime.datetime(2019, 12, 1, 21, 39, 3, 233059)
```
sebagai contoh, pada kode di atas kita menggunakan module datetime untuk menampilkan tanggal dan jam pada saat ini. Lalu selanjutkan, kita akan menggunakan modul random untuk mengacak karakter alfabet seperti contoh kode di bawah ini :
```python
>>> import random
>>> import string
>>> def randomword(length):
...     letters = string.ascii_lowercase
...     return ''.join(random.choice(letters) for i in range(length))
>>> randomword(5)
>>> 'sadas'
```
lalu kita bakal buat program untuk mengacar nama dari seluruh pelatih desktop programming amcc dengan contoh kode berikut ini:
```python
>>> import random
>>> import string
>>> def random_name():
...     name = ('david', 'sabil', 'peby', 'agung', 'yanuar')
...     return ''.join(random.choice(name) for i in range(1))
>>> random_name
>>> 'david'
```

## Menggunakan Variabel
Variabel adalah tempat menyimpan data pada kode program, lalu bagaimana menggunakan variabel dan menampilkan isi variabel pada python ?

```python
import datetime

my_var = datetime.datetime.now()
print(my_var)
...
>>> 2019-12-08 20:44:08.035777
```

## Tipe Data
Dalam python ada berbagai macam tipe data mulai dari interger, string, float. list, dictionary hingga tuple. Didalam file basic.py sudah ada contoh bagaimana menggunakan berbagai macam file tersebut.