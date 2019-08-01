def pytest_addoption(parser):
    parser.addoption('--browser', default="chrome")
    parser.addoption('--system', default="windows")
    parser.addoption('--url', default="test")