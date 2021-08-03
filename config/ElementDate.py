from base.BaseDataTools import ReedDataTools

work_book = {
    'book_path': '../document/元素表1.xls',
    'sheet_name': ['付费面板', '登录']
}


def get_paytips_path(path, sheet_name, rows_num):
    bottom_book = ReedDataTools(path)
    bottom_paytips_rowx_value = bottom_book.get_row_values(sheet_name, rows_num)
    paytips_xpath = bottom_paytips_rowx_value[4]
    return paytips_xpath


if __name__ == '__main__':
    print(get_paytips_path(work_book['book_path'], work_book['sheet_name'][0], 14))
