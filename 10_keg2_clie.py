import socket

hostname='localhost'
perintah=''
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50003))
print('program komunikasi tentang server')
while perintah.lower() != 'quit':
    perintah=raw_input('command:')
    s.send(perintah)
    if perintah.lower() !='quit':
        response=s.recv(1024)
        print('response:',response)
    if perintah.lower() == 'quit':
        break
s.close()