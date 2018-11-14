Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = 'Aria Widiyo Noviyanto'
>>> #3 menyimpan Aria Widiyo Noviyanto ke variabel Nama
>>> NIM = '0343'
>>> ## menyimpan 0343 ke variabel NIM
>>> Tinggi = 1.65
>>> ## menyimpan 1.65 ke variabel Tinggi
>>> Berat = 90
>>> ## menyimpan 90 ke variabek Berat
>>> TahunLahir = 1999
>>> ## menyimpan variabel 1999 ke Tahun Lahir
>>> Aku = (TahunLahir, Berat, Tinggi, NIM, Nama)
>>> ## menyimpan list ke variabel aku
>>> ## meksdunya menyimpan tuple ke variabel Aku
>>> Data = (TahunLahir, Berat, Tinggi, NIM,Nama)
>>> ## menyimpan list ke variabel Data
>>> type(Aku)
<class 'tuple'>
>>> ## ini menunjukkan jenis data variabel Aku
>>> Aku[0]
1999
>>> ## melakukan indexing pada variabel Aku yang berupa tuple pada deret ke 0
>>> a = NIM % 4; Aku[a]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a = NIM % 4; Aku[a]
TypeError: not all arguments converted during string formatting
>>> type(Aku[0])
<class 'int'>
>>> ## ini menunjukkan jenis data variabel Aku[0]
>>> Aku[a:4]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    Aku[a:4]
NameError: name 'a' is not defined
>>> Aku[0:4]
(1999, 90, 1.65, '0343')
>>> #3 melakukan slicing dari list variabel Aku
>>> type(Aku[0:4])
<class 'tuple'>
>>> ## ini menunjukkan jenis data dari variabel Aku[0:4]
>>> type(Data)
<class 'tuple'>
>>> ## ini menunjukkan jenis data variabel Data
>>> Data[4][5]
'W'
>>> ## melakukan indexing pada variabel data
>>> Data[4][0:6]
'Aria W'
>>> ## melakukan indexing dan slicing pada variabel data
>>> Data[0] =
SyntaxError: invalid syntax
>>> Data[0]
1999
>>> Data[-a]
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    Data[-a]
NameError: name 'a' is not defined
>>> Data[-0]
1999
>>> ## melakukan indexing pada variabel data
>>> range(a)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    range(a)
NameError: name 'a' is not defined
>>> 
