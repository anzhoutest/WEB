from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium import webdriver

class Base:
    def __init__(self,driver):
        self.driver = driver

    def find_element_obj(self,loc,timeout=10,poll=0.5):
        '''
        :param loc:元祖（BY.ID,ID属性值）
        :param timeout:
        :param poll:
        :return:一个元素对象
        '''
        return WebDriverWait(self.driver,timeout,poll).\
            until(lambda x: x.find_element(*loc))


    def find_elements_obj(self,loc,timeout=10,poll=0.5):
        '''
        :param loc:元祖（BY.ID,ID属性值）
        :param timeout:
        :param poll:
        :return:一组元素对象
         '''
        return WebDriverWait(self.driver,timeout,poll).\
            until(lambda x: x.find_elements(*loc))

    def if_exist(self,loc):
        '''
        :param loc:
        :return: 布尔值
        '''
        try:
            self.find_element_obj(loc)
            return True
        except Exception as e:
            return False

    # 点击元素
    def click_element(self,loc):
        self.find_element_obj(loc).click()


    def input_text(self,loc,text):
        '''
        :param loc:
        :param text: 需要输入的文本内容
        :return:
        '''
        ele = self.find_element_obj(loc)
        ele.clear()
        ele.send_keys(text)


    def select_el(self,loc,n):
        '''
        :param loc:
        :param n:
        :return: 定位下拉列表框
        '''
        se_el = self.find_element_obj(loc)
        sele_obj = Select.select_by_index(n)
