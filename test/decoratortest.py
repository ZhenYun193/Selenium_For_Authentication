"""
def make_div(func)
    ""对被装饰的函数的返回值 div标签""
    def inner(*args, **kwargs):
        print(f'<div>{func()}</div>')
    return inner


def make_p(func):
    ""对被装饰的函数的返回值 p标签""
    def inner(*args, **kwargs):
        b = f'<p>{func()}</p>'
        return b
    return inner


@make_div
@make_p
def content():
    a = '人生苦短'
    return a
"""

client_zhang = {
    'id': 'client_01',
    'is_authenticated': False,
    'is_vip': True,
    'level': 3,
    'username': 'zhang',
    'password': 'zhang',
    'money': 8,
    'pay_password': 'zhang123456',
    'payed_column': ['japan']
}

client_li = {
    'id': 'client_02',
    'is_authenticated': False,
    'is_vip': False,
    'level': 0,
    'username': 'li',
    'password': 'li',
    'money': 300,
    'pay_password': 'li123456',
    'payed_column': ['guangdong']
}


# 获取用户信息
def get_login_mgs(client):
    username = input('请输入用户名：')
    password = input('请输入密码：')
    if username == client['username'] and password == client['password']:
        client['is_authenticated'] = True
        print(f'------尊敬的{client["username"]}，登录成功------')
        return client
    else:
        print(f'用户名或密码错误， 用户名是：{username}；密码是：{password}')
        get_login_mgs(client)


# 获取支付信息
def get_pay_mgs(client, column):
    """
    function:支付
    :return:
    """
    while True:
        pay_password = input('请输入支付密码：')
        if pay_password == client['pay_password'] and 10 <= client['money']:
            client['payed_column'].append(column)
            client['money'] = client['money'] - 10
            msg = 'pay_success'
            return msg
        elif pay_password == client['pay_password'] and 10 > client['money']:
            print(f'余额不足，请充值；当前余额:￥{client["money"]}元')
            return 'money not enough'
        else:
            print('------密码错误，请重新输入------')


# 登录鉴权
def authenticate_login(function):
    def wrapper(client, *args):
        if client['is_authenticated'] is True:
            print(f'------尊敬的{client["username"]}，已登录------')
            return f'------成功进入【{function(*args)}】栏目------'
        else:
            get_login_mgs(client)
            return f'------成功进入【{function(*args)}】栏目------'
    return wrapper


# 购买鉴权
def authenticate_pay(function):
    def wrapper(client, column, *args, **kwargs):
        while True:
            if client['is_authenticated'] is False:
                get_login_mgs(client)
            else:
                if column in client['payed_column']:
                    result = f'------你已解锁栏目【{function(*args, **kwargs)}】，请进入观看------'
                    return result
                else:
                    print(f'------栏目【{column}】需要付费解锁，请支付￥10元解锁进入------')
                    while True:
                        is_pay = input('是否购买,Y/N?：')
                        if is_pay == 'Y':
                            mas_pay = get_pay_mgs(client, column)
                            if mas_pay == 'pay_success':
                                print(f'已解锁栏目：【{client["payed_column"]}】,当前余额：￥{client["money"]}元')
                                result = f'------打开【{function(*args, **kwargs)}】栏目------'
                                return result
                            else:
                                return mas_pay
                        elif is_pay == 'N':
                            print('取消支付成功')
                            return None
                        else:
                            print('输入错误，请输入:Y or N')
    return wrapper


# 会员鉴权
def authenticate_vip(function):
    def wrapper(client, *args, **kwargs):
        while True:
            if client['is_authenticated'] is True:
                if client['is_vip'] is True:
                    function(*args, **kwargs)
                    return f'------进入成功【{function()}】栏目------'
                else:
                    print(f'------栏目【{function()}】仅会员可进入，请支付￥30元升级会员后进入-------')
                    while True:
                        pay_password = input('请输入支付密码：')
                        if pay_password == client['pay_password']:
                            client['money'] = client['money'] - 10
                            client['is_vip'] = True
                            print(f'------支付成功，尊敬的{client["username"]}已是会员------')
                            return f'------进入成功【{function()}】栏目------'
                        else:
                            print('------密码错误，请重新输入------')
            else:
                get_login_mgs(client)
    return wrapper


@ authenticate_pay
def home():
    home_page = '首页'
    return home_page


@ authenticate_vip
def america():
    america_column = '欧美'
    return america_column


@ authenticate_login
def japan():
    japan_column = '日本'
    return japan_column


def china():
    china_column = '中国'
    return china_column


if __name__ == '__main__':
    home(client_zhang, 'home')
