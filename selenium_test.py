import json
import os

import requests
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException

DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')

chromeOptions = webdriver.ChromeOptions()
chromeOptions._binary_location = '/usr/bin/google-chrome-stable'
chromeOptions.add_argument('--headless')
chromeOptions.add_argument('--disable-gpu')
chromeOptions.add_argument('--remote-debugging-port=9222')
prefs = {"download.default_directory": os.path.dirname(__file__) + '/data'}
chromeOptions.add_experimental_option("prefs", prefs)

driver = webdriver.Chrome(executable_path="./chromedriver", chrome_options=chromeOptions)


GOOGLE = 'https://www.google.com'
driver.get(GOOGLE)
img_url = GOOGLE + driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/img').get_attribute('src')

r = requests.post(DISCORD_WEBHOOK_URL, data=json.dumps({'content': 'test', 'embeds': [{'image': {'url': img_url}}]}), headers={'content-type': 'application/json'})
