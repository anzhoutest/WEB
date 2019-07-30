import sys,os
sys.path.append(os.getcwd())

from WEB.Page.Page import Page_Obj
from WEB.Base.Initdriver import init_driver
from WEB.Base.Read_Data import read_yaml
import pytest,allure,time

def read_data():
    list_data = []
    data = read_yaml('serch').get('Serch_Data')
    for i in data.keys():
        list_data.append((data.get(i).get('test'),data.get(i).get('expect')))

    return list_data

class Test_home_page:
    def setup_class(self):
        self.driver = init_driver()
        self.home_page_test = Page_Obj(self.driver).return_search_page()

    def teardown_class(self):
        self.driver.quit()

    # @pytest.allure.severity(pytest.allure.severity_level.)
    @pytest.mark.parametrize('test_num,expect',read_data())
    def test_click_search(self,test_num,expect):
        self.home_page_test.click_search(test_num)
        assert test_num == expect
        time.sleep(2)



