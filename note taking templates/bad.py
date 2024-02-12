import random
import PySimpleGUI as gui
import pyperclip
vert = 0
ttc = ''

gui.theme('LightBrown6')

layout = [
    [gui.Text('Text To Copy', font= ('Arial', 16))],
    [gui.Text(ttc, font= ('Arial', 11))],
    [gui.Button('Generate', size=(7, 1), font=('Arial', 24))]
]

def infinite():
    curly1 = []
    for i in range(8):
        vert = round(random.uniform(0.5, 14.5), 2)
        if i%2==1:
            curly = (rf'{vert}\le y\le{vert+0.5}\left\ '+'{'+fr'-{random.uniform(0, 15)}\le x\le15\right\ '+'}')
        else:
            curly = (rf'-{vert}\le y\le{-vert+0.5}\left\ '+'{'+fr'-15\le x\le{random.uniform(0, 15)}\right\ '+'}')
        curly = curly.replace('\ ', '\\')
        curly1.append(curly)

    for i in range(8):
        vert = round(random.uniform(0.5, 14.5), 2)
        if i%2==1:
            curly = (rf'{vert}\le x\le{vert+0.5}\left\ '+'{'+fr'-{random.uniform(0, 15)}\le y\le15\right\ '+'}')
        else:
            curly = (rf'-{vert}\le x\le{-vert+0.5}\left\ '+'{'+fr'-15\le y\le{random.uniform(0, 15)}\right\ '+'}')
        curly = curly.replace('\ ', '\\')
        curly1.append(curly)

    diag = round(random.uniform(0, 1), 2)
    variance = round(random.uniform(-13, 13), 2)

    for i in range(6):
        diag = round(random.uniform(0, 1), 2)
        variance = round(random.uniform(-13, 13), 2)
        if i%2==1:
            curly = (rf'\max\left(x-{diag}y-{variance},{diag}y-x-0.5+{variance}\right)\le0\left\ '+'{'+fr'-15\le y\le{random.uniform(0, 15)}\right\ '+r'}\left\{-15<x<15\right\}')
        else:
            curly = (rf'\max\left(x-{diag}y-{variance},{diag}y-x-0.5+{variance}\right)\le0\left\ '+'{'+fr'-{random.uniform(0, 15)}\le y\le15\right\ '+r'}\left\{-15<x<15\right\}')
        curly = curly.replace('\ ', '\\')
        curly1.append(curly)
    curly1 = '\n'.join(curly1)
    return curly1

window = gui.Window(title="Desmos Art Generator", layout=layout, size=(512, 512), element_justification='c')
while True:    
    event, values = window.read()
    print (values)
    print (event)

    if event == 'Generate':
        ttc = infinite()
        pyperclip.copy(ttc)
        print(ttc)

    elif event == gui.WIN_CLOSED:
        window.close()
        break

    layout = [
    [gui.Text('Text To Copy', font= ('Arial', 16))],
    [gui.Text(ttc, font= ('Arial', 11))],
    [gui.Button('Generate', size=(7, 1), font=('Arial', 24))]
    ]
    window.close()
    window = gui.Window(title="Desmos Art Generator", layout=layout, size=(512, 512), element_justification='c')