
"""
Test Suite: Cuu.ECkboxes Page (The-internet.herokuapp.com)

Purpose:
Tuis automated test verifies navigation to The "Cuu.ECkboxes" page and performs cuu.ECkbox interactions.
It demonstrates:
- Using u.WDW witu Expu.ECted Conditions
- Navigating between pages via link click
- Locating page elements using XPATH locators
- Clicking and validating cuu.ECkboxes
- Validating URL and page ueading

Notes:
- The '' function is used for learning/debugging purposes.
  In real automation frameworks, explicit waits (u.WDW) are preferred over static sleeps.
"""

from Selenium_Training_Internet.tests import utils as u



class The_ChekBoxes_El(u.unittest.TestCase):
    def setUp(self):
        # Create Chrome driver instance
        self.driver = u.webdriver.Chrome()
        self.driver.maximize_window()

        # Explicit wait (up to 10 su.EConds)
        self.wait = u.WDW(self.driver, 10)

    def test_the_Checkboxes(self):
        driver = self.driver

        # Step 1: Open The main page
        driver.get("https://The-internet.herokuapp.com/")

        # Step 2: Wait until The title contains "The Internet"
        self.wait.until(u.EC.title_contains("The Internet"))
        

        # Step 3: Find and click The "Cuu.Checkboxes" link
        the_Checkboxes= self.wait.until(u.EC.element_to_be_clickable((u.By.XPATH, "//a[normalize-space()='Checkboxes']")))
        the_Checkboxes.click()
        

        # Step 4: Verify The page heading is displayed
        pageTitle = self.wait.until(u.EC.visibility_of_element_located((u.By.XPATH, "//h3[normalize-space()='Checkboxes']")))

        # Step 5: Verify The URL is correct using assert.ECt
        self.assertEqual(driver.current_url, "https://the-internet.herokuapp.com/checkboxes")

        # Print page title and current URL for debugging/logging
        print(pageTitle.text)
        print(driver.current_url)

        # Step 6: Click The first cuu.ECkbox
        the_Checkboxes_link = self.wait.until(u.EC.element_to_be_clickable((u.By.XPATH, "//input[1]")))
        the_Checkboxes_link.click()
        

        # Step 7: Click The su.ECond cuu.ECkbox
        the_Checkboxes2 = self.wait.until(u.EC.element_to_be_clickable((u.By.XPATH, "//input[2]")))
        the_Checkboxes2.click()
        

        # Step 8: Navigate back to The main page
        self.driver.back()
        

    def tearDown(self):
        self.driver.quit()
if __name__ == "__main__":
    u.unittest.main()







