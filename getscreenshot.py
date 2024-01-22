from datetime import datetime
import pyaudio
import wave
import audioop
import math
import json
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pyvirtualdisplay import Display
#import tweepy
import os
import sys

print("ARGUMENT : " + sys.argv[1])
print("\n")

display = Display(visible=0, size=(800, 800))
display.start()
options = Options()
# browser is Chromium instead of Chrome

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

#options.BinaryLocation = "/usr/bin/chromium-browser"
#driver_path = "/usr/bin/chromedriver"
#driver = webdriver.Chrome(options=options, service=Service(driver_path))
#driver = webdriver.Chrome(ChromeDriverManager().install())

#driver.get('https://globe.adsbexchange.com/?icao='+icaocode+'&lat=37.719308818039025&lon=-121.84063212768908&hideSidebar&hideButtons&zoom=12')

print("Start screenshot GET time", str(datetime.now()), flush=True)
driver.get('https://globe.adsbexchange.com?lat=37.719308818039025&lon=-121.84063212768908&hideSidebar&hideButtons&zoom=12')
print("End screenshot END time", str(datetime.now()), flush=True)
print("Start screenshot SAVE TO FILE time", str(datetime.now()), flush=True)
driver.get_screenshot_as_file("./screenshot3_"+sys.argv[1]+"1.png")
print("End screenshot SAVE TO FILE time", str(datetime.now()), flush=True)



driver.quit()
print("end...", flush=True)



