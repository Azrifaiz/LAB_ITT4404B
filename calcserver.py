import socket
import sys
import time
import errno
import math        #Math Module
from multiprocessing import Process

ok_message = '\nHTTP/1.0 200 OK\n\n'
nok_message = '\nHTTP/1.0 404 NotFound\n\n'

def process_start(s_sock):
    s_sock.send(str.encode("== Calculator Using Python =="))
    while True:
        data = s_sock.recv(2048)
        data = data.decode("utf-8")

        try:
            operation,number1= data.split(" ")
            op = str(operation)
            n1 = int(number1)

            if op[0] == 'l':
                answer = math.log(n1)
            elif op[0] == 's':
                answer = math.sqrt(n1)
            elif op[0] == 'e':
                answer = math.exp(n1)
            elif op[0] == 'f':
                answer = math.factorial(n1)
            else:
                answer = ('Wrong input')

            sendAnswer = ('Answer = '+str(answer))
            print ('Calculation Completed')
        except:
            print ('Wrong input')
            sendAnswer = ('Wrong input')

        if not data:
            break

        s_sock.send(str.encode(sendAnswer))
    s_sock.close()

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8080))
    print("Listening...")
    s.listen(28)

    try:
        while True:
            try:
                s_sock, s_addr= s.accept()
                p = Process(target=process_start, args=(s_sock,))
                p.start()
else:
                answer = ('Wrong input')

            sendAnswer = ('Answer = '+str(answer))
            print ('Calculation Completed')
        except:
            print ('Wrong input')
            sendAnswer = ('Wrong input')

        if not data:
            break

        s_sock.send(str.encode(sendAnswer))
    s_sock.close()

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8080))
    print("Listening...")
    s.listen(28)

    try:
        while True:
            try:
                s_sock, s_addr= s.accept()
                p = Process(target=process_start, args=(s_sock,))
                p.start()

            except socket.error:

                print('got a socket error')

            except Exception as e:
                print("an exception occurred!")
                print(e)
                sys.exit(1)
    finally:
           s.close()

