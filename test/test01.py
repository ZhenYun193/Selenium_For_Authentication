# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from base.BaseMouseActionsTools import MouseActionsTools
# from selenium.webdriver.common.action_chains import ActionChains
#
#
# driver = webdriver.Chrome(r'../driver/chrome/chromedriver.exe')
# driver.get(r'https://www.baidu.com')
# element = driver.find_element(By.XPATH, '//*[@id="mod_player"]')
# print('开始等待')
# time.sleep(2)
# print('等待结束')
# element.click()
# print('开始等待')
# time.sleep(5)

# class Base(object):
#     def __init__(self):
#         print('wo shi class Base')
#
#
# class A(Base):
#     def __init__(self):
#         super().__init__()
#         print('wo shi class A')
#
#
# class B(Base):
#     def __init__(self):
#         super().__init__()
#         print('wo shi class B')
#
#
# class D(Base):
#     def __init__(self):
#         super().__init__()
#         print('wo shi class D')
#
#
# class C(B, D, A):
#     def __init__(self):
#         super().__init__()
#         print('wo shi class c')
#
#
# if __name__ == '__main__':
#     d = C()


# class Electrical(object):
#     def __init__(self, name):
#         self.name = name
#         print('Electrical init')
#
#
# class Phone(Electrical):
#
#     def __init__(self, name, price):
#         Electrical.__init__(self, name)
#         self.price = price
#         print('Phone init')
#
#
# class Computer(Electrical):
#
#     def __init__(self, name, config):
#         Electrical.__init__(self, name)
#         self.config = config
#         print('Computer init')
#
#
# class HuaWei(Phone, Computer):
#
#     def __init__(self, name, price, config):
#         Phone.__init__(self, name, price)
#         Computer.__init__(self, name, config)
#         print('HuaWei init')
#
#
# h = HuaWei('huawei', 100, 'i7')

#
# from infofile.BroswerData import *
# from base.BaseDecoratoToolsr import is_vip


# class MyDecorator:
#     @is_vip(pay_main_view)
#     def pay_video_main_view(self, locator_list, action='buy', method='cash'):
#         if action == 'vip':
#             print(f"开通btn：{locator_list['vip_btn']}")
#         elif action == 'buy':
#             if method == 'diamond':
#                 print(f"开通btn：{locator_list['diamond_btn']}")
#             elif method == 'cash':
#                 print(f"现金btn：{locator_list['cash_btn']}")
#
#     @staticmethod
#     def payed_view(locator_data, pay_method=None):
#         """
#         function: 支付弹窗
#         :return:
#         """
#         if pay_method == 'card':
#             print(locator_data['pay_method'][3])
#             print(locator_data['card_num'][0], locator_data['card_num'][1])
#             print(locator_data['card_pwd'][0], locator_data['card_num'][1])
#         elif pay_method == 'wechat':
#             print(locator_data['pay_method'][2])
#         elif pay_method == 'QQ':
#             print(locator_data['pay_method'][1])
#         else:
#             print(locator_data['pay_method'][0])
#         if pay_method != 'wechat' and pay_method != 'QQ':
#             # 确认支付
#             print(locator_data['payed_btn'])


# if __name__ == '__main__':
#     a = MyDecorator()
#     a.payed_view('card')

from selenium import webdriver
from base.BaseDriverTools import GreaterDriver
import os
import platform
from time import sleep

path = os.path.join(os.path.abspath('..'), 'driver', 'chrome', 'chromedriver.exe')
print(platform.system())


def driver_info_chrome(option_list):
    option = webdriver.ChromeOptions()
    for param in option_list:
        if isinstance(param, tuple):
            option.add_experimental_option(*param)

        elif isinstance(param, str):
            option.add_argument(param)
    return option


class MyDriver(GreaterDriver):
    def __init__(self, driver_path, browser='chrome', driver_info=True, option_list=None):
        self.option = webdriver.ChromeOptions()
        if driver_info:
            super(MyDriver, self).__init__(driver_path=driver_path, browser=browser)
        else:
            if browser == 'chrome':
                option = driver_info_chrome(option_list)
                super(MyDriver, self).__init__(driver_path=driver_path, browser=browser, options=option)


if __name__ == '__main__':
    my_list = ['--start-maximized']
    options = webdriver.ChromeOptions()
    options.binary_location = r'C:\Program Files (x86)\Google\Chrome\Application'
    options.add_experimental_option('debuggerAddress', '127.0.0.1:9853')
    dri_debugger = webdriver.Chrome(executable_path=path, options=options)
    dri_debugger.get('https://login.taobao.com/member/login.jhtml')
    sleep(2)
    dri_debugger.find_element_by_id('fm-login-id').send_keys('13609713162')
    sleep(2)
    dri_debugger.find_element_by_id('fm-login-password').send_keys('zyb19931110')
    sleep(2)
    dri_debugger.find_element_by_xpath('//button[@type="submit"]').click()
