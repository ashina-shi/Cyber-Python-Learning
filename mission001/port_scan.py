import socket

ip = '192.168.56.101'
port = 80

message = """GET /dvwa/index.php HTTP/1.1
Host: 192.168.56.101

""" 

data = message.encode()
print(message)


client = socket.socket()
client.connect((ip, 80))
client.send(data)
a = client.recv(1024)


print(a.decode())
client.close()
