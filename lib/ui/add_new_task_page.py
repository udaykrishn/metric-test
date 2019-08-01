from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select


class AddNewTaskPage:
    def __init__(self,driver):
        self.driver=driver

    def wait_for_add_new_task_page(self):
        wait=WebDriverWait(self.driver,30)
        wait.until(expected_conditions.visibility_of(self.get_create_task_button()))

    def select_customer(self, name='-- new customer --'):
        status=False
        ddl=self.driver.find_element_by_name('customerId')
        sct=Select(ddl)
        all_options=sct.options
        for option in all_options:
            text=option.text
            print(text)
            if text==name:
                sct.select_by_visible_text(name)
                status=True
                break
        if status==False:
            sct.select_by_visible_text('-- new customer --')

    def select_project(self,name='-- new project --'):
        status=False
        ddl=self.driver.find_element_by_name('projectId')
        sct=Select(ddl)
        all_options=sct.options
        for option in all_options:
            text=option.text
            if text==name:
                sct.select_by_visible_text(name)
                status=True
                break
        if status==False:
            sct.select_by_visible_text('-- new project --')

    def get_customername_textbox(self):
        try:
            return self.driver.find_element_by_name('customerName')
        except:
            return None

    def get_projectname_textbox(self):
        try:
            return self.driver.find_element_by_name('projectName')
        except:
            return None

    def get_task_first_textbox(self):
        try:
            return self.driver.find_element_by_name('task[0].name')
        except:
            return None

    def get_create_task_button(self):
        try:
            return self.driver.find_element_by_xpath("//input[@value='Create Tasks']")
        except:
            return None