import PySimpleGUI as gui
from pynput import keyboard
#IMPORTING

gui.theme_previewer()

enable_gui = ''
wordle_word_arr = []
guess_arr = []

key = 0

layout = [[gui.Text('Do you want to enable the gui?', font= ('Arial', 16))],
[gui.Button('Yes', size=(6, 1), font=('Arial', 32)), gui.Button('No', size=(6, 1), font=('Arial', 32))]]

window = gui.Window(title="Graphics options", layout=layout, size=(348, 140), element_justification='c')

while True:
    event, values = window.read()
    if event == 'Yes':
        enable_gui = 'true'
        window.close()
        break
    elif event == 'No':
        enable_gui = 'false'
        window.close()
        break
    elif event == gui.WIN_CLOSED:
        window.close()
        break
# enable gui

guess_number = 1
guess_number = str(guess_number)
loop = 6

if enable_gui == 'false':
    print ('this is not the place for that')
elif enable_gui =='true':
    print ('this is a wip')

    while loop > 0:
        layout = [[gui.Text('Guess number ' + guess_number + ':')],
        [gui.Input(do_not_clear=False)],
        [gui.Button('Enter', size=(4, 1), font=('Arial', 12)), gui.Button('Exit', size=(4, 1), font=('Arial', 12))]]

        window = gui.Window(title="Wordle", layout=layout, size=(696, 280), element_justification='l')

        while True:
            event, values = window.read()
            if event == gui.WIN_CLOSED or event == 'Exit':
                window.close()
                loop = 0
                break
            elif event == 'Enter':
                if values[0] == '':
                    print ('Please put an answer')
                else:
                    guess = (values[0])
                    for letter in guess:
                        guess_arr.append(letter)
                    print (guess)
        loop -= 1
# defining guess

window.close()