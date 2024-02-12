import time,os
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#pip install webbrowser, selenium

i = int(input('Please put the amount of bots to make:\n'))
ii = 1
options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress","localhost:9222")
pin = input('Please put the meet code here:\n')
name = input('Please put the name of the bot:\n')

driver = webdriver.Chrome(executable_path="C:/chromedriver/chromedriver.exe", options=options)

link = ('https://meet.google.com/' + pin)

print (link)
while i >= 1:
    driver.get(link)
    ii = str(ii)
    while True:
        try:
            driver.find_element(by=By.XPATH, value="//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-dgl2Hf ksBjEc lKxP2d LQeN7 AjXHhf']").click()
        except:
            continue
        else:
            break
    while True:
        try:
            driver.find_element(by=By.XPATH, value="//button[@class='VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 jEvJdc QJgqC']").click()
        except:
            continue
        else:
            break
    driver.switch_to.new_window('tab')
    print (name, ii)
    i -= 1
    ii = int(ii)
    ii += 1

