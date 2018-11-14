Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Nama = 'Aria Widiyo Noviyanto'
>>> ## menyimpan Aria Widiyo Noviyanto ke variabel nama
>>> NIM = 'L200183043'
>>> ## menyimpan L200183043 ke variabel nim
>>> x = '1'+NIM[7:]
>>> ## menyimpan slicing dan string ke variabel x
>>> a = int(x)
>>> ## merubah string menjadi bilangan bulat
>>> b = len(Nama)
>>> ## menghitung isi dari variabel nama
>>> type(a)
<class 'int'>
>>> ## menampilkan jenis data atau class dari variabel a
>>> type(b)
<class 'int'>
>>> ## menampilkan jenis data atau class dari variabel b
>>> a / b
49.666666666666664
>>> ## merupakan meknisme perhitungan aritmatika a dibagi b yang  menghasilkan 49.666666666666664
>>> a // b
49
>>> ## merupakan mekanisme perhitungan aritmatika dari a diabgi b yang yang hasil baginya dibulatkan menghasilkan angka 49
>>> 10 * (a - 999)
440
>>> ## merupakan mekanisme perhitungan aritmatika yaitu perkalian dan pengurangaan yang menghasilkan angka 440
>>> b ** 2
441
>>> ## merupakan mekanisme perhitungnga aritmatika perpangkatan dari variabel b yang berisi angka yang kemudian dipangkatkan 2
>>> a % b
14
>>> #3 merupakan menaknisme perhitungan aritmatika sisa hasil bagi
>>> #3 merupakan menaknisme perhitungan aritmatika sisa hasil bagi
>>> c = 12.5
>>> ## menyimpan angka 12.5 di variabel c
>>> type(c)
<class 'float'>
>>> ## menampilkan jenis data atau class dari variabel c
>>> a / c
83.44
>>> merupakan mekanisme perhitungan aritmatika yaitu pembagian
SyntaxError: invalid syntax
>>> a // c
83.0
>>> ## merupakan mekanisme perhitungan aritmatika dari a dibagi c yang hasil baginya dibulatkan menghasilkan angka 83
>>> c > b
False
>>> ## merupakan mekanisme dari operator perbandingna yang menghasilkan type data bolean bool yang bernilai false
>>> type(c > b)
<class 'bool'>
>>> ## merupakan mekanisme dari operator perbaandingnga yang menghasilkan type data bool
>>> a > b and b > c
True
>>> ## merupakan mekanisme ooperator perbandingan dari operator logika menghasilkan bolean atau bool beru[a true
>>> a > 1100 or b < 10
False
>>> 
