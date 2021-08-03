from selenium import webdriver
from base.BaseDriverTools import DriverTools as Dt
from base.BaseMouseActionsTools import MouseActionsTools as Mt
from base.BaseWindowsOperationTools import WindowsOperationTools as Wt


class MyDriver(Dt, Wt, Mt):
    def __init__(self, browser, driver_path, driver_info=True, option_list=None):
        if driver_info:
            super(MyDriver, self).__init__(driver_path=driver_path, browser=browser)
        else:
            if browser == 'chrome':
                self.option = MyDriver.driver_info_chrome(option_list)
            # firefox 个性化定制与chrome不一样，需要另外写方法定制
            elif browser == 'firefox':
                self.option = MyDriver.driver_info_firefox(option_list)
            elif browser == 'edge':
                self.option = MyDriver.driver_info_ie(option_list)
            super(MyDriver, self).__init__(driver_path=driver_path, browser=browser, chrome_options=self.option)

    @staticmethod
    def driver_info_chrome(option_list):
        chrome_option = webdriver.ChromeOptions()
        for param in option_list:
            if isinstance(param, tuple):
                chrome_option.add_experimental_option(*param)
            elif isinstance(param, str):
                chrome_option.add_argument(param)
        return chrome_option

    @staticmethod
    def driver_info_firefox(option_list):
        firefox_option = webdriver.FirefoxOptions()
        for param in option_list:
            if isinstance(param, tuple):
                firefox_option.set_capability(*param)
            elif isinstance(param, str):
                firefox_option.add_argument(param)
        return firefox_option

    @staticmethod
    def driver_info_ie(option_list):
        ie_option = webdriver.ChromeOptions()
        for param in option_list:
            if isinstance(param, tuple):
                ie_option.add_experimental_option(*param)
            elif isinstance(param, str):
                ie_option.add_argument(param)
        return ie_option


if __name__ == '__main__':
    my_list = [('useAutomationExtension', False), ("excludeSwitches", ['enable-automation']),
               '--start-maximized', 'blink-settings=imagesEnabled=false']
    path = '../driver/chrome/chromedriver.exe'
    t = MyDriver('chrome', path, driver_info=False, option_list=my_list)
    t.open_page('https://www.baidu.com')
    print(t.driver.page_source)
