import socket

ip = '192.168.56.101'
port = 80

message = """POST /dvwa/login.php HTTP/1.1
Host: 192.168.56.101
Content-Length: 44
Cache-Control: max-age=0
Accept-Language: en-US,en;q=0.9
Origin: http://192.168.56.101
Content-Type: application/x-www-form-urlencoded
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like >
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,ima>
Referer: http://192.168.56.101/dvwa/login.php
Accept-Encoding: gzip, deflate, br
Cookie: security=high; PHPSESSID=daeaa988eea2e043b877bda052d0edce
Connection: keep-alive

username=admin&password=password&Login=Login
"""

data = message.encode()
print(message)


client = socket.socket()
client.connect((ip, 80))
client.send(data)
a = client.recv(1024)


print(a.decode())
client.close()
#一旦HTTPはこれで終わり
