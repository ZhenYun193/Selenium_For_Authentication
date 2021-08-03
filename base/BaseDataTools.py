import xlrd
from xlutils.copy import copy


class ReedDataTools:
    """
    class：exel表格基本操作类
    function：{
    1.get_sheet_count_num：获取exel表格的表单数量
    2.get_sheet_all_names：获取exel所有表格的名称
    3.open_sheet：打开表单
    4.get_sheet_property：获取表单的属性
    5.get_cell_value：获取单元个的值
    6.get_rows_values：取指定行所有的单元格的值
    7.get_cols_values：获取指定列所有的单元格的值
    }
    """
    def __init__(self, book_path):
        self.book = xlrd.open_workbook(book_path)

    def get_sheet_count_num(self):
        """
        函数功能：获取exel表格的表单数量
        :return: 表单的个数
        """
        num = self.book.nsheets
        return num

    def get_sheet_all_names(self):
        """
        函数功能：获取exel所有表格的名称
        :return: tuple所有表格的名称
        """
        name = self.book.sheet_names()
        return name

    def open_sheet(self, sheet):
        """
        函数功能：打开表单
        :param sheet: 打开的表单，int时，通过索引打开表单；
                      str时，通过表单名字打开表单
        :return: 表单对象
        """
        if type(sheet) is str:
            return self.book.sheet_by_name(sheet)
        elif type(sheet) is int:
            return self.book.sheet_by_index(sheet)
        else:
            print(f'sheet的数据类型要求是：str或int，当前传入的数据类型是{type(sheet)}')

    def get_sheet_property(self, open_sheet, attribute):
        """
        函数功能：获取表单的属性
        :param open_sheet: 打开的表单对象，传入表单的索引或表单名称
        :param attribute: 表单属性：{
                        name：获取表单名称
                        index：获取表单索引
                        nrows：获取表单的行数
                        ncols：获取表单的列数
                                  }
        :return: 表单属性值
        """
        sheet = self.open_sheet(open_sheet)
        if attribute == 'name':
            return sheet.name
        elif attribute == 'index':
            return sheet.number
        elif attribute == 'nrows':
            return sheet.nrows
        elif attribute == 'ncols':
            return sheet.ncols
        else:
            print(f'attribute输入有误，当前输入值是：{attribute}')

    def get_cell_value(self, open_sheet, cell):
        """
        函数功能：获取单元个的值
        :param open_sheet: 打开的表单对象，传入表单的索引或表单名称
        :param cell: Tuple，(rowx_num，colx_num)，行号和列号，从0开始计算
        :return: 单元格值
        """
        sheet = self.open_sheet(open_sheet)
        return sheet.cell_value(*cell)

    def get_row_values(self, open_sheet, row_num):
        """
        函数功能：获取指定行所有的单元格的值
        :param open_sheet: 打开的表单对象，传入表单的索引或表单名称
        :param row_num: 行号，从0开始计算
        :return: list，元素是每个单元个的值
        """
        sheet = self.open_sheet(open_sheet)
        return sheet.row_values(row_num)

    def get_col_values(self, open_sheet, cols_num):
        """
        函数功能：获取指定列所有的单元格的值
        :param open_sheet: 打开的表单对象，传入表单的索引或表单名称
        :param cols_num: 列号，从0开始计算
        :return: list，元素是每个单元个的值
        """
        sheet = self.open_sheet(open_sheet)
        return sheet.col_values(cols_num)


class WriteDataTools:
    """
    功能：写入exel表格数据
    function：{
    get_sheet：获取新exel表的表单对象
    write_cell_value：写入单元格值
    save_book：保存exel表
    }
    """
    def __init__(self, book_path):
        self.old_book = xlrd.open_workbook(book_path)
        self.new_book = copy(self.old_book)

    def get_sheet(self, sheet_num):
        """
        函数功能： 获取可编辑的sheet对象
        :param sheet_num: sheet的索引值
        :return: sheet对象
        """
        return self.new_book.get_sheet(sheet_num)

    def write_cell_value(self, sheet_num, rowx_num, colx_num, cell_value):
        """
        函数功能：写入单元格的值
        :param sheet_num: 表单的索引
        :param rowx_num: 行号
        :param colx_num: 列号
        :param cell_value:
        :return: 表单对象
        """
        write_cell = self.get_sheet(sheet_num)
        write_cell.write(rowx_num, colx_num, cell_value)
        return write_cell

    def save_book(self, book_path):
        """
        函数功能：保存exel表
        :param book_path: 保存路径
        :return:
        """
        self.new_book.save(book_path)


if __name__ == '__main__':
    book = '../document/元素表1.xls'
    bk = ReedDataTools(book)
    print(bk.get_cell_value(0, (0,1)))


