
#Python Selenium WebDriver Unitests - Cross-Browser Automation Framework

import time
from selenium import webdriver
import requests
import os
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import random
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options as Edge_Options



def delay():
    time.sleep(random.randint(2,4))

def take_screenshot(driver):
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"screenshots_Wiki/error_{now}.png"
    os.makedirs("screenshots_Wiki", exist_ok=True)
    driver.save_screenshot(filename)
    print(f"Screenshot saved to {filename}")


class Chrome_RealEstate(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--disable-link-features=AutomationControlled")
        self.driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()


    def test_real_estate_Max(self):
        driver = self.driver
        driver.get("https://qasvus.wordpress.com/")

        delay()

        #API testing from Selenium
        print("California Real Estate Url has", requests.get("https://qasvus.wordpress.com/").status_code, "as status Code")
        code = requests.get("https://qasvus.wordpress.com/").status_code
        if code == 200:
            print("API response code is OK")
        else:
            print("API response code is not OK")

        wait = WebDriverWait(driver, 10)
        wait.until(EC.title_contains("California Real Estate"))

        self.assertIn("California Real Estate", driver.title, "Wrong title on main page")
        print("MAIN PAGE TITLE:", driver.title)

        # if "California Real Estate" not in driver.title:
        #     raise Exception("California Real Estate page has wrong Title")
        delay()
        #driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)

        header = driver.find_element(By.ID, "send-us-a-message")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", header)
        self.assertEqual(header.text, "Send Us a Message")
        print("HEADER TEXT:", header.text)


        delay()


        #Verify 'Send Us a Message':
        try:
            driver.find_element(By.ID, "send-us-a-message")
            print("Test result: Page has 'Send Us a Message' text")
        except WDE:
            print("Test result: No Page text is visible ")

        delay()

        #CLear fields:
        driver.find_element(By.ID, "g2-name").clear()
        driver.find_element(By.ID, "g2-email").clear()
        driver.find_element(By.ID, "contact-form-comment-g2-message").clear()

        #Filling the form:
        try:
            #driver.find_element(By.ID, "g2-name").click()
            driver.find_element(By.ID, "g2-name").send_keys("David Gilmor")
            print("Test result: Input Name field is visible and filled out")
            driver.find_element(By.ID, "g2-email").send_keys("david@gilmor.com")
            print("Test result: Input Email field is visible and filled out")
            davidsMessage = "I took a heavenly ride through our silence. I knew the moment had arrived. For killing the past and coming back to life"
            driver.find_element(By.ID, "contact-form-comment-g2-message").send_keys(davidsMessage)
            print("Test result: Message field is visible and filled out")
        except WDE:
            print("Test result: No Input Name field is visible")


        #Clicking the submit button:
        try:
            driver.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()
            wait.until(EC.title_contains("California Real Estate"))
            self.assertIn("California Real Estate", driver.title, "Wrong title after submit")
            print("AFTER SUBMIT TITLE:", driver.title)

            print("Test result: Submit Button is visible and clicked")
        except WDE:
            print("Test result: No Submit button is visible")



        #Verify and Clicked "Go back" link:
        try:
            go_back = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Go back")))
            go_back.click()

            print("Test result: Go back link visible and clicked")
        except WDE:
            print("Test result: No Go back link is visible")

        #Negaitve test "Submit" button:
        try:
            driver.find_element(By.XPATH, "//button[normalize-space()='Submit']")
            print("Test result: Submit button is visible")
        except WDE:
            print("Test result: No Submit button is visible")
    def test_real_estate_1820x1050(self):
        driver = self.driver
        self.driver.set_window_size(1820, 1050)
        driver.get("https://qasvus.wordpress.com/")
        delay()

        #API testing from Selenium
        print("California Real Estate Url has", requests.get("https://qasvus.wordpress.com/").status_code, "as status Code")
        code = requests.get("https://qasvus.wordpress.com/").status_code
        if code == 200:
            print("API response code is OK")
        else:
            print("API response code is not OK")

        wait = WebDriverWait(driver, 10)
        wait.until(EC.title_contains("California Real Estate"))

        self.assertIn("California Real Estate", driver.title, "Wrong title on main page")
        print("MAIN PAGE TITLE:", driver.title)

        # if "California Real Estate" not in driver.title:
        #     raise Exception("California Real Estate page has wrong Title")
        delay()
        #driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)

        header = driver.find_element(By.ID, "send-us-a-message")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", header)
        self.assertEqual(header.text, "Send Us a Message")
        print("HEADER TEXT:", header.text)


        delay()


        #Verify 'Send Us a Message':
        try:
            driver.find_element(By.ID, "send-us-a-message")
            print("Test result: Page has 'Send Us a Message' text")
        except WDE:
            print("Test result: No Page text is visible ")

        delay()

        #CLear fields:
        driver.find_element(By.ID, "g2-name").clear()
        driver.find_element(By.ID, "g2-email").clear()
        driver.find_element(By.ID, "contact-form-comment-g2-message").clear()

        #Filling the form:
        try:
            #driver.find_element(By.ID, "g2-name").click()
            driver.find_element(By.ID, "g2-name").send_keys("David Gilmor")
            print("Test result: Input Name field is visible and filled out")
            driver.find_element(By.ID, "g2-email").send_keys("david@gilmor.com")
            print("Test result: Input Email field is visible and filled out")
            davidsMessage = "I took a heavenly ride through our silence. I knew the moment had arrived. For killing the past and coming back to life"
            driver.find_element(By.ID, "contact-form-comment-g2-message").send_keys(davidsMessage)
            print("Test result: Message field is visible and filled out")
        except WDE:
            print("Test result: No Input Name field is visible")


        #Clicking the submit button:
        try:
            driver.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()
            wait.until(EC.title_contains("California Real Estate"))
            self.assertIn("California Real Estate", driver.title, "Wrong title after submit")
            print("AFTER SUBMIT TITLE:", driver.title)

            print("Test result: Submit Button is visible and clicked")
        except WDE:
            print("Test result: No Submit button is visible")



        #Verify and Clicked "Go back" link:
        try:
            go_back = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Go back")))
            go_back.click()

            print("Test result: Go back link visible and clicked")
        except WDE:
            print("Test result: No Go back link is visible")

        #Negaitve test "Submit" button:
        try:
            driver.find_element(By.XPATH, "//button[normalize-space()='Submit']")
            print("Test result: Submit button is visible")
        except WDE:
            print("Test result: No Submit button is visible")


    def tearDown(self):
        self.driver.quit()

class Edge_RealEstate(unittest.TestCase):

    def setUp(self):
        os.environ["SE_DRIVER_MIRROR_URL"] = "https://msedgedriver.microsoft.com"
        options = Edge_Options()
        options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = webdriver.Edge(options=options)
        self.driver.maximize_window()

    def test_real_estate_Max(self):
        driver = self.driver
        driver.get("https://qasvus.wordpress.com/")

        delay()

        # API testing from Selenium
        print("California Real Estate Url has", requests.get("https://qasvus.wordpress.com/").status_code,
              "as status Code")
        code = requests.get("https://qasvus.wordpress.com/").status_code
        if code == 200:
            print("API response code is OK")
        else:
            print("API response code is not OK")

        wait = WebDriverWait(driver, 10)
        wait.until(EC.title_contains("California Real Estate"))

        self.assertIn("California Real Estate", driver.title, "Wrong title on main page")
        print("MAIN PAGE TITLE:", driver.title)

        # if "California Real Estate" not in driver.title:
        #     raise Exception("California Real Estate page has wrong Title")
        delay()
        # driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)

        header = driver.find_element(By.ID, "send-us-a-message")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", header)
        self.assertEqual(header.text, "Send Us a Message")
        print("HEADER TEXT:", header.text)

        delay()

        # Verify 'Send Us a Message':
        try:
            driver.find_element(By.ID, "send-us-a-message")
            print("Test result: Page has 'Send Us a Message' text")
        except WDE:
            print("Test result: No Page text is visible ")

        delay()

        # CLear fields:
        driver.find_element(By.ID, "g2-name").clear()
        driver.find_element(By.ID, "g2-email").clear()
        driver.find_element(By.ID, "contact-form-comment-g2-message").clear()

        # Filling the form:
        try:
            # driver.find_element(By.ID, "g2-name").click()
            driver.find_element(By.ID, "g2-name").send_keys("David Gilmor")
            print("Test result: Input Name field is visible and filled out")
            driver.find_element(By.ID, "g2-email").send_keys("david@gilmor.com")
            print("Test result: Input Email field is visible and filled out")
            davidsMessage = "I took a heavenly ride through our silence. I knew the moment had arrived. For killing the past and coming back to life"
            driver.find_element(By.ID, "contact-form-comment-g2-message").send_keys(davidsMessage)
            print("Test result: Message field is visible and filled out")
        except WDE:
            print("Test result: No Input Name field is visible")

        # Clicking the submit button:
        try:
            driver.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()
            wait.until(EC.title_contains("California Real Estate"))
            self.assertIn("California Real Estate", driver.title, "Wrong title after submit")
            print("AFTER SUBMIT TITLE:", driver.title)

            print("Test result: Submit Button is visible and clicked")
        except WDE:
            print("Test result: No Submit button is visible")

        # Verify and Clicked "Go back" link:
        try:
            go_back = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Go back")))
            go_back.click()

            print("Test result: Go back link visible and clicked")
        except WDE:
            print("Test result: No Go back link is visible")

        # Negaitve test "Submit" button:
        try:
            driver.find_element(By.XPATH, "//button[normalize-space()='Submit']")
            print("Test result: Submit button is visible")
        except WDE:
            print("Test result: No Submit button is visible")
    def test_real_estate_1820x1050(self):
        driver = self.driver
        self.driver.set_window_size(1820, 1050)
        driver.get("https://qasvus.wordpress.com/")
        delay()

        # API testing from Selenium
        print("California Real Estate Url has", requests.get("https://qasvus.wordpress.com/").status_code,
              "as status Code")
        code = requests.get("https://qasvus.wordpress.com/").status_code
        if code == 200:
            print("API response code is OK")
        else:
            print("API response code is not OK")

        wait = WebDriverWait(driver, 10)
        wait.until(EC.title_contains("California Real Estate"))

        self.assertIn("California Real Estate", driver.title, "Wrong title on main page")
        print("MAIN PAGE TITLE:", driver.title)

        # if "California Real Estate" not in driver.title:
        #     raise Exception("California Real Estate page has wrong Title")
        delay()
        # driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)

        header = driver.find_element(By.ID, "send-us-a-message")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", header)
        self.assertEqual(header.text, "Send Us a Message")
        print("HEADER TEXT:", header.text)

        delay()

        # Verify 'Send Us a Message':
        try:
            driver.find_element(By.ID, "send-us-a-message")
            print("Test result: Page has 'Send Us a Message' text")
        except WDE:
            print("Test result: No Page text is visible ")

        delay()

        # CLear fields:
        driver.find_element(By.ID, "g2-name").clear()
        driver.find_element(By.ID, "g2-email").clear()
        driver.find_element(By.ID, "contact-form-comment-g2-message").clear()

        # Filling the form:
        try:
            # driver.find_element(By.ID, "g2-name").click()
            driver.find_element(By.ID, "g2-name").send_keys("David Gilmor")
            print("Test result: Input Name field is visible and filled out")
            driver.find_element(By.ID, "g2-email").send_keys("david@gilmor.com")
            print("Test result: Input Email field is visible and filled out")
            davidsMessage = "I took a heavenly ride through our silence. I knew the moment had arrived. For killing the past and coming back to life"
            driver.find_element(By.ID, "contact-form-comment-g2-message").send_keys(davidsMessage)
            print("Test result: Message field is visible and filled out")
        except WDE:
            print("Test result: No Input Name field is visible")

        # Clicking the submit button:
        try:
            driver.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()
            wait.until(EC.title_contains("California Real Estate"))
            self.assertIn("California Real Estate", driver.title, "Wrong title after submit")
            print("AFTER SUBMIT TITLE:", driver.title)

            print("Test result: Submit Button is visible and clicked")
        except WDE:
            print("Test result: No Submit button is visible")

        # Verify and Clicked "Go back" link:
        try:
            go_back = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Go back")))
            go_back.click()

            print("Test result: Go back link visible and clicked")
        except WDE:
            print("Test result: No Go back link is visible")

        # Negaitve test "Submit" button:
        try:
            driver.find_element(By.XPATH, "//button[normalize-space()='Submit']")
            print("Test result: Submit button is visible")
        except WDE:
            print("Test result: No Submit button is visible")

    def tearDown(self):
        self.driver.quit()

class Firefox_RealEstate(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.maximize_window()

    def test_real_estate_Max(self):
        driver = self.driver
        driver.get("https://qasvus.wordpress.com/")

        delay()

        #API testing from Selenium
        print("California Real Estate Url has", requests.get("https://qasvus.wordpress.com/").status_code, "as status Code")
        code = requests.get("https://qasvus.wordpress.com/").status_code
        if code == 200:
            print("API response code is OK")
        else:
            print("API response code is not OK")

        wait = WebDriverWait(driver, 10)
        wait.until(EC.title_contains("California Real Estate"))

        self.assertIn("California Real Estate", driver.title, "Wrong title on main page")
        print("MAIN PAGE TITLE:", driver.title)

        # if "California Real Estate" not in driver.title:
        #     raise Exception("California Real Estate page has wrong Title")
        delay()
        #driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)

        header = driver.find_element(By.ID, "send-us-a-message")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", header)
        self.assertEqual(header.text, "Send Us a Message")
        print("HEADER TEXT:", header.text)


        delay()


        #Verify 'Send Us a Message':
        try:
            driver.find_element(By.ID, "send-us-a-message")
            print("Test result: Page has 'Send Us a Message' text")
        except WDE:
            print("Test result: No Page text is visible ")

        delay()

        #CLear fields:
        driver.find_element(By.ID, "g2-name").clear()
        driver.find_element(By.ID, "g2-email").clear()
        driver.find_element(By.ID, "contact-form-comment-g2-message").clear()

        #Filling the form:
        try:
            #driver.find_element(By.ID, "g2-name").click()
            driver.find_element(By.ID, "g2-name").send_keys("David Gilmor")
            print("Test result: Input Name field is visible and filled out")
            driver.find_element(By.ID, "g2-email").send_keys("david@gilmor.com")
            print("Test result: Input Email field is visible and filled out")
            davidsMessage = "I took a heavenly ride through our silence. I knew the moment had arrived. For killing the past and coming back to life"
            driver.find_element(By.ID, "contact-form-comment-g2-message").send_keys(davidsMessage)
            print("Test result: Message field is visible and filled out")
        except WDE:
            print("Test result: No Input Name field is visible")


        #Clicking the submit button:
        try:
            driver.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()
            wait.until(EC.title_contains("California Real Estate"))
            self.assertIn("California Real Estate", driver.title, "Wrong title after submit")
            print("AFTER SUBMIT TITLE:", driver.title)

            print("Test result: Submit Button is visible and clicked")
        except WDE:
            print("Test result: No Submit button is visible")



        #Verify and Clicked "Go back" link:
        try:
            go_back = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Go back")))
            go_back.click()

            print("Test result: Go back link visible and clicked")
        except WDE:
            print("Test result: No Go back link is visible")

        #Negaitve test "Submit" button:
        try:
            driver.find_element(By.XPATH, "//button[normalize-space()='Submit']")
            print("Test result: Submit button is visible")
        except WDE:
            print("Test result: No Submit button is visible")
    def test_real_estate_1820x1050(self):
        driver = self.driver
        self.driver.set_window_size(1820, 1050)
        driver.get("https://qasvus.wordpress.com/")
        delay()

        #API testing from Selenium
        print("California Real Estate Url has", requests.get("https://qasvus.wordpress.com/").status_code, "as status Code")
        code = requests.get("https://qasvus.wordpress.com/").status_code
        if code == 200:
            print("API response code is OK")
        else:
            print("API response code is not OK")

        wait = WebDriverWait(driver, 10)
        wait.until(EC.title_contains("California Real Estate"))

        self.assertIn("California Real Estate", driver.title, "Wrong title on main page")
        print("MAIN PAGE TITLE:", driver.title)

        # if "California Real Estate" not in driver.title:
        #     raise Exception("California Real Estate page has wrong Title")
        delay()
        #driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)

        header = driver.find_element(By.ID, "send-us-a-message")
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", header)
        self.assertEqual(header.text, "Send Us a Message")
        print("HEADER TEXT:", header.text)


        delay()


        #Verify 'Send Us a Message':
        try:
            driver.find_element(By.ID, "send-us-a-message")
            print("Test result: Page has 'Send Us a Message' text")
        except WDE:
            print("Test result: No Page text is visible ")

        delay()

        #CLear fields:
        driver.find_element(By.ID, "g2-name").clear()
        driver.find_element(By.ID, "g2-email").clear()
        driver.find_element(By.ID, "contact-form-comment-g2-message").clear()

        #Filling the form:
        try:
            #driver.find_element(By.ID, "g2-name").click()
            driver.find_element(By.ID, "g2-name").send_keys("David Gilmor")
            print("Test result: Input Name field is visible and filled out")
            driver.find_element(By.ID, "g2-email").send_keys("david@gilmor.com")
            print("Test result: Input Email field is visible and filled out")
            davidsMessage = "I took a heavenly ride through our silence. I knew the moment had arrived. For killing the past and coming back to life"
            driver.find_element(By.ID, "contact-form-comment-g2-message").send_keys(davidsMessage)
            print("Test result: Message field is visible and filled out")
        except WDE:
            print("Test result: No Input Name field is visible")


        #Clicking the submit button:
        try:
            driver.find_element(By.XPATH, "//button[normalize-space()='Submit']").click()
            wait.until(EC.title_contains("California Real Estate"))
            self.assertIn("California Real Estate", driver.title, "Wrong title after submit")
            print("AFTER SUBMIT TITLE:", driver.title)

            print("Test result: Submit Button is visible and clicked")
        except WDE:
            print("Test result: No Submit button is visible")



        #Verify and Clicked "Go back" link:
        try:
            go_back = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Go back")))
            go_back.click()

            print("Test result: Go back link visible and clicked")
        except WDE:
            print("Test result: No Go back link is visible")

        #Negaitve test "Submit" button:
        try:
            driver.find_element(By.XPATH, "//button[normalize-space()='Submit']")
            print("Test result: Submit button is visible")
        except WDE:
            print("Test result: No Submit button is visible")


    def tearDown(self):
        self.driver.quit()



