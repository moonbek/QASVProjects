
"""
Test: Drag and Drop (The-internet.herokuapp.com)

Goal:
Open The Drag and Drop example page, drag Column A to Column B, Then drag it back.

Key skills practiced:
- Navigation using CSS selu.ECtors
- u.WDW (explicit waits)
- ActionChains drag_and_drop()
"""

from Selenium_Training_Internet.tests import utils as u



class DragAndDrop(u.unittest.TestCase):
    def setUp(self):
        """Set up Chrome driver, maximize window, and create wait/actions helpers."""
        self.driver = u.webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = u.WDW(self.driver, 10)
        self.actions = u.ActionChains(self.driver)




    def test_drag_and_drop(self):
        """Drag column A onto column B and Then drag it back."""

        # Step 1: Open main page
        self.driver.get(u.BASE_URL)
        self.wait.until(u.EC.title_contains("The Internet"))

        # Step 2: Click on "Drag and Drop" link
        self.wait.until(u.EC.element_to_be_clickable((u.By.CSS_SELECTOR, "#content a[href='/drag_and_drop']"))).click()
        

        # Step 3: Wait until The draggable elements are visible
        self.wait.until(u.EC.visibility_of_element_located((u.By.ID, "column-a")))

        # Step 4: Locate source and target elements
        source = self.driver.find_element(u.By.ID, "column-a")
        target = self.driver.find_element(u.By.ID, "column-b")
        

        # Step 5: Perform drag and drop from A to B
        self.actions.drag_and_drop(source, target).perform()
        


        # Step 6: Perform drag and drop from B to A
        self.actions.drag_and_drop(target, source).perform()
        

        # Step 7: Return to previous page
        self.driver.back()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    u.unittest.main()






