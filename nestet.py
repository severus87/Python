# 这是“nester.py”模块， 用来显示列表里的每一个元素。该模块只有一个函数print_lol()
def print_lol(list_item):
    # 该函数只有一个变量list_item，该变量是个列表
    for deep_item in list_item:
        if isinstance(deep_item, list):
            print_lol(deep_item)
        else:
            print(deep_item)
