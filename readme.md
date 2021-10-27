# <p align="center"> TUGAS PEMROGRAMAN - INPUT BIODATA
[![melvian](./images/melvian.png)](https://www.linkedin.com/in/melvian-wijaya-760b371b1/)
<p align="justify">Tugas Pemgrogaman membuat program input menggunakan bahasa pemrograman python.

---
<br>


# [latihan1.py](https://github.com/melviandanuw/TugasProgramBiodata/blob/main/latihan1.py)

<p align="justify">Berisi latihan menulis syntax dalam bahasa pemrograman python.

- Syntax menampilkan output pada Python.
```sh
print("string"); //print string.
print(iniVariabel); //print variabel.
print(100); //print integer.
```
- Variabel dalam Python.
```sh
variabelA = 'string'; //Variabel yang berisi string.
variabelB = 100; //Variabel yang berisi integer.
```
- Menampilkan output dengan menggunakan format() method.
```sh
//%d pada syntax berfungsi menampilkan decimal format

//format(a,b) berfungsi menampilkan a = value 
pertama & b = value kedua.

print("hasil penjumlahan {1}+{0}=%d".format(a, b) %(a+b)); 
```

---
<br>


# [tugas1.py](https://github.com/melviandanuw/TugasProgramBiodata/blob/main/tugas1.py)

<p align="justify">Berisi tugas membuat program biodata dalam bahasa pemrograman python.

- Variabel input dengan tipe data string.
```sh
//method input berfungsi untuk menyimpan inputan user.

nameLengkap = input("Masukan Nama Lengkap:\n")
```
- Variabel input dengan tipe data integer.
```sh
//int(input("")) berfungsi untuk menentukan tipe data yang dapat disimpan divariabel tersebut.

noTelp = int(input("Masukan Nomor Telepon:\n"));
```
- Menampilkan output dengan print.
```sh
print("""Assalamu\'alaikum.\n
Let me introduce my self. My name is""", nameLengkap + ', but you can call me', namaPanggilan + """. 
My NPM is""", str(npm) + '. I was born in', tempatLahir + ' and i am', str(umur) + """ years old. 
I am very glad if you want to invite to my house in""", alamat+ """. 
So, don\'t forget to call me before with the number""", str(noTelp) + """.
\nThank You.""");

// tanda \' berfungsi untuk print kutip satu (').
// \n berfungsi membuat baris baru
// str(notelp) casting dari variabel int ke str.
```