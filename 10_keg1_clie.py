import socket

hostname = 'localhost'
pesan = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50003))
print "Program komunikasi tentang data diri"
while pesan.lower() != 'q':
    pesan = raw_input('perintah: ')
    s.send(pesan)
    if pesan.lower() == 'keluar':
        print('siap!!')
        s.close()
        break
    elif pesan.lower() !='q':
        response = s.recv(1024)
        print 'jawab: ', response
s.close()