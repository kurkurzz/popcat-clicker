import platform

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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
	driver = webdriver.Chrome(executable_path=driver_path,options=op)

	driver.get('https://popcat.click')
	element = driver.find_element_by_xpath('//*[@id="app"]/img')
	while True:
		element.click()
finally:
	driver.quit()
