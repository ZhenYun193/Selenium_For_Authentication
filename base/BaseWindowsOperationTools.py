import os.path
import time
import logging
from base.BaseDriverTools import GreaterDriver


class WindowsOperationTools(GreaterDriver):
    def get_windows_title(self):
        """
        function: 获取窗口标题
        :return:
        """
        return self.driver.title

    def set_windows_size(self, size='max', window_handle='current', width=None, height=None):
        """
        function: 设置浏览器窗口大小
        :param size: 设置窗口的大小，默认最大
        :param width: 宽度
        :param height: 高度
        :param window_handle: 指定窗口，默认当前窗口
        :return:
        """
        if size == 'set':
            self.driver.set_window_size(width, height, window_handle)
            logging.info(f'设置窗口尺寸，宽：{width}，长：{height}，窗口句柄：{window_handle}')
        elif size == 'max':
            self.driver.maximize_window()
        elif size == 'min':
            self.driver.minimize_window()

    def back_and_forward(self, event='back'):
        """
        function: 窗口后退（back）和前进（forward）
        :param event: 默认后退
        :return:
        """
        if event == 'back':
            self.driver.back()
            logging.info('页面前进')
        else:
            self.driver.forward()
            logging.info('页面后退')

    def windows_refresh(self):
        """
        function: 刷新窗口
        :return:
        """
        self.driver.refresh()

    def switch_windows(self, handle):
        """
        function：切换窗口
        :param handle: 窗口的句柄
        :return:
        """
        return self.driver.switch_to.window(handle)

    def get_window_handle(self, window=True):
        """
        function: 获取窗口句柄
        window: {
                True：当前窗口句柄，默认当前窗口
                False：所有窗口句柄
            }
        :return:
        """
        if window:
            return self.driver.current_window_handle
        else:
            return self.driver.window_handles

    def switch_alert(self):
        pass

    def get_img(self, path):
        """
        function: 截图
        :return:
        """
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        screen_name = os.path.join(path, '%s.png' % rq)
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logging.info(f'截图并保存到：{path}')
        except NameError as e:
            logging.error(f'截图失败：{e}')
            self.get_img(path)


if __name__ == '__main__':
    pass
