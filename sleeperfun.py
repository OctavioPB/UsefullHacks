#! python3
# - Launch a webpage every hour to do scrapping
import datetime
import time
from selenium.webdriver import Firefox
from selenium.webdriver.common import keys as kk
launchtime = datetime.datetime.now()

while True:
    while datetime.datetime.now() < launchtime:
         print('Waiting...')
         time.sleep(1)
    else:
        driver = Firefox()
        driver.get('https://www.google.com/')
        googlebar = driver.find_element_by_css_selector('input.gLFyf.gsfi')
        googlebar.send_keys('Tax lawyer high net worth individual')
        googlebar.send_keys(kk.Keys.ENTER)
        print('Searching...')
        #googlebtn = driver.find_element_by_css_selector('input.gNO89b')
        #googlebtn.click()
        time.sleep(5)
        print('Task Completed')
        driver.close()
        launchtime = launchtime + datetime.timedelta(minutes=4)
