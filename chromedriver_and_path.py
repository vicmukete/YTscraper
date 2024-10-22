import platform
import time
import os
import requests
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
download_path = fr"C:\Users\{current_user_d}\Documents\New Drivers".replace('\\', '/')

# File path of chromedriver
chromedriver_path = r"C:\Users\muket\Desktop\Chrome Drivers\chromedriver.exe"

driver_option = webdriver.ChromeOptions()
driver_option.add_argument('--incognito')


def create_new_folder(url):
    """
    folder_name = 'New Drivers'
    folder_path = fr'C:/Users/{current_user_d}/Documents'
    full_path = os.path.join(folder_path, folder_name).replace('\\', '/')
    """

    print(download_path + "\n")
    # Create the new folder if it doesn't already exist
    os.makedirs(download_path, exist_ok=True)
    response = requests.get(url)
    try:
        if os.path.exists(download_path):
            os.chmod(download_path, 0o666)
            print("File permission modified successfully")
            if response.status_code == 200:
                with open(download_path, mode='wb') as file:
                    file.write(response.content)
                print(f'file saved successfully to {download_path}')
            else:
                print(f'Failed to download file. Status code {response.status_code}')
        else:
            print("File not found:", download_path)
    except PermissionError:
        print("Permission Denied: You do not have the necessary permissions ot change this file.")

    # check if the request was successful
    '''if response.status_code == 200:
        with open(full_path, mode='wb') as file:
            file.write(response.content)
        print(f'file saved successfully to {full_path}')
    else:
        print(f'Failed to download file. Status code {response.status_code}')'''


def extract_links(chromedriver):
    links = [item for item in chromedriver if item.startswith('http')]
    return links


def create_wd():
    service = Service(chromedriver_path)
    return webdriver.Chrome(service=service, options=driver_option)


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

if platform.uname().system == 'Windows':
    create_new_folder(working_drivers[9])
    time.sleep(2)

browser.quit()
