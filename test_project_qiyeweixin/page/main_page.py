from selenium.webdriver.common.by import By
from test_project_qiyeweixin.page.add_member_page import AddMember
from test_project_qiyeweixin.page.base_page import BasePage
from test_project_qiyeweixin.page.contact_page import ContactPage


class MainPage(BasePage):
    _memberAdd_phone = ""
    _url = "https://work.weixin.qq.com/wework_admin/frame#index"

    def go_to_contact(self):
        return ContactPage(self.driver)

    def go_to_add_member(self):
        self.driver.find_element(By.CSS_SELECTOR, "[node-type='addmember']").click()
        return AddMember(self.driver)
