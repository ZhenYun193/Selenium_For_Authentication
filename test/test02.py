# 滑块验证处理, 使用opencv-python模块识别图片
from time import sleep
from func.MyFunction import *
from infofile.BroswerData import *
from base.MyDriver import MyDriver

dri_debugger = MyDriver(browser=browser_data['browser'],
                        driver_path=browser_data['driver_path'])


def sliding_slider():
    url = r'https://i.qq.com'
    dri_debugger.open_page(url)
    sleep(1)
    # 切入iframe, 点击[账号密码登录]
    dri_debugger.switch_frame('login_frame')
    dri_debugger.element_operation((By.ID, 'switcher_plogin'), event='click')
    # 输入账号密码
    dri_debugger.element_operation((By.ID, 'u'), event='input', value='1499820342')
    dri_debugger.element_operation((By.ID, 'p'), event='input', value='1499820342')
    # 点击【登录】btn
    sleep(1)
    dri_debugger.element_operation((By.ID, 'login_button'), event='click')
    sleep(2)
    # 下载图片
    img_iframe = dri_debugger.element_locator((By.XPATH, '//*[@id="tcaptcha_iframe"]'))
    dri_debugger.switch_frame(img_iframe)
    sleep(1)
    big_img_link = dri_debugger.element_operation((By.ID, 'slideBg'),
                                                  event='attribute', attribute_name='src')
    small_img_link = dri_debugger.element_operation((By.ID, 'slideBlock'),
                                                    event='attribute', attribute_name='src')
    small_ele = dri_debugger.element_locator((By.ID, 'slideBlock'))
    while True:
        # 下载大图和小图
        down_img(big_img_link, './img/big_img.png')
        down_img(small_img_link, './img/small_img.png')
        # 匹配小图在大图中的位置
        locator = match_img('./img/big_img.png', './img/small_img.png')
        x = int(locator[2][0] * 280/680)-30
        # 滑动小图
        dri_debugger.mouse_move_to(small_ele, x, 0, event='element_to_position')
        sleep(2)
        try:
            dri_debugger.element_operation((By.XPATH, '//*[@id="e_reload"]'),event='click')
        except Exception as e:
            break
    dri_debugger.quit_browser()


if __name__ == '__main__':
    sliding_slider()
