import time
import logging
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class GreaterDriver(object):
    def __init__(self, browser, driver_path, **kwargs):
        """
        function: 实例化浏览器对象
        :param browser: Tuple(浏览器类型，浏览器驱动地址)
        :param driver_path: 浏览器驱动路径
        :return: 浏览器页面对象
        """
        if browser == 'chrome':
            self.driver = webdriver.Chrome(executable_path=driver_path, **kwargs)
        elif browser == 'firefox':
            self.driver = webdriver.Firefox(executable_path=driver_path, **kwargs)
        elif browser == 'edge':
            self.driver = webdriver.Ie(executable_path=driver_path, **kwargs)
        else:
            print(f'启动浏览器有误，当前启动是：【{browser}】，驱动路径：{driver_path}')


class DriverTools(GreaterDriver):
    """
    class：webdriver的基本操作类
    function：{
        open_page：打开页面
        element_locator：查找元素
        element_operation: 操作元素
        quit_browser：关闭页面 or 退出浏览器
        implicit_wait：隐式等待
        show_wait：显示等待
        get_cookie：获取cookie
    }
    """

    def open_page(self, page_url):
        """
        函数功能：打开浏览器页面
        :param page_url: 打开页面的地址
        :return: 返回页面对象
        """
        return self.driver.get(page_url)

    def element_locator(self, position, is_elements=False):
        """
        函数功能：定位元素
        :param position: Tuple，（BY.ID，value）第一个参数是定位的方式；第二个参数是定位的值
        :param is_elements: 是否定位多个元素
        :return: 返回元素对象
        """
        try:
            if is_elements is False:
                element = self.driver.find_element(*position)
                return element
            else:
                elements = self.driver.find_elements(*position)
                return elements

        except NoSuchElementException as e:
            logging.error(f'找不到元素{e}，查找元素方法：{position[0]},值：{position[1]}')

    def element_operation(self, position, event='click', value=None, attribute_name=None):
        """
        函数功能：给定位到的元素传值
        :param attribute_name: 元素class属性名
        :param event: 元素事件
                {click: 点击，默认，
                 input：传值，
                 text：文本，
                 attribute：属性值
                 }
        :param position: Tuple，第一个参数是定位的方式；第二个参数是定位的值
        :param value: str，传输入的值
        :return:
        """
        element = self.element_locator(position)
        if event == 'click':
            element.click()
            logging.info(f'点击元素：{element.text}')
        elif event == 'input':
            element.send_keys(value)
            logging.info(f'输入值：{value}')
        elif event == 'text':
            logging.info(f'获取元素文本值{element.text}')
            return element.text()
        elif event == 'attribute':
            try:
                return element.get_attribute(attribute_name)
            except Exception as e:
                logging.error(f'获取元素属性值失败：{attribute_name}')

    @staticmethod
    def is_element_displayed(element):
        """
        function: 元素是否存在
        :param element:
        :return:
        """
        return element.is_displayed()

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        logging.info('等待时间：%d秒' % seconds)

    def quit_browser(self, action=True):
        """
        函数功能：关闭窗口or退出浏览器
        :param action: {
                    True:退出浏览器，
                    False：关闭当前窗口，如果它是当前打开的最后一个窗口，则退出浏览器
                }
        :return:
        """
        if action:
            self.driver.quit()
            logging.info('关闭当前窗口')
        else:
            self.driver.close()
            logging.info('浏览器关闭')

    def implicit_wait(self, seconds):
        """
        函数功能：隐式等待
        :param seconds: int，等待的秒数
        :return:
        """
        self.driver.implicitly_wait(seconds)
        logging.info(f'等待时间:{seconds}秒')

    def show_wait(self, timeout, poll_frequency=0.5, *args):
        """
        函数功能：显示等待
        :param timeout:超时前的秒数
        :param poll_frequency:查找元素的间隔时间，默认情况下是0.5秒
        :param args:定位元素的方法（BY.ID, value）
        :return:返回元素对象
        """
        element = WebDriverWait(self.driver, timeout, poll_frequency) \
            .until(ec.presence_of_element_located(*args))
        return element

    def get_cookie(self):
        """
        function:获取cookie
        :return:
        """
        return self.driver.get_cookies()

    def add_cookie(self):
        """
        function: 添加cookie
        :return:
        """
        self.driver.add_cookie(self.get_cookie())

    def switch_frame(self, reference, action=None):
        """
        function：切换iframe 或 frame
        :param reference: 可以传入frame的id、name、index以及selenium的WebElement对象
        :param action: 切换的动作，{
                            back：返回上层，多层嵌套，
                            default：返回主文档
                            }
        :return:
        """
        if action is None:
            return self.driver.switch_to.frame(reference)
        elif action == 'back':
            return self.driver.switch_to.parent_frame()
        elif action == 'default':
            return self.driver.switch_to.default_content()


if __name__ == '__main__':
    path = '../driver/chrome/chromedriver.exe'
    dri = GreaterDriver(browser='chrome', driver_path=path)
