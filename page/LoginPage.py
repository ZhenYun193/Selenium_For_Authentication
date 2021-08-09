from time import sleep
from config.ElementDate import *
from base.MyDriver import MyDriver


class LoginElement:
    # 头像
    head_portrait = login_info_list['head_portrait']
    # 选择登录方式：QQ or WX , 选择QQ
    login_for_qq = login_info_list['login_type']
    # 切入登录弹窗iframe
    login_iframe_01 = login_info_list['iframe']['iframe_01']
    login_iframe_02 = login_info_list['iframe']['iframe_02']
    # 选择登录方式：账号密码 or 扫码登录，选择账号密码
    login_by_username = login_info_list['login_method']
    # 用户名
    username = {'position': login_info_list['user_mgs']['username'][0],
                'value': login_info_list['user_mgs']['username'][1], 'event': 'input'}
    # 密码
    password = {'position': login_info_list['user_mgs']['password'][0],
                'value': login_info_list['user_mgs']['password'][1], 'event': 'input'}
    # 登录按钮
    login_btn = login_info_list['login_btn']


class LogoutElement:
    # 头像
    head_portrait = logout_info_list['head_portrait']
    # 退等按钮
    logout_btn = logout_info_list['login_out']


class LoginProcess(MyDriver):

    def __init__(self, path, browser='chrome', **kwargs):

        super(LoginProcess, self).__init__(driver_path=path, browser=browser, **kwargs)

    def login(self):
        # 点击头像
        self.element_operation(LoginElement.head_portrait)
        # 选择QQ登录
        sleep(2)
        self.element_operation(LoginElement.login_for_qq)
        # 切换到登陆弹窗的frame
        sleep(2)
        self.switch_frame(LoginElement.login_iframe_01)
        self.switch_frame(LoginElement.login_iframe_02)
        # 点击【账号密码登录】
        sleep(2)
        self.element_operation(LoginElement.login_by_username)
        # 输入账号
        self.element_operation(**LoginElement.username)
        # 输入密码
        self.element_operation(**LoginElement.password)
        # 点击【登录】
        self.element_operation(LoginElement.login_btn)
        return self.driver

    def logout(self):
        # 鼠标移动到头像
        head_portrait = self.element_locator(LogoutElement.head_portrait)
        self.mouse_move_to(head_portrait)
        # 点击【退出】
        self.element_operation(LogoutElement.logout_btn)


if __name__ == '__main__':
    lo = LoginProcess(browser_data['driver_path'], driver_info=False, option_list=browser_data['info'])
    lo.open_page(browser_data['page_url_file'])
    lo.login()
    sleep(3)
    lo.logout()
    sleep(5)
    lo.quit_browser()
