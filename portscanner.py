import socket
import threading
# import colorama

def scan(targets,ports):
    for port in range(1,ports):
        threading.Thread(target=scanport, args=(targets,port)).start()
 
def scanport(ip,port):
    try:
        sock = socket.socket()
        sock.connect((ip,port))
        print("port open " + str(port))
        sock.close()
    except:
        # print("port closed " + str(port))
        pass


targets = input("Enter ip of the machine (seperate by ',' for multiple machines): ")
ports = int(input("enter number of ports you want to scan: "))

scan(targets,ports)