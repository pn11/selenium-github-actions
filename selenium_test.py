from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory": os.path.dirname(__file__) + '/data'}
chromeOptions.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chromeOptions)

driver.get('https://google.com')

print(driver.page_source)
