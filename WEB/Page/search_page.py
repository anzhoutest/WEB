from WEB.Base.Base import Base
from WEB import Page

class home_page(Base):
    #实例化driver
    def __init__(self,driver):
        Base.__init__(self,driver)
    #点击新闻
    def click_niew(self):
        self.click_element(Page.niew_el)
    #点击网页
    def click_webpage(self):
        self.click_element(Page.webpage_el)
    #点击微信
    def click_wechat(self):
        self.click_element(Page.wechat_el)
    #点击知乎
    def click_zhihu(self):
        self.click_element(Page.zhihu_el)
    #点击图片
    def click_picture(self):
        self.click_element(Page.picture_el)
    #点击视频
    def click_vedio(self):
        self.click_element(Page.vedio_el)
    #点击明医
    def click_mingyi(self):
        self.click_element(Page.mingyi_el)
    #点击英文
    def click_english(self):
        self.click_element(Page.english_el)
    #点击问问
    def click_ask(self):
        self.click_element(Page.ask_el)
    #点击学术
    def click_xueshu(self):
        self.click_element(Page.xueshu_el)
    #点击更多
    def click_more(self):
        self.click_element(Page.more_el)
    #点击输入框
    def click_search(self,text):
        self.input_text(Page.search_el,text)