#Imports
import unittest
from selenium import webdriver
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains



#Config
BASE_URL = "https://the-internet.herokuapp.com/"
WAIT_TIME = 10

#Locators
ADD_REMOVE_LINK = (By.XPATH, "//a[normalize-space()='Add/Remove Elements']")
ADD_ELEMENT_BUTTON = (By.XPATH, "//button[normalize-space()='Add Element']")
DELETE_BUTTONS = (By.XPATH, "//button[normalize-space()='Delete']")

#uelper functions
def delay(min_delay=2, max_delay=4):
    time.sleep(random.randint(min_delay, max_delay))

def open_home(driver):
    driver.get(BASE_URL)

def click(driver, locator):
    WebDriverWait(driver, WAIT_TIME).until(EC.element_to_be_clickable(locator)).click()

def count(driver, locator):
    return len(driver.find_elements(*locator))


def click_n_times(driver, locator, n):
    for _ in range(n):
        click(driver, locator)

def delete_all(driver, locator):
    total = count(driver, locator)
    for _ in range(total):
        click(driver, locator)

