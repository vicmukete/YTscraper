import io
import platform
import time
import os
import requests
import zipfile
# import pyuac

# provides the main interface for controlling web browsers
from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
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

system_info = platform.uname()
current_d = os.getcwd().split("\\")
current_user_d = current_d[2]

# path where the file should be downloaded
download_path = fr"C:\Users\{current_user_d}\Documents\New Drivers"

# File path of chromedriver
chromedriver_path = r"C:\Users\muket\Desktop\Chrome Drivers\chromedriver.exe"

driver_option = webdriver.ChromeOptions()
driver_option.add_argument('--headless')


def extract_links(chromedriver):
    links = [item for item in chromedriver if item.startswith('http')]
    return links


def create_wd():
    service = Service(chromedriver_path)
    return webdriver.Chrome(service=service, options=driver_option)


def extract_end_from_link(link):
    last_element = link.split('/')
    print(last_element[-1])
    return last_element[-1]


def create_new_folder(url, filename):
    print('File saved to this path: ' + download_path + "\n")
    # Create the new folder if it doesn't already exist
    os.makedirs(download_path, exist_ok=True)
    full_zip_path = os.path.join(download_path, filename)
    response = requests.get(url)
    if response.status_code == 200:
        print(f'File save successfully to {download_path}')
        # the following allows the content to be downloaded in chunks
        with open(full_zip_path, 'wb') as zip_file:
            for chunk in response.iter_content(chunk_size=1892):
                zip_file.write(chunk)
        # extract the zip file
        with zipfile.ZipFile(io.BytesIO(response.content), 'r') as zip_file:
            zip_file.extractall()
    else:
        print(f'Failed to download file. Status Code: {response.status_code}')


def system_dependencies(system, link):
    if platform.uname().system == system:
        new_filename1 = extract_end_from_link(link)
        create_new_folder(link, new_filename1)
        time.sleep(2)


# split a particular element in working driver by the /
# and take the last element of the split. (chromedriver-win64.zip)

browser = create_wd()
browser.get('https://googlechromelabs.github.io/chrome-for-testing/#stable')
WebDriverWait(browser, 3).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="stable"]'))
)
chrome_link = browser.find_element(By.XPATH, '//*[@id="stable"]').text
chromedrivers = chrome_link.split()
working_drivers = (extract_links(chromedrivers))
print(f"List of Drivers: {working_drivers}\n")
print(f"Machine System: {platform.uname().system}")
print(f"Machine Name: {platform.uname().node}\n")

'''if platform.uname().system == 'Windows':
    new_filename = extract_end_from_link(working_drivers[9])
    create_new_folder(working_drivers[9], new_filename)
    time.sleep(2)'''

browser.quit()
