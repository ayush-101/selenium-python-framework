from pages.login_page import LoginPage  # Adjust the import path as needed
from pages.home_page import HomePage  # Add this import for HomePage

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("student", "Password123")

    home_page = HomePage(driver)
    assert "Logged In Successfully" in home_page.get_message()

    