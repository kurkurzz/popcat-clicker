import os
import sys
import time
import math
import platform

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

# Select chromedriver based on os
# Chromedriver version is 92.*
os_use = platform.system()
if os_use == 'Darwin':
    driver_path = 'drivers/chromedriver_macos'
elif os_use == "Windows":
    driver_path = 'drivers/chromedriver.exe'
elif os_use == "Linux":
	driver_path = 'drivers/chromedriver_linux'

try:
	op = webdriver.ChromeOptions()
	driver = webdriver.Chrome(executable_path=resource_path(driver_path),options=op)

	driver.get('https://popcat.click')
	element = driver.find_element_by_xpath('//*[@id="app"]/img')
	# limit 800 pop per 30 seconds
	while True:
		start  = time.time()
		counter = 0
		while True:
			element.click()
			counter+=1
			if counter >= 799:
				end = time.time()
				diff = end - start
				time.sleep(30-math.ceil(diff))
				break
finally:
	exit()
