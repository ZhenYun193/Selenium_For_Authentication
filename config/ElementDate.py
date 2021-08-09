from selenium.webdriver.common.by import By

# 启动浏览器信息
browser_data = {
    'browser': 'chrome',
    'driver_path': '../driver/chrome/chromedriver.exe',
    'page_url_baidu': 'https://www.baidu.com',
    'page_url_file': 'https://v.qq.com/x/cover/mzc00200uvgh0p1.html',
    'info': [('useAutomationExtension', False), ("excludeSwitches", ['enable-automation']),
             '--start-maximized']
}

# 登陆信息
login_info_list = {
    # 头像
    'head_portrait': (By.XPATH, '//div[@id="mod_head_user"]/a'),
    # login_type': 'QQ'
    'login_type': (By.XPATH, '//div[@id="login_win_type"]//a[@data-type="qq"]'),
    # 'login_method':'username and password'
    'login_method': (By.XPATH, '//div[@id="bottom_qlogin"]/a'),
    'iframe': {
        'iframe_01': '_login_frame_quick_',
        'iframe_02': 'ptlogin_iframe',
    },
    'user_mgs': {
        'username': [(By.ID, 'u'), '1026466206'],
        'password': [(By.ID, 'p'), 'Tencent123#']
    },
    'login_btn': (By.ID, 'login_button'),
    'login_out': (By.XPATH, '//a[@data-type="logout"]')
}

# 退登信息
logout_info_list = {
    # 头像
    'head_portrait': (By.XPATH, '//div[@id="mod_head_user"]/a'),
    'login_out': (By.XPATH, '//a[@data-type="logout"]')
}


# 播放器控件
player_info = {
    'player': (By.XPATH, '//div[@id="tenvideo_player"]'),
    # play_progress :整条播放进度条
    'play_progress': (By.XPATH, '//txpdiv[@class="txp_progress_list"]'),
    # played_progress:已经播放的进度条
    'played_progress': (By.XPATH, '//txpdiv[@class="txp_progress_play"]'),
    'paytips': (By.XPATH, '//a[contains(text(),"购买单片")]'),
    # 'ps': 'data-status=play时，暂停播放'
    'play_status': (By.XPATH, '//txpdiv[@aria-label="播放/暂停"]')
}

# 付费面板
pay_main_view = {
    'vip_btn': [(By.XPATH, '//div[@class="action mt_15"]/a[contains(text(),"开通VIP")]'),
                (By.XPATH, '//a[contains(text(),"续费VIP享精彩不断")]')],
    'cash_btn': [(By.XPATH, '//div[@class="content"]//a[contains(text(),"元原价购买")]'),
                 (By.XPATH, '//div[@class="content"]//a[contains(text(),"元购买")]')],
    'diamond_btn': [(By.XPATH, '//div[@id="_vip_player_sec"]//a[contains(text(),"钻原价购买")]'),
                    (By.XPATH, '//div[@id="_vip_player_sec"]//a[contains(text(),"钻购买")]')]
}

# 右侧面板
pay_right_view = {
    'vip_btn': [(By.XPATH, '//div[@class="action"]/a[contains(text(),"开通VIP")]'),
                ('', '')],
    'cash_btn': [(By.XPATH, '//div[@id="_vip_player_sec"]//a[contains(text(),"元原价购买")]'),
                 ('', '')],
    'diamond_btn': [(By.XPATH, ''),
                    ('', '')]
}

# 支付弹窗
pay_page_data = {
    'iframe01': (By.XPATH, '//iframe[@class="cash_dialog_frame"]'),
    'pay_method': (
        (By.XPATH, '//span[contains(text(),"Q币支付")]'),
        (By.XPATH, '//span[contains(text(),"QQ钱包")]'),
        (By.XPATH, '//span[contains(text(),"微信支付")]'),
        (By.XPATH, '//span[contains(text(),"QQ卡")]'),
    ),
    # QQ卡，卡号密码
    'card_num': [(By.XPATH, '//*[@placeholder="请输入QQ卡号"]'), '456431316545'],
    'card_pwd': [(By.XPATH, '//*[@placeholder="请输入QQ卡密码"]'), '48944646131'],
    'payed_btn': (By.XPATH, '//span[contains(text(),"确认支付")]'),
}

ad_info = {
    'ad_title_text': (By.XPATH, '//txpdiv[contains(text(),"关闭该广告")]'),
    'ad_time': (By.XPATH, '//txpdiv[@data-role="adplayer-video-countdown"]')
}
