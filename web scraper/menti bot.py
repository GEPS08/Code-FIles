import time,os
import webbrowser
from pynput.keyboard import Key, Controller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
keyboard = Controller()
#pip install webbrowser, selenium

amount = int(input('Please put the amount of bots to make:\n'))
options = ''
option = int(input('Please put the option you want to select:\n'))
pin = input('Please put the game pin here:\n')
i = amount

driver = webdriver.Chrome(executable_path="C:/chromedriver/chromedriver.exe", options=options)

driver.get('http://www.menti.com')
driver.fullscreen_window()

while i >= 1:
    driver.get('http://www.menti.com')
    driver.find_element(By.NAME, 'id').send_keys(pin, "\n")
    time.sleep(0.1)   
    if i == amount:
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
    time.sleep(0.2)
    if option == 2:
        keyboard.press(Key.down)
        keyboard.release(Key.down)
    if option == 3:
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        keyboard.press(Key.down)        
        keyboard.release(Key.down)
    while True:
        try:
            #driver.find_element(by=By.CSS_SELECTOR, value="[aria-label='Option 1']")
            #driver.find_element(by=By.XPATH, value="//input[@id='mcq-2']").submit()
            #driver.find_element(by=By.LINK_TEXT, value='Option 2').click()
            driver.find_element(by=By.ID, value='mcq-2').submit()
            #driver.find_element(by=By.XPATH, value="//form[@class='m-el m-a m-f m-g m-h m-i m-j m-k r-form']").send_keys(Keys.DOWN)
        except:
            continue
        else:
            break
    print ('Complete')
    i -= 1