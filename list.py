angka_angka = [2, 3, 5, 5, 4, 2, 6, 5, 7, 8, 3]
angka_unik = []
for angka in angka_angka:
    if angka not in angka_unik:
        angka_unik.append(angka)
print(angka_unik)


#unpacking
#list
koordinat = [1, 2, 3]
x, y, z = koordinat
print(z)
#tupple
koordinat = (4, 5, 6)
a, b, c = koordinat
print(a)


#dictionaries
ponsel = input("Masukan nomor ponsel: ")
digits_mapping = {
    "1": "satu",
    "2": "dua",
    "3": "tiga",
    "4": "empat",
    "5": "lima",
    "6": "enam",
    "7": "tujuh",
    "8": "delapan",
    "9": "sembilan",
    "0": "nol"
    }
output = ""
for ch in ponsel:
    output += digits_mapping.get(ch, "!") + " "
print(output)
