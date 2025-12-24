

#Cross-browser UnitTest automation (Chrome, Firefox) with Selenium + WebDriver Manager.
import unittest


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager







class MultiBrowserTest(unittest.TestCase):
    def test_firefox_example(self):
        print("Hello Firefox unittest!")

        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.maximize_window()

        driver.get("http://qasvus.wordpress.com/")
        print("FIREFOX TITLE:", driver.title)

        self.assertIn("California Real Estate", driver.title)

        driver.quit()

    def test_chrome_example(self):
        print("Hello Chrome unittest!")

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()

        driver.get("http://qasvus.wordpress.com/")
        print("CHROME TITLE:", driver.title)

        self.assertIn("California Real Estate", driver.title)

        driver.quit()

    #For some reasons Edge temporarily disabled
    # def test_edge_example(self):
    #     print("Hello Edge unittest!")
    #
    #
    #     driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    #     driver.maximize_window()
    #
    #
    #
    #
    #     driver.get("http://qasvus.wordpress.com/")
    #     print("EDGE TITLE:", driver.title)
    #
    #     self.assertIn("California Real Estate", driver.title, "Wrong title on main page")
    #
    #     driver.quit()




if __name__ == "__main__":
    unittest.main()