"""
HTML Report Selenium Tests (Cross-Browser)

How to run this test file and generate the HTML report:

1) Run the test from Terminal (from the project root folder):
   python HTML_AmericanIdol_Reporting.py
   or
   python3 HTML_AmericanIdol_Reporting.py

2) Wait until the tests finish.

3) Open the generated HTML report:
   - Check the "HtmlReports" folder in the project root.
   - Open the latest report file in your browser.
"""



import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
import HtmlTestRunner


class ABCTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://abc.com/")
        cls.driver.maximize_window()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def checkElementVisibility(self, by, locator, element_name):
        try:
            element = self.driver.find_element(by, locator)
            self.assertTrue(element.is_displayed(), f"{element_name} is not displayed")
            print(f"{element_name} is displayed")
        except WebDriverException:
            self.fail(f"{element_name} is not found")

    def test_01_title(self):
        self.assertIn("ABC", self.driver.title)

    def test_02_logo(self):
        self.checkElementVisibility(By.XPATH, "//div[@class='navigation__group']//img[@alt='ABC']", "Logo")

    # ... и так далее: test_03_..., test_04_...


if __name__ == '__main__':
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports')
    )
