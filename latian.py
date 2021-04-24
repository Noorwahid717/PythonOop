a = 44
f = 44
if f > a:
    print("f lebih besar dari a")
elif a == f:
    print("a dan f adalah sama")

          
a = 300
h = 44
if h > a:
    print("h lebis besar dari a")
elif a == h:
    print("a dan h adalah sama")
else:
    print("a lebih besar dari h")






jumlah = 5
nomer = 717
harga = 700
pesananku = "Aku ingin {0} buat {0} orang dari item nomer {1} untuk {2:.3f} rupiah"
print(pesananku.format(jumlah, nomer, harga))






username = input("Masukan Namamu:")
print("Nama Pengguna adalah: " + username)




j = 480
w = 30
if j > w:
    print("j lebih besar dari w")
else:
    print("w tidak lebih besar dari j")


if a > h: print("a lebih besar dari h")

t = 3
q = 209
print("T") if t > q else print("Q")

def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

def my_function(country= "Norway"):
    print("I am from " + country)







        

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#     pass

# x = Student("Mike", "Wahid")
# x.printname()




# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")

# def my_function(food):
#     for x in food:
#         print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)


# def my_function(x):
#     return 83 * x

# print(my_function(46))
# print(my_function(42))
# print(my_function(24))

# def tri_recursion(k):
#     if(k > 0):
#         result = k + tri_recursion(k - 1)
#         print(result)
#     else:
#         result = 0
#     return result

# print("\n\nRecursion example Result")
# tri_recursion(9)


# x = lambda a : a + 5
# print(x(7))


# y = lambda b, c : b * c
# print(y(10, 4))


# z = lambda d, f, g : d + f + g
# print(z(5, 10, 15))


# def myfunc(n):
#     return lambda i : i * n

# mydoubler = myfunc(2)

# print(mydoubler(30))


# def myfunc(j):
#     return lambda a : a * j

# mytripler = myfunc(3)
# myquader = myfunc(4)

# print(mytripler(20))
# print(myquader(40))


# class Kelasku:
#     x = 5

# print(Kelasku)


# class Kelasmu:
#     x = "10kelas"

# p1 = Kelasmu
# print(p1.x)


# class Person:
#   def __init__(diri, nama, umur):
#      diri.nama = nama
#      diri.umur = umur

#   def myfunc(diri):
#      print("Hallo nama saya adalah " + diri.nama)

# p1 = Person("Noorwahid", 19)
# p1.myfunc()



# class Person:
#    def __init__(self, fname, lname):
#      self.namadepan = fname
#      self.namabelakang = lname

#    def printname(self):
#      print(self.namadepan, self.namabelakang)

# class Student(Person):
#    def __init__(self, fname, lname, tahun):
#        super().__init__(fname, lname)
#        self.graduationyear = tahun

#    def welcome(self):
#      print("Selamat datang", self.namadepan, self.namabelakang, " di kelas Teknik Informatika", self.graduationyear)


# x = Student("Noor", "Wahid", 2020)
# x.welcome()





# class MyNumbers:
#     def __iter__(self):
#         self.a = 0
#         return self

#     def __next__(self):
#         if self.a <= 40:
#             x = self.a
#             self.a += 4
#             return x
#         else:
#             raise StopIteration

# myclass = MyNumbers()
# myiter = iter(myclass)

# for x in myiter:
#     print(x)









# f = open("demoteks.txt", "r")
# print(f.read())
# f.close()





berat_badan = int(input('Berat badan: '))
unit = input('(L)bs atau (K)g:')
if unit.upper() == "L":
    dikonversikan = berat_badan * 0.45
    print(f"Berat Badan Kamu Adalah {dikonversikan} kios")
else:
    dikonversikan = berat_badan / 0.45
    print(f"Berat badan kamu adalah {dikonversikan} pounda.")


nomor_rahasia = 9
tebak_hitung = 0
tebak_batas = 3
while tebak_hitung < tebak_batas:
    tebak = int(input('Tebak angka:'))
    tebak_hitung += 1
    if tebak == nomor_rahasia:
        print('Kamu berhasil menebaknya!')
        break
else:
    print('Maaf. kamu gagal menebaknya.')

