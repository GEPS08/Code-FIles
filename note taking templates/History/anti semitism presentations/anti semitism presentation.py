import os
import time

presenter = input('Presenter:\n')
topic = input('Topic:\n')
learned = input('One thing I learned:\n')
question = input('One question:\n')
well = input('One thing done well:\n')
work = input('One thing to work on:\n')

print ('Presenter:' + presenter + '                 Topic:' + topic + '\n\nI learned:\n' + learned + '\nOne question:\n' + question +'\nDone well:\n' + well +'\nTo work on:\n' + work)

with open ('C:\\Users\\' + os.getlogin() + '\\.vscode\\code files\\note taking templates\\History\\anti semitism presentations\\presentations.txt', 'a') as file:
    file.write('Presenter: ' + presenter + '                 Topic: ' + topic + '\n\nI learned:\n' + learned + '\nOne question:\n' + question + '?\nDone well:\n' + well +'\nTo work on:\n' + work + '\n\n\n')
