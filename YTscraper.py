import time
import os
import csv
import pandas as pd
from Packages import Conversions


# import platform

# provides the main interface for controlling web browsers
from selenium import webdriver

# used to manage the lifecycle of browser driver executable, useful
# when configuring and starting the ChromeDriver service
from selenium.webdriver.chrome.service import Service

# an exception thrown when a command does not complete within a specified time
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException, \
    ElementClickInterceptedException, NoSuchElementException

# Provides predefined methods to locate elements on a webpage
from selenium.webdriver.common.by import By

# Used to wait for certain conditions to be met bf proceeding
from selenium.webdriver.support.ui import WebDriverWait

# Has a set of common conditions that are used when automation browser interactions
from selenium.webdriver.support import expected_conditions as EC

# You can use the Keys class to perform keyboard actions such as pressing Enter, Tab, Arrow keys, etc.
from selenium.webdriver.common.keys import Keys

# from selenium.webdriver import ActionChains

# File path of chromedriver
chromedriver_path = r"C:\Users\muket\Desktop\Chrome Drivers\chromedriver.exe"

driver_option = webdriver.ChromeOptions()
driver_option.add_argument('--incognito')

# create a panda df that reads csv file
df = pd.read_csv('YTdata.csv')


# allows for the creation of the webdriver to access
# website and open url

def create_wd():
    service = Service(chromedriver_path)
    return webdriver.Chrome(service=service, options=driver_option)


def downloadChromeDriver():
    """while True:
        if platform.uname().system == 'Windows':
            browser = create_wd()
            browser.get('https://googlechromelabs.github.io/chrome-for-testing/#stable')
            WebDriverWait(browser, 3).until(
                EC.presence_of_all_elements_located((By.XPATH, '//*[@id="stable"]'))
            )
            chrome_link = browser.find_element(By.XPATH, '//*[@id="stable"]')
            chrome_link.doubleClick()
            browser.get('https://www.google.com/')"""


def ask_db():
    while True:
        db_answer = input("Would you like to add to / create your YT database (y or n)? ").lower()
        try:
            if db_answer == 'y':
                print()
                # run all the functions in the conversion class
            elif db_answer == 'n':
                scrapeTwo = input(print('Would you like to scrape again?')).lower()
                if scrapeTwo == 'y':
                    scrape_yt()
                elif scrapeTwo == 'n':
                    print('Thank you for using YT scraper')
                    exit()
        except SyntaxError:
            print('Please enter an appropriate response')


# gives the option for user to run the script again
def run_again():
    while True:
        again = input("Would you like to enter another entry (y or n)? ").lower()
        try:
            if again == 'y':
                scrape_yt()
            elif again == 'n':
                print('Thank you for using YT scraper')
                exit()
        except SyntaxError:
            print('Please enter an appropriate response.')


# Create a CSV file accessible in Excel
# set pda=None so when it 'is not None' it is prepared to run
# could have done the same to either parameter
def create_csv(split_data, profile_data_after=None):
    # check if the file exists already
    file_exists = os.path.isfile("YTdata.csv")

    # Prepare data for writing
    if profile_data_after is not None:
        data_write = profile_data_after
    else:
        data_write = split_data

    # if the len of data is less than 6, N/A
    # is filled in for the missing parts
    if len(data_write) < 6:
        data_write += ['N/A'] * (6 - len(data_write))

    # if the file already exists then this will add new data
    # if not a new csv file is created with headers for data
    with open("YTdata.csv", 'a', newline="") as csvfile:
        write = csv.writer(csvfile)
        if not file_exists:
            write.writerow(["Link", "Subscriber Count", "Video Count", "Views", "Date Joined", "Country"])
        write.writerow(data_write)


#  Has the goal of scraping specified info from YT
# For now specifically title, eventually Views, video Publication, Creator, etc
def scrape_yt():
    # Get user search
    user_search = input("What would you like to search for: ")
    # Create wd and open yt
    browser = create_wd()
    browser.get('https://www.youtube.com/')

    # Wait for the specified XPATH to load before searching
    try:
        WebDriverWait(browser, 3).until(
            EC.element_to_be_clickable((By.NAME, "search_query"))
        )
        search_box = browser.find_element(By.NAME, "search_query")

        # Finds the search-input tag on the link
        # Access the search bar and enters user response
        search_box.click()
        search_box.send_keys(user_search)
        search_box.send_keys(Keys.RETURN)

    except TimeoutException:
        print('Timeout, waiting for search box to load')
        browser.quit()
    except (ElementNotInteractableException, ElementClickInterceptedException):
        print('Error, interacting with search box')
        browser.quit()

    time.sleep(2)

    try:
        # Another point to wait for specified XPATH before extracting
        WebDriverWait(browser, 3).until(
            EC.presence_of_all_elements_located((By.XPATH,
                                                 "//*[@id='text']"))
        )
        # Find and click link to requested profile
        yt_profile = browser.find_element(By.XPATH,
                                          "//*[@id='main-link']")
        yt_profile.click()
        time.sleep(2)
    except NoSuchElementException:
        print(f"{user_search} could not be found.")
        print()
        browser.quit()
        run_again()

    # Must access the 'more' tab to access data
    more_button = browser.find_element(By.CLASS_NAME,
                                       'truncated-text-wiz__absolute-button')
    more_button.click()

    # Point ot wait till we can find the description
    WebDriverWait(browser, 3).until(
        EC.presence_of_all_elements_located((By.XPATH,
                                             "//*[@id='description-container']"))
    )
    profile_description = browser.find_element(By.XPATH,
                                               "//*[@id='description-container']")

    WebDriverWait(browser, 3).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "tbody")))

    profile_data = browser.find_element(By.TAG_NAME, "tbody")

    print()
    print('Description:\n' + profile_description.text.replace('. ', '.\n'))
    print()
    # Split the collected data
    split_data = profile_data.text.split('\n')
    if len(split_data) > 6:
        # remove the first entry of the split data if there are over 6
        # data entries
        profile_data_after = split_data[1:]
        for profile in profile_data_after:
            print(profile)
        create_csv(split_data, profile_data_after)
    else:
        print(profile_data.text)
        print('-' * 10)
        print()
        create_csv(split_data)


# Datasets to change
sub_count = df['Subscriber Count'].astype(str)
vid_count = df['Video Count'].astype(str)
view_count = df['Views'].astype(str)
date_joined = df['Date Joined'].astype(str)

# Dataset conversions

# downloadChromeDriver()
# scrape_yt()
# run_again()
# ask_db()
