# def greeting(name):
#   print("Hello, " + name)


# orang1 = {
#     "name": "NoorWahid",
#     "age": 19,
#     "country": "Indonesia"
#     }
# import camelcase

# c = camelcase.CamelCase()

# txt = "mau ngapain kamu kok gitu"

# print(c.hump(tct))

import numpy as np


arr = np.array([1,2,3,4,5,6,7,8,9])

print(arr)
print(type(arr))

array = np.array((1,2,3,4,5,6))

print(array)

#Array yang memiliki larik 2-D (matriks) sebagai elemennya disebut larik 3-D.

#Ini sering digunakan untuk mewakili tensor orde-3 ke-3.

arra = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arra)


#Periksa berapa banyak dimensi yang dimiliki array:

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

Untuk mengakses elemen dari array 3-D kita dapat menggunakan integer yang dipisahkan koma yang mewakili dimensi dan indeks elemen.

arr1 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr1[0, 1, 2])
