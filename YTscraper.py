import time

# provides the main interface for controlling web browsers
from selenium import webdriver

# used to manage the lifecycle of browser driver executable, useful
# when configuring and starting the ChromeDriver service
from selenium.webdriver.chrome.service import Service

# an exception thrown when a command does not complete within a specified time
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException, \
    ElementClickInterceptedException

# Provides predefined methods to locate elements on a webpage
from selenium.webdriver.common.by import By

# Used to wait for certain conditions to be met bf proceeding
from selenium.webdriver.support.ui import WebDriverWait

# Has a set of common conditions that are used when automation browser interactions
from selenium.webdriver.support import expected_conditions as EC

# You can use the Keys class to perform keyboard actions such as pressing Enter, Tab, Arrow keys, etc.
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager

# File path of chromedriver
chromedriver_path = r"C:\Users\muket\Desktop\chromedriver.exe"

driver_option = webdriver.ChromeOptions()
driver_option.add_argument('--incognito')


# allows for the creation of the webdriver to access
# website and open url
def create_webdriver():
    service = Service(chromedriver_path)
    return webdriver.Chrome(service=service, options=driver_option)


# Get user search
user_search = input("What would you like to search for: ")


def run_again():
    while True:
        again = input("Would you like to enter another entry (y or n)? ").lower()
        if again == 'y':
            scrape_yt()
        elif again == 'n':
            print('Thank you for using YT scraper')
            exit()
        else:
            print('Please enter an appropriate response.')


#  Has the goal of scraping specified info from YT
# For now specifically title, eventually Views, video Publication, Creator, etc
def scrape_yt():
    browser = create_webdriver()
    browser.get('https://www.youtube.com/')

    # Wait for the specified XPATH to load before searching
    try:
        WebDriverWait(browser, 15).until(
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

    time.sleep(5)

    # Another point to wait for specified XPATH before extracting
    WebDriverWait(browser, 3).until(
        EC.presence_of_all_elements_located((By.XPATH,
                                             "//*[@id='text']"))
    )
    # Find and click link to requested profile
    yt_profile = browser.find_element(By.XPATH,
                                      "//*[@id='main-link']")
    # Clicks on first profile generated
    yt_profile.click()
    time.sleep(3)

    # Must access the 'more' tab to access data
    more_button = browser.find_element(By.CLASS_NAME,
                                       'truncated-text-wiz__absolute-button')
    more_button.click()

    # Point ot wait till we can find the description
    WebDriverWait(browser, 5).until(
        EC.presence_of_all_elements_located((By.XPATH,
                                             "//*[@id='description-container']"))
    )
    description = browser.find_element(By.XPATH,
                                       "//*[@id='description-container']")

    # acct_link = browser.find_element(By.XPATH, "//*[@class='ytd-about-channel-renderer']")
    profile_data = browser.find_element(By.XPATH, "//*[@id='additional-info-container']")
    # vid_count = browser.find_element(By.XPATH, "//*[@class='ytd-about-channel-renderer']")
    # views = browser.find_element(By.XPATH, "//*[@class='ytd-about-channel-renderer']")
    # date_joined = browser.find_element(By.XPATH, "//*[@class='ytd-about-channel-renderer']")
    # og_country = browser.find_element(By.XPATH, "//*[@class='ytd-about-channel-renderer']")

    # Split the collected data and remove the first two entries
    profile_details_bf = profile_data.text.split('\n')
    profile_details = profile_details_bf[2:]
    # Remove the first two lines of collected data
    if len(profile_details) >= 6:
        print()
        print('Description:\n' + description.text.replace('. ', '.\n'))
        print()
        print('Profile Details:')
        print(f'Link: {profile_details[0]}')
        print(f'Subscriber Count: {profile_details[1]}')
        print(f'Video Count: {profile_details[2]}')
        print(f'Views: {profile_details[3]}')
        print(f'Date Joined: {profile_details[4]}')
        print(f'Country: {profile_details[5]}')
    else:
        print('Profile data could not be extracted correctly.')


scrape_yt()
# run_again()

'''
Further Steps:

Click on first user profile link
Access the 'more' link in the bio
Scrape the data in channel details
Store in excel/pandas

After scraping YT data once:

Navigate to previous page
Select the next user profile link
Repeat above process
Repeat all processes for desired amount of times
'''
