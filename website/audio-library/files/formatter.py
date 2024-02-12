import os

i = 0
name = os.listdir(r'C:\\Users\\' + os.getlogin() + '\\.vscode\\code files\\website\\audio-library\\files')
print(name)
for file in name:
    name[i] = name[i].replace(' ', '')
    i += 1