print "Kegiatan 2"
a = raw_input ("masukkan passwaord:")
for i in range (3):
    if i == 2:
        print "Anda telah mencoba 3 kali. Akses anda ditolak. "
    elif a == "Aria":
        print "Anda berhasil login"
        break
    elif a!= "Aria":
        print "Maaf, anda salah memasukkan password. "
        a = raw_input ("Massukkan password")
