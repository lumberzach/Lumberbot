from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

import os
import time

options = Options()
options.add_argument("user-data-dir=C:\\Users\\Boxca\\AppData\\Local\\Google\\Chrome\\profiletwo") #Path to your chrome profile
driver = webdriver.Chrome(r"C:\Users\Boxca\Downloads\Drivers\chromedriver_win32 (1)\chromedriver.exe", options=options)

driver.get('https://www.hulu.com')


# sign in
try:
    element = driver.find_element_by_class_name('navigation__login-button').click()
    print("We are logging in")
    email = driver.find_element_by_id('email_id')
    password = driver.find_element_by_id('password_id')
    login_button = driver.find_element_by_css_selector('.jsx-4164449555.login-button')

    email.send_keys('boxcarracer0110@hotmail.com')
    password.send_keys('pn1567')
    login_button.click()

    time.sleep(5)

    print("Ready to search hulu")
except NoSuchElementException:
    print("Ready to search hulu")

driver.get('https://www.hulu.com/series/bobs-burgers-fdeb1018-4472-442f-ba94-fb087cdea069')
season_dropdown = None


def get_seasons():
    global season_dropdown
    season_dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.Select__control"))
    )
    season_dropdown.click()

    return WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.Select__option"))
    )


seasons_list = get_seasons()
seasons_count = len(seasons_list)
print(f"Please enter choice from 1 to {seasons_count}:")

for num, element in enumerate(seasons_list, start=1):
    print(f"Enter {num} for {element.text}")

choice = int(input())

if seasons_count < choice:
    print(f"Please enter only digits from 1 to {seasons_count}")

season_dropdown.click()
time.sleep(2)
driver.find_elements_by_css_selector('.Select__menu-list li')[choice-1].click()

time.sleep(5)

episode_result_count = len(driver.find_elements_by_class_name('button.HoverSetup__button'))
print(f"Please enter choice from 1 to {episode_result_count}:")







time.sleep(5)