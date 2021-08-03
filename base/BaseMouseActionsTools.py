from base.BaseDriverTools import GreaterDriver
from selenium.webdriver.common.action_chains import ActionChains


class MouseActionsTools(GreaterDriver):
    def __init__(self, browser, driver_path, **kwargs):
        super(MouseActionsTools, self).__init__(driver_path=driver_path, browser=browser, **kwargs)
        self.mouse_driver = ActionChains(self.driver)

    def mouse_click(self, event='double', on_element=None):
        """
        function：鼠标基本操作
        :param event:
                {double：左键双击，
                context：右键单击，
                default：左键单击,
                select: 左键点击，不放开
        }
        :param on_element: 操作的元素对象
        :return:
        """
        if event == 'double':
            self.mouse_driver.double_click(on_element).perform()
        elif event == 'context':
            self.mouse_driver.context_click(on_element).perform()
        elif event == 'select':
            self.mouse_driver.click_and_hold(on_element).perform()
        else:
            self.mouse_driver.click(on_element).perform()

    def mouse_move_to(self, *args, event='to_element'):
        """
        function: 鼠标拖拽元素
        :param event:{
            to_element: 鼠标悬停在指定元素,
            element_to_position: 拖拽元素到指定位置,
            element_to_element: 拖拽元素到指定元素
        }
        :param args:{
            if to_element: element,
            if element_to_position: source_element, xoffset, yoffset,
            if element_to_element: source_element, target_element
        }
        :return:
        """
        if event == 'to_element':
            self.mouse_driver.move_to_element(*args).perform()
        elif event == 'element_to_position':
            self.mouse_driver.drag_and_drop_by_offset(*args).perform()
        elif event == 'element_to_element':
            self.mouse_driver.drag_and_drop(*args).perform()

    def keyboard_event(self, position, *args):
        """
        function: 键盘基本操作
        :param position: element
        :param args:
            {
            Keys.BACK_SPACE: 删除键（BackSpace）
            Keys.SPACE: 空格键(Space)
            Keys.TAB: 制表键(Tab)
            Keys.ESCAPE: 回退键（Esc）
            Keys.ENTER: 回车键（Enter）
            Keys.CONTROL,'a': 全选（Ctrl+A）
            Keys.CONTROL,'c': 复制（Ctrl+C）
            Keys.CONTROL,'x': 剪切（Ctrl+X）
            Keys.CONTROL,'v': 粘贴（Ctrl+V）
            Keys.F1: 键盘F1
            ……
            Keys.F12: 键盘F12
        }
        :return:
        """
        self.driver.find_element(position).send_keys(*args)


if __name__ == '__main__':
    pass
