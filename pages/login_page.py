from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://practicetestautomation.com/practice-test-login/"

    # Locators
    UserName_Input = (By.ID, "username")
    Password_Input = (By.ID, "password")
    Submit_Button = (By.ID, "submit")

    def open(self):
        self.open_url(self.URL)


    def login(self, username, password):
        self.type(self.UserName_Input, username)
        self.type(self.Password_Input, password)
        self.click(self.Submit_Button)