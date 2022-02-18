str1 = "aku cinta indonesia"
print(str1)

str2 = str1[:10]+'tanah airku'+str1[9:]
print(str2)

str3 = 'aku cinta tanah air ku indonesia'
str4 = str3[:9]+''+str3[22:]
print(str4)

kelas = 'Praktikum Pemrograman Berorientasi Objek'
up = kelas.upper()
lo = kelas.lower()
print(kelas)
print(up)
print(lo)

s = '     python     '
print(s.strip())
print(s.lstrip())
print(s.rstrip())

print(len(kelas))

jumlah = len(kelas)
print('panjang string adalah :',jumlah)

s1 = 'python '
s2 = 'programing'
print(s1+s2)

print(kelas.index('a'))
print(kelas)

kelas2 = kelas.replace('Praktikum','praktik')
print(kelas2)

a = 'satu'
b = 'dua'
c = 'tiga'
print('saya mempunyai %s mangga'%(b))

print(kelas.split())

# input1 = input('hari ini adalah : ')
# print(input1)

# data1 = input('angka 1 : ')
# data2 = input('angka 2 : ')
# data3 = int(data1)+int(data2)
# print(data1,' * ',data2,' = ',data3)

list1 = [1,2,3,4,5,6,7,8,9]
# print(list1)
# print(list1[5])
# print(list1[:3])
# print(len(list1))
# print(list1[10-3:])
# print(list1[2:9])
# print(list1[-10])
# print(list1[0])
# list1.append(10)
# print(list1)
# list1.insert(1,11)
# print(list1)

list2 = ['hello']
list1.extend(list2)
print(list1)

list1.extend('hai')
print(list1)

del list1[1]
print(list1)

list1.remove(5)
print(list1)

list1.pop()
print(list1)

a = [50,20,30,40]
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)
print(min(a))
print(max(a))
d = {1:100,2:200,3:300,4:400,5:500}
print(d)
print(d[2])
print(d.get(4))
print(d.keys())
print(d.values())
del d[3]
print(d)
d.clear()
len(d)

#tuple
t=(100,200,300,400)
print(t)
print(t[0])
print(t[3])
print(t.index(200))
t2=(10,20,10,30,10,40,20)
print(t2.count(20))
print(t2.count(10))
print(t2.count(30))

#yang ditambahkan
#contoh a
himpunan_nama_buah = {'anggur', 'jeruk', 'apel', 'nanas'}
print(himpunan_nama_buah)

#contoh b
himpunan_nama_bunga = set(['mawar', 'anggrek', 'melati'])
print(himpunan_nama_bunga)

#contoh c
himpunan_angka = {'1', '2', '3'}
print(himpunan_angka)

#mwnambahkan satu persatu
himpunan_angka.add('1')
himpunan_angka.add('2')
himpunan_angka.add('3')
himpunan_angka.add('4')
himpunan_angka.add('5')
himpunan_angka.add('6')
himpunan_angka.add('7')

# menambah lebih dari satu anggota sekaligus
himpunan_angka.update({ '8', '9' })

# bisa juga menggunakan list
himpunan_angka.update(['5', '6'])

print(himpunan_angka)

#contoh d
# set integer 
my_set = {3,4,5} 
print(my_set) 

# set dengan menggunakan fungsi set() 
my_set = set([6,7,8]) 
print(my_set) 

# set data campuran 
my_set1 = {7,8,9, "Python", (1,2,3)} 
print(my_set1) 

my_set2 = {'bunga', 'buah', 12, True, ('Y', 'N')}
print(my_set2)


print('bybell')


#BELLA TRIANA
5210411175
