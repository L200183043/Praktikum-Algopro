import socket
import platform

machine=platform.machine()
release=platform.release()
system=platform.system()
version=platform.version()
node=platform.node()
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 50003))
s.listen(5)
print('TCP sudah siap')
data=''

kamus={'machine':machine,'release':release,'system':system,'version':version,'node':node}

while data.lower() !='quit':
    komm, addr=s.accept()
    while data.lower() !='quit':
        data=komm.recv(2024)
        print('command:', data)
        if kamus.has_key(data):
            komm.send(kamus[data])
        elif kamus.has_key(data) == 'quit':
            s.close()
            break
        else:
            komm.send('unknown command')
s.close()