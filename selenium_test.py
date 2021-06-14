import os

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException

chromeOptions = webdriver.ChromeOptions()
chromeOptions._binary_location = '/usr/bin/google-chrome-stable'
chromeOptions.add_argument('--headless')
chromeOptions.add_argument('--disable-gpu')
chromeOptions.add_argument('--remote-debugging-port=9222')
prefs = {"download.default_directory": os.path.dirname(__file__) + '/data'}
chromeOptions.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(executable_path="./chromedriver", chrome_options=chromeOptions)

driver.get('https://google.com')

print(driver.page_source)
