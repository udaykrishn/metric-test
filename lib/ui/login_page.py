from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Login_Page:
    def __init__(self,driver):
        self.driver=driver
    def wait_for_login_page_to_load(self):
        waits=WebDriverWait(self.driver,30)
        waits.until(expected_conditions.visibility_of(self.get_username_textbox()))
        waits.until(expected_conditions.visibility_of(self.get_password_textbox()))

    def get_username_textbox(self):
        try:
            return self.driver.find_element_by_name('username')
        except:
            return None

    def get_password_textbox(self):
        try:
            return self.driver.find_element_by_name('pwd')
        except:
            return None

    def get_login_button(self):
        try:
            return self.driver.find_element_by_id('loginButton')
        except:
            return None

    def get_login_error_msg(self):
        try:
            return self.driver.find_element_by_xpath("//span[text()='Username or Password is invalid. Please try again.']")
        except:
            return None
        