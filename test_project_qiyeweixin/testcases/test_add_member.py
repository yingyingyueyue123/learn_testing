from test_project_qiyeweixin.page.add_member_page import AddMember
from test_project_qiyeweixin.page.main_page import MainPage


class TestAddMember:
    def setup_class(self):
        self.main = MainPage()

    def teardown_class(self):
        self.main.base_quit()

    def test_add_member(self):
        result = self.main.go_to_add_member().add_member("13199991111").get_member_list()
        assert "皮城女警" in result

    def test_add_member_fail(self):
        self.main.go_to_add_member().add_member("2222%%%")
        result = AddMember(self.main.driver).get_phone_error_message()
        assert "请填写正确的手机号码" == result

    def test_contact_add_member(self):
        self.main.go_to_contact().go_to_add_member().add_member()