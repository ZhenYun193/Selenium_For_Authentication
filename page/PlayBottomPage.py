from time import sleep
from base.MyDriver import MyDriver
from infofile.BroswerData import *
from base.BaseDecoratoToolsr import *
from selenium.webdriver.common.by import By


class PlayBottomPage(MyDriver):
    def __init__(self, path, browser='chrome', **kwargs):
        super(PlayBottomPage, self).__init__(driver_path=path, browser=browser, **kwargs)

    def login(self, login_data_list):
        # 点击头像
        # self.element_operation(login_data_list['head_portrait'])
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

    def ad_wait_time(self):
        """
        function: 处理广告
        :return:
        """
        sleep(2)
        # 获取广告文案
        ad_text = self.element_operation((By.XPATH, '//txpdiv[contains(text(),"关闭该广告")]'), event='text')
        print(ad_text)
        # 获取广告时间
        ad_time = self.element_operation((By.XPATH, '//txpdiv[@data-role="adplayer-video-countdown"]'), event='text')
        print(ad_time)

    def get_play_status(self):
        """
        function: 获取播放器的播放状态
        :return: 播放按钮对象
        """
        sleep(2)
        # 滑动鼠标，展示播放器工具栏
        player = self.element_locator(player_info['player'])
        self.mouse_move_to(player)
        # 选择播放按钮
        player_btn = self.element_locator(player_info['play_status'])
        # 获取data-status的值
        status = player_btn.get_attribute('data-status')
        if status == 'play':
            print('当前是暂停状态')
        elif status == 'pause':
            print('当前是播放状态')
        return player_btn

    def main_view_by_paytips(self):
        """
        function: 通过paytips拉起付费面板
        :return:
        """
        # 点击播放器，暂停播放
        self.element_operation(player_info['player'])
        sleep(2)
        # 点击【购买单片】，拉起付费面板
        sleep(3)
        self.element_operation(player_info['paytips'])

    def main_view_by_progress(self):
        """
        function: 有试看，通过拖动进度条拉起付费面板
        :return:
        """
        # 点击播放器，暂停播放
        self.element_operation(player_info['player'])
        # 获取进度条size
        play_progress = self.element_locator(player_info['play_progress'])
        # 滑动进度条
        played_progress = self.element_locator(player_info['played_progress'])
        xoffset = play_progress.size['width'] / 2
        yoffset = play_progress.size['height']
        self.mouse_move_to((played_progress, xoffset, yoffset), event='element_to_position')
        sleep(3)

    @is_vip(pay_main_view)  # 默认非VIP，VIP传参：user_status='vip',调用pay_video_main_view传参
    def pay_video_main_view(self, element_data, action='buy', pay_method='cash'):
        """
        function: 付费面板拉起购买弹窗/开通会员
        :param element_data: 付费面板元素数据
        :param action: 购买or开通，默认购买
                    {action :{ buy: 购买
                               vip: 开通会员}
                    }
        :param pay_method: 支付方式，默认现金
                    {method :{ cash: 现金购买
                               diamond: 钻石购买}
                    }
        :return:
        """
        if action == 'vip':
            self.element_operation(element_data['vip_btn'])
        elif action == 'buy':
            if pay_method == 'diamond':
                self.element_operation(element_data['diamond_btn'])
            elif pay_method == 'cash':
                self.element_operation(element_data['cash_btn'])

    @is_vip(pay_right_view)
    def pay_video_right_top(self, element_data, action='buy', pay_method='cash'):
        """
        function: 右侧面板拉起购买弹窗/开通会员
        :return:
        """
        if action == 'vip':
            self.element_operation(element_data['vip_btn'])
        elif action == 'buy':
            if pay_method == 'diamond':
                self.element_operation(element_data['diamond_btn'])
            elif pay_method == 'cash':
                self.element_operation(element_data['cash_btn'])

    def payed_view(self, element_data, pay_method='Q币'):
        """
        function: 支付弹窗，选择支付方式，确认支付
        :param element_data: 付费弹窗数据
        :param pay_method: 选择支付的方式
                        {card：QQ卡（需要卡号和密码），
                        wechat：微信支付，
                        QQ：QQ钱包支付，
                        Q币：Q币支付，有Q币不足，充值的情况
                        }
        :return:
        """
        # 切入iframe
        iframe_01 = self.element_locator(element_data['iframe01'])
        self.switch_frame(iframe_01)
        if pay_method == 'card':
            el = self.element_locator((By.XPATH, '//span[contains(text(),"更多方式")]'))
            self.mouse_move_to(el)
            self.element_operation(element_data['pay_method'][3])
            print(element_data['card_num'][0], element_data['card_num'][1])
            debug = self.element_locator(element_data['card_num'][0])
            debug.click()
            debug.send_keys('123456478978')
            # self.element_operation(element_data['card_num'][0], event='input',
            #                        value=element_data['card_num'][1])
            self.element_operation(element_data['card_pwd'][0], event='input',
                                   value=element_data['card_num'][1])
        elif pay_method == 'wechat':
            self.element_operation(element_data['pay_method'][2])
        elif pay_method == 'qq':
            self.element_operation(element_data['pay_method'][1])
        elif pay_method == 'Q币':
            self.element_operation(element_data['pay_method'][0])
        if pay_method != 'wechat' and pay_method != 'QQ':
            # 确认支付
            self.element_operation(element_data['payed_btn'])


if __name__ == '__main__':
    payed = PlayBottomPage(browser_data['driver_path'])
    payed.open_page(browser_data['page_url_file'])
    sleep(5)
    # paytips拉起付费面板
    payed.main_view_by_progress()
    sleep(3)
    # 点击购买
    payed.pay_video_main_view()
    # 登录
    payed.login(login_data_list=login_info_list)
    sleep(3)
    payed.pay_video_right_top()
    sleep(5)
    try:
        payed.payed_view(pay_page_data, pay_method='card')

    except Exception as e:
        pass
    # 关闭浏览器
    # payed.quit_browser()
