from time import sleep
from infofile.BroswerData import *
from base.MyDriver import MyDriver


class Login(MyDriver):
    def __init__(self, path, browser='chrome', **kwargs):
        super(Login, self).__init__(driver_path=path, browser=browser, **kwargs)

    def login(self, login_data_list):
        # 点击头像
        self.element_operation(login_data_list['head_portrait'])
        # 选择QQ登录
        sleep(2)
        self.element_operation(login_data_list['login_type'])
        # 切换到登陆弹窗的frame
        sleep(2)
        self.switch_frame(login_data_list['iframe']['iframe_01'])
        self.switch_frame(login_data_list['iframe']['iframe_02'])
        # 点击【账号密码登录】
        sleep(2)
        self.element_operation(login_data_list['login_method'])
        # 输入账号
        self.element_operation(login_data_list['user_mgs']['username'][0],
                               value=login_data_list['user_mgs']['username'][1], event='input')
        # 输入密码
        self.element_operation(login_data_list['user_mgs']['password'][0],
                               value=login_data_list['user_mgs']['password'][1], event='input')
        # 点击【登录】
        self.element_operation(login_data_list['login_btn'])
        return self.driver

    def logout(self, logout_data_list):
        # 鼠标移动到头像
        head_portrait = self.element_locator(logout_data_list['head_portrait'])
        self.mouse_move_to(head_portrait)
        # 点击【退出】
        self.element_operation(logout_data_list['login_out'])


if __name__ == '__main__':
    lo = Login(browser_data['driver_path'], driver_info=False, option_list=browser_data['info'])
    lo.open_page(browser_data['page_url_file'])
    lo.login(login_data_list=login_info_list)
    sleep(3)
    lo.logout(logout_data_list=logout_info_list)
    sleep(5)
    lo.quit_browser()



