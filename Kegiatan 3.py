a = input ("Masukkan Nama Saudara")
b = float(input ('pukul berapa sekarang :'))
if b<= 10.59:
    print('Selamat Pagi', a)
elif 15.00>=b>= 11.00:
    print('Selamat Siang', a)
elif 15.01<=b<= 17.00:
    print('Selamat Sore', a)
else :
    print('Selamat Malam', a)
