import os
import requests
from cv2 import cv2


def kill_chromedriver():
    """
    function: 删除chromedriver进程
    :return:
    """
    os.system('taskkill /F /IM chromedriver.exe')


def find_chromedriver():
    """
    function: 查询chromedriver进程
    :return:
    """
    os.system('tasklist | findstr chromedriver.exe')


def down_img(down_link, save_path):
    """
    function: 下载文件
    :param down_link: 下载路径
    :param save_path: 保存路径
    :return:
    """
    # 获取图片二进制数据
    img_bit = requests.get(down_link).content
    # 保存为图片文件
    img = open(save_path, mode='wb')
    img.write(img_bit)
    img.close()


def match_img(master_img_path, second_img_path):
    """
    function: 匹配两张图片的位置
    :param master_img_path: 主图片路径
    :param second_img_path: 副图片路径
    :return: 坐标
    """
    # 读取主图片
    master_img_rgb = cv2.imread(master_img_path)
    # 主图片灰度处理
    master_img_gray = cv2.cvtColor(master_img_rgb, cv2.COLOR_BGR2GRAY)
    # 读取副图片
    second_img_rgb = cv2.imread(second_img_path, 0)
    # 匹配副图在在图中的位置
    res = cv2.matchTemplate(master_img_gray, second_img_rgb, cv2.TM_CCOEFF_NORMED)
    value = cv2.minMaxLoc(res)
    return value
