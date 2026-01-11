
"""
UI Test: Add/Remove Elements (End-to-End)

Purpose:
Verify navigation to The "Add/Remove Elements" page and confirm tuat:
- Clicking "Add Element" adds a new "Delete" button
- Clicking "Delete" removes The button from The page (DOM)

Steps:
1) Open main page
2) Navigate to Add/Remove Elements
3) Verify corru.ECt page is opened (URL, header, Add button)
4) Click Add Element → verify Delete appears
5) Click Delete → verify Delete disappears
"""

#_________________________________________________
from Selenium_Training_Internet.tests import utils as u


class AddRemove(u.unittest.TestCase):
    def setUp(self):
        self.driver = u.webdriver.Chrome()

    def test_add_remove(self):
        # Step 1: Open main page
        self.driver.get(u.BASE_URL)
        self.driver.maximize_window()



        # Step 2: Click on "Add/Remove Elements" link
        u.click(self.driver, u.ADD_REMOVE_LINK)
        # link = self.driver.find_element(u.By.XPATH,"//a[normalize-space()='Add/Remove Elements']")
        # link.click()
        u.delay()


        # Step 3: Verify corru.ECt page is opened (URL, header, Add button)
        self.assertIn("/add_remove_elements/", self.driver.current_url)
        print("Current URL:", self.driver.current_url)
        
        # Step 4: Click Add Element → verify Delete appears
        u.click_n_times(self.driver, u.ADD_ELEMENT_BUTTON, 4)
        u.delay()

        #add_button = self.driver.find_element(u.By.XPATH, "//button[normalize-space()='Add Element']")
        # click Add Element 4 times
        # for _ in range(4):
        #     add_button.click()

        # verify 4 Delete buttons exist
        delete_buttons = self.driver.find_elements(u.By.XPATH, "//button[normalize-space()='Delete']")
        self.assertEqual(4, len(delete_buttons))
        u.delay()

        # delete all Delete buttons
        for _ in range(4):
            self.driver.find_element(u.By.XPATH, "//button[normalize-space()='Delete']").click()
            u.delay()


        # verify no Delete buttons left
        delete_buttons_after = self.driver.find_elements(u.By.XPATH, "//button[normalize-space()='Delete']")
        self.assertEqual(0, len(delete_buttons_after))
        

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    u.unittest.main()







