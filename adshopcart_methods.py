import datetime
from time import sleep
from selenium import webdriver #import selenium to the file
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import adshopcart_locators as locators
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select # -----add this import for drop down list
from selenium.webdriver import Keys


s = Service(executable_path='C:\Automation\Python\python_cctb\chromedriver.exe')
driver = webdriver.Chrome(service=s)



def setUp():
    print(f'Launch {locators.app} App')
    print(f'Test Started at: ¨{datetime.datetime.now()}')
    print(f'--------------------***-----------------------')
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(locators.advshoppingcart_homepage_url)

    if driver.current_url == locators.advshoppingcart_homepage_url and locators.advshoppingcart_home_page_title in driver.title:
        print(f'Yey! {locators.app} App website launched successfully!!!')
        print(f'{locators.app} Homepage URL: {driver.current_url}, Homepage title: {driver.title}')
        print(driver.title)
        sleep(1)
    else:
        print(f'{locators.app} did not launch. Check your code or application!')
        print(f'Current URL: {driver.current_url}, Page title: {driver.title}')


def tearDown():
    if driver is not None:
        print(f'--------------------***-----------------------')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()


setUp()
tearDown()