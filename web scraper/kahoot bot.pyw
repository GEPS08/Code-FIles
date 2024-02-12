import time,os
import PySimpleGUI as gui
from selenium import webdriver
from selenium.webdriver.common.by import By
#pip install webbrowser, selenium

gui.theme('DarkBlue15')

layout = [
[gui.Text('Setup', font= ('Arial', 16))],
[gui.Text('Amount of bots:', size=(15, 1)), gui.InputText(default_text=('10'))],
[gui.Text('Name of bots:', size=(15, 1)), gui.InputText()],
[gui.Text('Kahoot game pin', size=(15, 1)), gui.InputText()],
[gui.Text('', size=(1, 1))],
[gui.Submit(size=(12, 1), font= ('Arial', 16)), gui.Cancel(size=(12, 1), font= ('Arial', 16))],
[gui.Text('', size=(1, 2))],
[gui.Text('Which option do you want to select?', font= ('Arial', 16))],
[gui.Button('1', size=(6, 1), font=('Arial', 32)), gui.Button('2', size=(6, 1), font=('Arial', 32))], 
[gui.Button('3', size=(6, 1), font=('Arial', 32)), gui.Button('4', size=(6, 1), font=('Arial', 32))]
]

window = gui.Window(title="Kahoot Bot", layout=layout, size=(512, 512), element_justification='c')
while True:
    event, values = window.read()
    print (values)
    print (event)
    if event == 'Cancel':
        window.close()
        break

    elif event == 'Submit':
        i = int(values[0])
        name = values[1]
        pin = values[2]
        break

    elif event == gui.WIN_CLOSED:
        window.close()
        import sys
        sys.exit("Error message")
        break

i1 = i
ii = 1
options = ''

window.refresh()

driver = webdriver.Chrome(executable_path="C:/chromedriver/chromedriver.exe", options=options, service_args=["--verbose", "--log-path=C:\\chromedriver\\logan\\logan.log"])

while i >= 1:
    driver.get('http://www.kahoot.it')
    driver.find_element(By.NAME, 'gameId').send_keys(pin, "\n")
    ii = str(ii)
    while True:
        try:
            driver.find_element(By.NAME, 'nickname').send_keys(name, ii, "\n")
        except:
            continue
        else:
            break
    driver.switch_to.new_window('tab')
    print (name, ii)
    i -= 1
    ii = int(ii)
    ii += 1

while True:
    i = i1
    ii = 0
    answer = ''

    window.refresh()
    event, values = window.read()
    if event == 'Submit':
        continue
    elif event == 'Cancel':
        window.close()
        driver.close()
        break
    elif event == gui.WIN_CLOSED:
        window.close()
        driver.close()
        break
    answer = event
    print (answer)

    print (answer)

    while i >= 1:
        driver.switch_to.window(driver.window_handles[ii])

        window.refresh()

        while True:
            try:
                driver.find_element(by=By.XPATH, value="//button[@aria-label='Answer {}']".format(answer)).click()
            except:
                continue
            else:
                break
        print ('tab:', ii)

        ii += 1
        i -= 1