import os

periods = 0

with open(r"C:\\Users\\Joe\\.vscode\\code files\\note taking templates\\religion journal thing.txt", "r") as file:
    textfile = file.read()

    periods = textfile.count('.')

    periods = str(periods)

print (periods)

