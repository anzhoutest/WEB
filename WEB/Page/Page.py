from WEB.Page.search_page import home_page

class Page_Obj():
    def __init__(self,driver):
        self.driver = driver
    def return_search_page(self):
        return home_page(self.driver)


