import json
import os
import time

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


JACK = 'https://twitter.com/jack/photo'
driver.get(JACK)
time.sleep(10)
img_url = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[1]/div/div/div/div/div/img').get_attribute('src')

r = requests.post(DISCORD_WEBHOOK_URL, data=json.dumps({'content': 'test', 'embeds': [{'image': {'url': img_url}}]}), headers={'content-type': 'application/json'})
