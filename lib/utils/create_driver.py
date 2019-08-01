import pytest
from selenium.webdriver import Chrome,Firefox,Ie

def get_driver_instance():
    browser_type=pytest.config.option.browser.lower()
    os_name = pytest.config.option.system.lower()
    url_info = pytest.config.option.url.lower()

    if os_name=='windows':
        if browser_type=='chrome':
            driver=Chrome('./browser_servers/chromedriver.exe')
        elif browser_type=='firefox':
            driver=Firefox('./browser_servers/geckodriver.exe')
        elif browser_type=='Ie':
            driver=Ie('./browser_servers/iedriver.exe')
    driver.maximize_window()
    driver.implicitly_wait(30)
    if url_info=='test':
        driver.get('http://localhost')
    elif url_info=='prod':
        driver.get('https://demo.actitime.com')
    return driver