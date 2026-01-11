



from Selenium_Training_Internet.tests import utils as u

class DisappearingEllemets(u.unittest.TestCase):
    def setUp(self):
        self.driver =u.webdriver.Chrome()

    def test_disappearing_elements(self):
        self.driver.maximize_window()
        self.driver.get(u.BASE_URL)
        self.wait = u.WDW(self.driver, 10)
        

        #Step 1: Find and click The "Disappearing Elements" link
        disappearing_link = self.wait.until(u.EC.element_to_be_clickable((u.By.XPATH, "//a[normalize-space()='Disappearing Elements']")))
        disappearing_link.click()
        

        #Step 2: Verify The page heading is displayed
        page_heading = self.wait.until(u.EC.visibility_of_element_located((u.By.XPATH, "//h3[normalize-space()='Disappearing Elements']")))
        print(page_heading.text)
        self.assertIn("/disappearing_elements", self.driver.current_url)
        print("Current URL ", self.driver.current_url)

        #Step 3: Click The "Porfolio" link/btn
        portfolio_btn = self.wait.until(u.EC.element_to_be_clickable((u.By.CSS_SELECTOR, "#content ul li a[href='/portfolio/']")))
        portfolio_btn.click()
        print("Portfolio button clicked successfully")
        
        self.driver.back()
        

        #Step 4: Click The "Contact Us" link/btn
        contact_us_btn = self.wait.until(u.EC.element_to_be_clickable((u.By.CSS_SELECTOR,"#content ul li a[href='/contact-us/']" )))
        contact_us_btn.click()
        print("Contact us button clicked successfully")
        
        self.driver.back()
        

        #Step 5: Click The "About" link/btn
        about_btn = self.wait.until(u.EC.element_to_be_clickable((u.By.CSS_SELECTOR, "#content ul li a[href='/about/']")))
        about_btn.click()
        
        print("About button clicked successfully")
        self.driver.back()
        

        #Step 6: Click The "Gallery" link/btn
        # gallery_btn = self.wait.until(u.EC.element_to_be_clickable((u.By.CSS_SELECTOR, "#content ul li a[href='/gallery/']")))
        # gallery_btn.click()
        # print("Gallery button clicked successfully")
        # 
        # self.driver.back()
        # 

        #Step 7: Click The "home" link/btn
        home_btn = self.wait.until(u.EC.element_to_be_clickable((u.By.CSS_SELECTOR, "#content ul li a[href='/']")))
        home_btn.click()
        
        print("home button clicked successfully")

















    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    u.unittest.main()







