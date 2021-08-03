def is_vip(element_data):
    """
    function: 区分付费面板会员和非会员的元素数据，处理完的列表直接当作参数传入被装饰函数
    :param element_data：原始数据
    :return:
    """

    def out_wrapper(fun):
        def wrapper(self, user_status='not vip', *args, **kwargs):
            """
            :param self: 类方法的实例
            :param user_status: 会员状态，默认非VIP
            :return:
            """
            if user_status == 'vip':
                new_list = {'vip_btn': element_data['vip_btn'][1],
                            'cash_btn': element_data['cash_btn'][1],
                            'diamond_btn': element_data['diamond_btn'][1]}
            else:
                new_list = {'vip_btn': element_data['vip_btn'][0],
                            'cash_btn': element_data['cash_btn'][0],
                            'diamond_btn': element_data['diamond_btn'][0]}
            fun(self, new_list, *args, **kwargs)

        return wrapper

    return out_wrapper


if __name__ == '__main__':
    pass
