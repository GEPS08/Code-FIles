import time,os
from selenium import webdriver
from selenium.webdriver.common.by import By
#pip install webbrowser, selenium

from pygame._sdl2 import get_num_audio_devices, get_audio_device_name #Get playback device names
from pygame import mixer #Playing sound
mixer.init() #Initialize the mixer, this will allow the next command to work
[get_audio_device_name(x, 0).decode() for x in range(get_num_audio_devices(0))] #Returns playback devices
#['Headphones (Oculus Virtual Audio Device)', 'MONITOR (2- NVIDIA High Definition Audio)', 'Speakers (High Definition Audio Device)', 'Speakers (NVIDIA RTX Voice)', 'CABLE Input (VB-Audio Virtual Cable)']
#mixer.quit() #Quit the mixer as it's initialized on your main playback device
#mixer.init(devicename='CABLE Input (VB-Audio Virtual Cable)') #Initialize it with the correct device
#mixer.music.load("Megalovania.mp3") #Load the mp3
#mixer.music.play() #Play it

options = ''
driver = webdriver.Chrome(executable_path="C:/chromedriver/chromedriver.exe", options=options)

driver.get('https://www.google.com')