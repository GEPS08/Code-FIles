import time,os
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
#pip install webbrowser, selenium


i = int(input('Please put the amount of bots to make:\n'))
ii = 1
options = ''
name = input('Please put the name of the bot:\n')
pin = input('Please put the game pin here:\n')

driver = webdriver.Chrome(executable_path="C:/chromedriver/chromedriver.exe", chrome_options=options)

while i >= 1:
    driver.get('https://play.blooket.com/play')
    driver.find_element(By.CLASS_NAME, 'styles__idInput___1zWUq-camelCase').send_keys(pin, "\n")
    ii = str(ii)
    while True:
        try:
            driver.find_element(By.CLASS_NAME, 'styles__nameInput___20VdG-camelCase').send_keys(name, ii, "\n")
        except:
            continue
        else:
            break
    driver.switch_to.new_window('tab')
    print (name, ii)
    i -= 1
    ii = int(ii)
    ii += 1

