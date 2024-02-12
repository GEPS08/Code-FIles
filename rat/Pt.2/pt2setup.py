

writer = []
with open(r"C:\Users\Joe\.vscode\code files\rat\Pt.2\setup.txt", 'r') as setup:
    setup = setup.read()
    writer = setup.split()
    print(setup)


writer[0] = input('Host Ip:\n')

for i in writer:
    print('asdf')

print (writer)