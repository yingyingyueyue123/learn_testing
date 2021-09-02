from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _url = ""

    def __init__(self, driver_base=None):
        if driver_base is None:
            option = Options()
            option.debugger_address = "localhost:9222"
            self.driver = webdriver.Chrome(options=option)
        else:
            self.driver: WebDriver = driver_base

        if self._url != "":
            self.driver.get(self._url)
        self.driver.implicitly_wait(5)

    def base_quit(self):
        return self.driver.quit()
