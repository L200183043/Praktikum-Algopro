import socket

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',50008))
s.listen(5)
print('TCP sudah siap')
masuk=''

while masuk !='q':
    komm, addr= s.accept()
    while masuk !='q':
        masuk= komm.recv(1024)
        if masuk == 'keluar':
            print('pesan:', masuk)
            komm.send('-')
            s.close()
        print('pesan:', masuk)
        komm.send('parameter dicatat')
        t=komm.recv(1024)
        if t=='hitung':
            masuk=int(masuk)
            h=4*3.14*masuk**2
            h=str(h)
            masuk=str(masuk)
            komm.send('luas permukaan bola berjari-jari' +masuk+ 'adalah' +h)
        else:
            komm.send('tidak ada')