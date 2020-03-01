suhu_minggu = [9.1, 6.7, 5.4]

# make round number for the float
#print(round(suhu_minggu[0]))


# loop over array
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]

# for color in colors:
#     if color > 50 and type(color) is int:
#         print(color)

# loop over dictionary
phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for key, value in phone_numbers.items():
    print("{} phone number is {}".format(key, value))

for value in phone_numbers.values():
    print("{}".format(value.replace('+', '00')))

    