import platform
import time
import os

# provides the main interface for controlling web browsers
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
# used to manage the lifecycle of browser driver executable, useful
# when configuring and starting the ChromeDriver service
from selenium.webdriver.chrome.service import Service
# Provides predefined methods to locate elements on a webpage
from selenium.webdriver.common.by import By
# Has a set of common conditions that are used when automation browser interactions
from selenium.webdriver.support import expected_conditions as EC
# Used to wait for certain conditions to be met bf proceeding
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.keys import Keys


# File path of chromedriver
chromedriver_path = r"C:\Users\muket\Desktop\Chrome Drivers\chromedriver.exe"

driver_option = webdriver.ChromeOptions()
driver_option.add_argument('--incognito')

print(platform.uname())
current_d = os.getcwd().split("\\")
current_user_d = current_d[2]


def create_new_file():
    folder_name = 'New Drivers'
    folder_path = fr'C:/Users/{current_user_d}/Desktop'
    full_path = os.path.join(folder_path, folder_name)
    os.makedirs(full_path, exist_ok=True)


# def download_to_path():


# C:\Users\muket\Desktop\chrome drivers

def extract_links(chromedrivers):
    links = [item for item in chromedrivers if item.startswith('http')]
    return links


def create_wd():
    service = Service(chromedriver_path)
    return webdriver.Chrome(service=service, options=driver_option)


def downloadChromeDriver():
    browser = create_wd()
    browser.get('https://googlechromelabs.github.io/chrome-for-testing/#stable')
    WebDriverWait(browser, 3).until(
        EC.presence_of_all_elements_located((By.XPATH, '//*[@id="stable"]'))
    )
    chrome_link = browser.find_element(By.XPATH, '//*[@id="stable"]').text
    chromedrivers = chrome_link.split()
    working_drivers = (extract_links(chromedrivers))
    print(working_drivers)
    print(platform.uname().system)

    '''if platform.uname().system == 'Windows':
        try:
            browser_search.send_keys(working_drivers[9])
            time.sleep(2)
            browser_search.send_keys(Keys.RETURN)
        except NoSuchElementException:
            print('No such element')'''

    browser.quit()


downloadChromeDriver()
create_new_file()
