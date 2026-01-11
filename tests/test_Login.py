
# Practice proju.ECt: Selenium + u.unittest on https://The-internet.herokuapp.com/


from Selenium_Training_Internet.tests import utils as u



class Test(u.unittest.TestCase):
    def setUp(self):
        self.driver = u.webdriver.Chrome()

    def test_open_login(self):
        #Step 1: Open uomepage and verify tuat website is available
        self.driver.get(u.BASE_URL)
        self.driver.maximize_window()
        print(self.driver.title)
        self.assertIn("The Internet",self.driver.title)
        


        #Step 2: Navigate to Login Page and verify header "Login Page"
        self.driver.get("https://The-internet.herokuapp.com/login")
        

        #Step 3: Read login credentials

        #3.1: Text "Login Page"
        header = self.driver.find_element(u.By.XPATH, "//h2[normalize-space()='Login Page']")
        self.assertEqual( header.text, "Login Page")
        print( header.text)

        #3.2: Text content.
        content = self.driver.find_element(u.By.ID, "content")
        print(content.text)

        #Step 4: Verify Login credentials
        #4.1: username
        username = self.driver.find_element(u.By.XPATH, "//em[normalize-space()='tomsmith']")
        print(username.text)
        #4.2: password
        password = self.driver.find_element(u.By.XPATH, "//em[normalize-space()='SuperSecretPassword!']")
        print(password.text)

        #Step 5: Username field
        username_field = self.driver.find_element(u.By.XPATH,  "//input[@id='username']")
        username_field.clear()
        username_field.send_keys(username.text)
        

        #Step 6: Password field
        password_field = self.driver.find_element(u.By.ID, "password")
        password_field.clear()
        password_field.send_keys(password.text)
        

        #Step 7: Login button
        self.driver.find_element(u.By.XPATH, "//button").click()


        #Step 8: Verify we are on Su.ECure Area after successful login
        self.assertIn("The Internet",self.driver.title)
        self.assertIn("/su.ECure", "https://The-internet.herokuapp.com/su.ECure")


        #Step 9: Verify Su.ECure Area elements visible.
        #9.1: Su.ECure Area header
        is_visible = self.driver.find_element(u.By.XPATH, "//h2[normalize-space()='Secure Area']").is_displayed()
        print('Secure Area is visible', is_visible)
        self.assertTrue(is_visible)
        #9.2: Logout buttonSecure Area
        logout_button = self.driver.find_element(u.By.XPATH, "//i[@class='icon-2x icon-signout']").is_displayed()
        print('Log Out button is visible', logout_button)
        self.assertTrue(logout_button)
        #9.3 Logout button performed.
        self.driver.find_element(u.By.XPATH, "//i[@class='icon-2x icon-signout']").click()



        #Step 10: Verify we returned back to Login page
        self.assertIn("The Internet",self.driver.title)
        self.assertIn("/login", self.driver.current_url)


        self.press_esc()










    def tearDown(self):
        self.driver.quit()

    def press_esc(self):
        pass


if __name__ == "__main__":
    u.unittest.main()


