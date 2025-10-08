from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("jdsh","dhuwhh")

    error_msg =login_page.get_error_message((By.ID,"error"))# Replace 'ID' with the appropriate locator strategy
    print("Error message text:", error_msg)
    assert "Your username is invalid!" in error_msg