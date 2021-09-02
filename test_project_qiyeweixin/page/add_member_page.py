from selenium.webdriver.common.by import By
from test_project_qiyeweixin.page.base_page import BasePage
from test_project_qiyeweixin.page.contact_page import ContactPage


class AddMember(BasePage):
    def add_member(self, phone):
        self.driver.find_element_by_id("username").send_keys("皮城女警")
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys("1111")
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        return ContactPage(self.driver)

    def get_phone_error_message(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".ww_inputWithTips_WithErr .ww_inputWithTips_tips").text
