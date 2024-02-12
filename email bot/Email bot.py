from pathlib import Path
import PySimpleGUI as gui
from pynput import keyboard
import imapclient
import imaplib
import pyzmail
import smtplib
import email
import os
import time
import random
#IMPORTING

imaplib._MAXLINE = 1000000

i = imapclient.IMAPClient('imap-mail.outlook.com')
i.login('a9087362987134b@outlook.com', 'iamabot1234')

folder_list = []

for item in i.list_folders():
    print(item[2])
    folder_list.append(item[2])
    

print (folder_list)
print (i.list_folders())

layout = [[gui.Push(),gui.Text('Which folder would you like to open', font= ('Arial', 16)),gui.Push()],
[gui.Push(),gui.OptionMenu(values=folder_list,size=(1,1)),gui.Push()],
[gui.VPush(),gui.Push(),gui.Button('Ok', size=(3, 1), font=('Arial', 12)),gui.Button('Cancel', size=(6, 1), font=('Arial', 12))]]

window = gui.Window(title="Graphics options", layout=layout, size=(1024, 512))

while True:
    event, values = window.read()
    print (event)
    print (values[0])
    email_folder = values[0]
    if event == 'Ok':
        enable_gui = 'true'
        window.close()
        break
    elif event == 'Cancel':
        enable_gui = 'false'
        window.close()
        break
    elif event == gui.WIN_CLOSED:
        window.close()
        break
#setting up the window

i.select_folder('Inbox')
i.search(['ALL'])
print(i.search(['ALL']))
#thing to get the emails

s = smtplib.SMTP('smtp-mail.outlook.com', 587)
s.starttls()
s.ehlo()
s.login('a9087362987134b@outlook.com', 'iamabot1234')
#thing to send the emails

for item in i.search(['ALL']):
#repeats each email
    print (item)
    rawmsgs = i.fetch(item, [b'BODY[]'])

    msg = pyzmail.PyzMessage.factory(rawmsgs[item][b'BODY[]'])

    with  open(r"C:\Users\Joe\.vscode\code files\email bot\Raw logs\Raw logs.txt", "a") as file:
        msg = str(msg)
        file.write(msg)
        file.close()

    msg = pyzmail.PyzMessage.factory(rawmsgs[item][b'BODY[]'])

    print (msg)

    print (msg.get_subject())
    print (msg.get_addresses('from'))
    print (msg.get_addresses('to'))
    print (msg.get_addresses('cc'))

    fromEmail = (msg.get_addresses('from'))
    toEmail = (msg.get_addresses('to'))
    ccEmail = (msg.get_addresses('cc'))

    print (fromEmail)

    for item in fromEmail:
        print(item[1])
        fromEmailAdress = item[1]
        fromEmailName = item[0]

    print (toEmail)

    for item in toEmail:
        print(item[1])
        toEmailAdress = item[1]
        toEmailName = item[0]

    print (ccEmail)


    for item in ccEmail:
        print(item[1])
        ccEmail = item[1]


    msg.html_part != None
    print ('This is the email in html:\n\n', msg.html_part.get_payload().decode(msg.html_part.charset), '\n\n')

    with  open(r"C:\Users\Joe\.vscode\code files\email bot\vars\log count.txt", "r+") as file:
        var_old = file.read()
        var_old = int(var_old)
        var = var_old + 1
        var = str(var)
        file.write(var)
        file.close()

    with  open(r"C:\Users\Joe\.vscode\code files\email bot\vars\log count.txt", "w") as file:
        file.write(var)
        file.close()

    with  open(r"C:\Users\Joe\.vscode\code files\email bot\html logs\emailhtml" + var + ".txt", "a") as file:
        file.write(msg.html_part.get_payload().decode(msg.html_part.charset))
        file.close()

    htmlfile = Path(r'C:\Users\Joe\.vscode\code files\email bot\html logs\emailhtml' + var + '.txt')
    htmlfile.rename(htmlfile.with_suffix('.html'))

    msg.text_part != None
    print ('This is the email in text:\n\n', msg.text_part.get_payload().decode(msg.text_part.charset), '\n\n')

    print ('The message:\n\n' + msg.text_part.get_payload().decode(msg.text_part.charset) + '\n\nWas sent to you by ' + fromEmailName + ' at ' + fromEmailAdress + '\n\n')

    man_auto = input('Would you like to manually or automaticly reply to this message (put auto for an automatic reply or man to manually reply)\n')

    if man_auto == 'man':
        msgSendText = input('What message would you like to send back?\n')
        msgSend = email.message.EmailMessage()
        msgSend['from'] = toEmailAdress
        msgSend["to"] = fromEmailAdress
        msgSend["Subject"] = ('Re: ' + (msg.get_subject()))
        msgSend.set_content(msgSendText)
        res = s.send_message(msgSend)

    elif man_auto == 'no' or man_auto == 'NO' or man_auto == 'No':
        continue

    elif man_auto == 'auto':
        att_pass = input('Would you like to attack or passively reply to this message (put att for an automatic attack or pass for an automatic passive reply)\n')

        if att_pass == 'pass':
            msgSendText = ('Hello ' + fromEmailName + ', \nThis is an automated reply because of me not being able to make a proper reply or me not caring about you.\nYour email that you sent to me, will still be recorded and might be properly answered in a few hours or days, so do not be concerned if this is an important situation\nThank you for your understanding,\n' + toEmailName)
            msgSend = email.message.EmailMessage()
            msgSend['from'] = toEmailAdress
            msgSend["to"] = fromEmailAdress
            msgSend["Subject"] = ('Re: ' + (msg.get_subject()))
            msgSend.set_content(msgSendText)
            res = s.send_message(msgSend)

        elif att_pass == 'att':
            
            attWarning = input('Are you sure you would like to procede with this?\nYou may get in trouble with your email provider\nY/N\n')

            if attWarning == 'y' or attWarning == 'Y':
                attLoop = int(input('Please put the amout of emails to send to the emaill under attack\n'))
                attSub = 'Re:' + (msg.get_subject())

                while attLoop > 0:
                    msgSendText = ('Hello ' + fromEmailName + ', \nYou and your email are now under attack due to the receiver of your original email, ' + toEmailName + ' at ' + toEmailAdress + ', classifying the email as a threat to them in any way, shape, or form' + '\n\nIf you would like to purchase protection from this current attack or another attach using this method, contact:\na9087362987134a@outlook.com\nDo not try do use automated warefare against this account because they are prepared for that and it will ultimately lead to nothing.' + '\nThank you for your understanding,\n' + toEmailName)
                    msgSend = email.message.EmailMessage()
                    msgSend['from'] = toEmailAdress
                    msgSend["to"] = fromEmailAdress
                    msgSend["Subject"] = (attSub)
                    msgSend.set_content(msgSendText)
                    res = s.send_message(msgSend)

                    attLoop = int(attLoop)
                    random_num = random.randint(60, 300)

                    time.sleep (random_num)

                    attLoop -= 1
                    attSub = ('Attack' + ' #' + str(attLoop))
            elif attWarning == 'n' or attWarning == 'N' :
                print('\nYou may have made the right decision\n\nIf you would like to still annoy the person in which you originally intended to, \nconsider using our discord spam bot, by contacting us at\n9087362987134a@gmail.com')

window.close()