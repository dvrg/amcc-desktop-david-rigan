# Menggunakan Module

import sys
print('Commandline arguments :')
for i in sys.argv:
    """ 
        Kita dapat memberikan argumen
        saat menjalankan program python
    """
    print(i)

if __name__ == '__main__':
    print('Run itselt')
else:
    print('Run from another module')    

#print(sys.argv)
#print(sys.path)    

