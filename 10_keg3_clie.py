import socket

hostname='localhost'
keluar=''

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname,50008))
print('menghitung luas permukaan bola')
for i in range(0,3):
    keluar=raw_input('pesan:')
    s.send(keluar)
    r=s.recv(1024)
    r=str(r)
    print('respon:' ,r)
    if keluar=='keluar':
        s.close()
s.close()