from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def type(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)
    

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    #def get_text(self, locator):
      #  element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
       # return element.text

    def get_message(self, locator):
        return self.driver.find_element(*locator).text

