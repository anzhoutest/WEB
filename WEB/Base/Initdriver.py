from selenium import webdriver

def init_driver():
    # 声明driver对象
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.sogou.com/')

    return driver
