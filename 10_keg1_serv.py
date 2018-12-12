import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50003))
s.listen(5)
print "Server penjawab otomatis sudah siap"
data = ''
kamus = {'nama':'aria widiyo noviyanto',
    'NIM':'L200183043',
    'angkatan':'2018',
    }
while data.lower() != 'q':
    komm, addr = s.accept()
    while data.lower() != 'q':
        data = komm.recv(1024)
        if data.lower() == 'q':
            print('siap!!')
            s.close()
            break
        print 'Perintah:', data
        if kamus.has_key(data):
            komm.send(kamus[data])
        else:
            komm.send('maaf, perintah tidak dimengerti')