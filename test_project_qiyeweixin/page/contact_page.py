from selenium.webdriver.common.by import By
from test_project_qiyeweixin.page.base_page import BasePage


class ContactPage(BasePage):
    def go_to_add_member(self):
        from test_project_qiyeweixin.page.add_member_page import AddMember
        return AddMember(self.driver)

    def get_member_list(self):
        name_list = self.driver.find_element(By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
        list1 = []
        for name in name_list:
            list1.append(name.text)
        return list1
