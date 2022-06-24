import socket

s = socket.socket()
print("Berjaya buat sokett")

port = 8888
localIP = "127.0.1.1"

msgFromServer = "hello UDP client"
bytesToSend = str.encode(msgFromServer)

UDPServerSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_DGRAM)

UDPServerSocket.bind((localIP, port))

s.bind(('', port))
print("Berjaya bind soket di port: " + str(port))

s.listen(5)
print("soket tengah menunggu client!")

while True:
        c, addr = s.accept()
        print("Dapat capaian dari: " + str(addr))

        c.send(b"Terima Kasih!")
        buffer = c.recv(1024)
        print(buffer)
c.close()

