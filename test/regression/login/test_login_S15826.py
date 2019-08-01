import unittest
import json
from lib.ui.home_page import HomePage
from lib.ui.login_page import Login_Page
from lib.utils import create_driver

class TestLoginS15826(unittest.TestCase):
    def setUp(self):
        self.driver=create_driver.get_driver_instance()
        self.login=Login_Page(self.driver)
        self.home=HomePage(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_valid_login_TC123567(self):
        data=json.load(open('./test/regression/login/S15826.json'))
        #Go to login page
        self.login.wait_for_login_page_to_load()
        #Enter UN
        self.login.get_username_textbox().send_keys(data['TC123567']['username'])
        #Enter password
        self.login.get_password_textbox().send_keys(data['TC123567']['pwd'])
        #Click on login button
        self.login.get_login_button().click()
        #Get title of the webpage and verify
        self.home.wait_for_home_page_to_load()
        actual_title=self.driver.title
        print('actual title',actual_title)
        assert actual_title==data['TC123567']['title'],'Failed due to title mismatched'
        self.home.get_logout_button().click()
        self.login.wait_for_login_page_to_load()