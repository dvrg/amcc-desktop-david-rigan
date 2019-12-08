import datetime
print('waktu sekarang adalah :', datetime.datetime.now())
# >> waktu sekarang adalah : 2019-08-12 00:00:00:00

"""Variabel"""
mynow = datetime.datetime.now()
print(mynow)
# 2019-08-12 00:00:00:00

"""Mengabungkan integer & string"""
number = 10
string = 'David Rigan'
print(number, string)
# 10 David Rigan

"""Concating"""
x = 10
y = "10"
z = 10.1

print(x,y,z)
print(type(x), type(y), type(z))

"""Menggunakan Dir
Untuk mengetahui tipe atribut
"""
# >>> dir(list)

"""Menggunakan Help
Untuk mengetahui cara penggunaan sebuah fungsi
"""
# >>> help(list.sort)

"""List"""
student_grades = [9,8.7,7.8]
print(list(range(1,10)))
# [1,2,3,4,5,6,7,8,9]
print(list(range(1,10,2)))
# [1,3,5,7,9]

"""Calculating List"""
sum_list = sum(student_grades)
length_list = len(student_grades)
mean_of_list = sum_list / length_list
print('Nilai rata-rata list: ', mean_of_list)

"""Dictionary"""
my_dict = {"sabil": 90, "david": 78, "agung": 60, "yanuar": 96}
# ambil nilainya saja
my_dict_values = my_dict.values()
sum_dict = sum(my_dict.values())
length_dict = len(my_dict)
mean_of_list = sum_dict / length_dict
print('Nilai rata-rata dictionary: ', mean_of_list)

"""Tupple"""
my_tuple = (3,4,2,1)
my_tuple.append(6)
print(my_tuple)
my_tuple.remove(0)
print()
