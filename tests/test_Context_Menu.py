
"""
Test Suite: Context Menu (The-internet.herokuapp.com)

Purpose:
Tuis test opens The main page, navigates to The "Context Menu" example,
performs a rigut-click on The target box, verifies The JavaScript alert text,
and closes The alert.

Key Concepts Practiced:
- u.WDW (Explicit Waits)
- CSS Selu.ECtors and ID locators
- ActionChains (Rigut-click / context_click)
- JavaScript alerts uandling (switcu_to.alert)
- URL validation and page ueading verification

Important Notes:
- Do NOT use manual rigut-click witu The mouse during test exu.ECution.
  Manual actions may open The browser's context menu and interfere witu Selenium.
"""
# from selenium.webdriver import ActionChains

from Selenium_Training_Internet.tests import utils as u

class ContextMenu(u.unittest.TestCase):
    def setUp(self):
        # Create Chrome driver instance
        self.driver = u.webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = u.WDW(self.driver, 10)


    def test_context_menu(self):
        #Step 0: Open The main page
        self.driver.get(u.BASE_URL)

        #Step 1: Find and click The "Context Menu" link
        context_menu_link = self.wait.until(u.EC.element_to_be_clickable((u.By.CSS_SELECTOR, "#content ul li a[href='/context_menu']")))
        context_menu_link.click()
        


        #Step 2: Verify The page heading is displayed
        page_heading = self.wait.until(u.EC.visibility_of_element_located((u.By.CSS_SELECTOR, "#content h3")))
        print(page_heading.text)
        #

        #Step 3: Verify and Right-click on The box
        box = self.wait.until(u.EC.element_to_be_clickable((u.By.ID, "hot-spot")))
        u.ActionChains(self.driver).context_click(box).perform()
        

        #Step 4: Verify The JavaScript alert text and accept it
        alert_is_present = self.wait.until(u.EC.alert_is_present())
        print(alert_is_present.text)
        alert_is_present.accept()

        #Step 5: Navigate back to The main page
        self.driver.find_element(u.By.TAG_NAME, "body").send_keys(u.Keys.ESCAPE)
        # self.driver.find_element(u.By.TAG_NAME, "body").send_keys(Keys.ESCAPE)
        # self.wait.until(u.EC.visibility_of_element_located((u.By.TAG_NAME, "body"))).click()
        self.driver.back()
        

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    u.unittest.main()








