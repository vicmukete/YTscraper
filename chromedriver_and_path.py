import platform
import os
import requests
import zipfile
import stat
# import pyuac

# provides the main interface for controlling web browsers
from selenium import webdriver
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

# new path that holds the chromedriver
# new_path = os.path.join(download_path, 'chromedriver-win64.zip\chromedriver-win64')

# initial file path of chromedriver
chromedriver_path = r"C:\Users\muket\Desktop\Chrome Drivers\chromedriver.exe"

driver_option = webdriver.ChromeOptions()
driver_option.add_argument('--headless')


def extract_links(chromedriver):
    links = [item for item in chromedriver if item.startswith('http')]
    return links


def create_wd():
    service = Service(chromedriver_path)
    return webdriver.Chrome(service=service, options=driver_option)


# split a particular element in working driver by the /
# and take the last element of the split. (chromedriver-win64.zip)
# Extracts desired content from zip file links
def extract_end_from_link(link):
    last_element = link.split('/')
    print(f"You're now downloading this file: {last_element[-1]}")
    return last_element[-1]


def create_new_folder(url, filename):
    # ensure file path, download path, and zip path
    # Create the new folder if it doesn't already exist
    os.makedirs(download_path, exist_ok=True)
    full_zip_path = os.path.join(download_path, filename)
    response = requests.get(url)
    if response.status_code == 200:
        print(f'File saved successfully to - {full_zip_path}\n')
        # the following allows the content to be downloaded in chunks
        with open(full_zip_path, 'wb') as zip_file:
            for chunk in response.iter_content(chunk_size=1892):
                zip_file.write(chunk)
        # extract the zip file
        # the function extracts the wrong thing
        # fixing the file path fixes the function
        with (zipfile.ZipFile(full_zip_path, 'r') as zip_ref):
            for file_name in zip_ref.namelist():
                if 'chromedriver' in file_name:
                    if 'LICENSE' not in file_name and 'THIRD_PARTY_NOTICES' not in file_name:
                        # file_name = file_name.replace('chromedriver-win64/', '')
                        print(file_name)
                        extracted_path = zip_ref.extract(file_name, download_path)
                        print(extracted_path)
                        # will give the right permissions if the os is not windows
                        if os.name != 'nt':
                            os.chmod(extracted_path, stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
                else:
                    print('Chromedriver not found in the ZIP file')
    else:
        print(f'Failed to download file. Status Code: {response.status_code}')


# final function to download the chromedriver depending on os
def system_dependencies(driver):
    # new_filename1 = extract_end_from_link(driver).replace('.zip', '')
    create_new_folder(driver, 'chromedriver.exe')


# access link to download chromedrivers
# move the main script to the top of the file
# move extract_links above main script
browser = create_wd()
browser.get('https://googlechromelabs.github.io/chrome-for-testing/#stable')
WebDriverWait(browser, 3).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="stable"]'))
)
chrome_link = browser.find_element(By.XPATH, '//*[@id="stable"]').text
chromedrivers = chrome_link.split()
working_drivers = (extract_links(chromedrivers))
machine_system = platform.uname().system

# Print computer information
print(f"Machine System: {platform.uname().system}")
print(f"Machine Name: {platform.uname().node}\n")
print("List of Drivers: ")

# Print the list of drivers and their indexes
for index, value in enumerate(working_drivers):
    print(index, value)

print()

browser.quit()


# Checks computer os and downloads chromedriver depending
# on os
def check_os():
    if machine_system == 'Darwin':
        system_dependencies(working_drivers[6])
    if machine_system == 'Windows':
        system_dependencies(working_drivers[9])
    if machine_system == 'Linux':
        system_dependencies(working_drivers[5])
