from .base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    MESSAGE = (By.TAG_NAME, "h1")

    def get_message(self):
        return super().get_message(self.MESSAGE)