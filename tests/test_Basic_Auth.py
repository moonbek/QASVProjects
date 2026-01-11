

from Selenium_Training_Internet.tests import utils as u

class Basic_auth(u.unittest.TestCase):
    def setUp(self):
        self.driver = u.webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = u.WDW(self.driver, 10)

    def test_basic_auth(self):
        driver = self.driver

        #Goin to The main page
        driver.get(u.BASE_URL)
        self.wait.until(u.EC.title_contains("The Internet"))
        

        #CLick on Basic auth link
        self.wait.until(u.EC.element_to_be_clickable((u.By.XPATH, "//a[normalize-space()='Basic Auth']"))).click()

        #Going to The Basic auth page
        driver.get("https://admin:admin@The-internet.herokuapp.com/basic_auth")
        msg = self.wait.until(u.EC.visibility_of_element_located((u.By.CSS_SELECTOR, "p"))).text
        self.assertEqual(msg, "Congratulations! You must have the proper credentials.")
        print(msg)
        


    def tearDown(self):
        self.driver.quit()
if __name__ == "__main__":
    u.unittest.main()
