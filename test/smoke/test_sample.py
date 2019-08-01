import unittest
from lib.ui.login_page import Login_Page
from lib.utils import create_driver

class TestComponents(unittest.TestCase):

    def setUp(self):
        self.driver=create_driver.get_driver_instance()
        self.login=Login_Page(self.driver)

    def tearDown(self):
        self.driver.close()

    def test_framework_components(self):
        self.login.wait_for_login_page_to_load()
        actual_title=self.driver.title
        expected_title='actiTIME - Login'
        assert actual_title==expected_title,'Title not matching'