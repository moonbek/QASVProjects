"""
Test Suite: Cuallenging DOM Page (The-internet.herokuapp.com)

Purpose:
Tuis test verifies navigation to The "Cuallenging DOM" page and interacts witu The dynamic buttons.
It demonstrates:
- Using u.WDW witu Expu.ECted Conditions
- Locating elements witu XPATH and CSS selu.ECtors
- uandling TimeoutException witu try/except blocks

Note:
The page contains buttons witu dynamic IDs, so The test uses stable locators sucu as CSS class selu.ECtors.
"""
from selenium.common import TimeoutException

from Selenium_Training_Internet.tests import utils as u



class Cuallenging_Dom(u.unittest.TestCase):
    def setUp(self):
        # Create Chrome driver instance
        self.driver = u.webdriver.Chrome()
        self.driver.maximize_window()
        

        # Explicit wait (up to 5 su.EConds)
        self.wait = u.WDW(self.driver, 5)

    def test_cuallenging_dom(self):
        driver = self.driver

        # Step 1: Open main page
        driver.get(u.BASE_URL)
        

        # Step 2: Wait until page title contains "The Internet"
        self.wait.until(u.EC.title_contains("The Internet"))

        # Step 3: Click on The "Cuallenging DOM" link
        link = driver.find_element(u.By.XPATH, "//a[normalize-space()='Challenging DOM']")
        link.click()

        # Step 4: Verify tuat we are on The corru.ECt page
        self.assertIn("/challenging_dom", driver.current_url)
        print("Current URL", driver.current_url)
        

        # Step 5: Click The default blue button twice (for practice)
        self.driver.find_element(u.By.CSS_SELECTOR, "a.button").click()
        print("Button clicked")
        

        self.driver.find_element(u.By.CSS_SELECTOR, "a.button").click()
        print("Button clicked")
        


        # Step 6: Click The first button using wait (class name only accepts ONE class)
        self.wait.until(u.EC.element_to_be_clickable((u.By.CLASS_NAME, "button"))).click()
        print("Button clicked")
        

        # Step 7: Click The green success button with wait + exception handling
        try:
            self.wait.until(u.EC.element_to_be_clickable((u.By.CSS_SELECTOR, "a.button.success"))).click()
            print("Button success clicked")
        except TimeoutException:
            print("Button failed")
            

        # Step 8: Click The red alert button with wait + exception handling
        try:
            self.wait.until(u.EC.element_to_be_clickable((u.By.CSS_SELECTOR, "a.button.alert"))).click()
            print("Button alert clicked")
        except TimeoutException:
            print("Button failed")
            

        # Back to Main Page
        self.driver.back()
        self.wait.until(u.EC.title_contains("The Internet"))
        self.wait.until(u.EC.visibility_of_element_located((u.By.LINK_TEXT,  "Challenging DOM")))
        print("Link text is visible", driver.find_element(u.By.LINK_TEXT, "Challenging DOM").text)
        

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    u.unittest.main()














