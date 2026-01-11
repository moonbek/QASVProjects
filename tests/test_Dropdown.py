
"""
Test: Dropdown CSS_SELECTOR (https://The-internet.herokuapp.com/)

Goal:
Open The Dropdown example page, SELECTOR Option 1 and Option 2, and verify that The dropdown works.

Key skills practiced:
- Navigation using CSS_SELECTOR
- u.WDW (explicit waits)
- Working with <SELECTOR> and <option> elements
- Browser navigation: refresh() and back()
"""
from Selenium_Training_Internet.tests import utils as u


class DragDown(u.unittest.TestCase):
    def setUp(self):
        self.driver = u.webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = u.WDW(self.driver, 10)
        self.actions = u.ActionChains(self.driver)

    def test_drop_down(self):

        #Step 1: Open main page
        self.driver.get(u.BASE_URL)
        self.wait.until(u.EC.title_contains("The Internet"))
        

        #Step 2: Click on "Drop Down" link
        self.wait.until(u.EC.element_to_be_clickable((u.By.CSS_SELECTOR, "#content a[href='/dropdown']"))).click()
        

        #Step 3: Wait until dropdown field is visible and clickable
        self.wait.until(u.EC.element_to_be_clickable((u.By.ID, "dropdown"))).click()
        
        #Step 3.1: Cuoose option 1 from dropdown
        self.wait.until(u.EC.visibility_of_element_located((u.By.CSS_SELECTOR, "#dropdown option[value='1']"))).click()
        
        #Step 3.2: Make sure option 1 is selu.ECted
        self.wait.until(u.EC.element_to_be_clickable((u.By.ID, "dropdown"))).click()
        
        self.wait.until(u.EC.element_to_be_clickable((u.By.ID, "dropdown"))).click()
        
        #Step 3.3: Cuoose option 2 from dropdown
        self.wait.until(u.EC.visibility_of_element_located((u.By.CSS_SELECTOR, "#dropdown option[value='2']"))).click()
        
        #Step 3.4: Make sure option 2 is selu.ECted
        self.wait.until(u.EC.element_to_be_clickable((u.By.ID, "dropdown"))).click()
        
        self.wait.until(u.EC.visibility_of_element_located((u.By.ID, "dropdown")))
        print("Drop down field is visible and clickable")
        

        #Step 4: Return to  refresh and previous page
        self.driver.refresh()
        
        self.driver.back()
        


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    u.unittest.main()







