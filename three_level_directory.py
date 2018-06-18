#!/usr/bin/env python

# 定义程序说明
description = '''
    程序说明：
    此程序为多级菜单，用户输入菜单前面的数字以进入各级菜单。
    还可输入 b 返回上级菜单，输入 q 退出程序。
'''
# 定义目录结构
menu = {
    '1_1': {
        '1_1_1': {
            '1_1_1_1': 'finally1',
            '1_1_1_2': 'finally2'
        },
        '1_1_2': {
            '1_1_2_1': 'finally1',
            '1_1_2_2': 'finally2',
            '1_1_2_3': 'finally3'
        }
    },
    '1_2': {
        '1_2_1': {
            '1_2_1_1': 'finally1',
            '1_2_1_2': 'finally2'
        },
        '1_2_2': {
            '1_2_2_1': 'finally1',
            '1_2_2_2': 'finally2',
            '1_2_2_3': 'finally3'
        }
    },
    '1_3': {
        '1_3_1': {
            '1_3_1_1': 'finally1',
            '1_3_1_2': 'finally2'
        },
        '1_3_2': {
            '1_3_2_1': 'finally1',
            '1_3_2_2': 'finally2',
            '1_3_2_3': 'finally3'
        }
    }
}

# 打印程序说明
print(description)

# 程序逻辑
while True:
    # 显示第一层目录结构
    print('一级菜单')
    for index, key in enumerate(menu.keys()):
        print(index+1, key)
    str1 = input('数字？ "b"？ "q"？')
    # 根据用户输入选择做调整
    # 如果是第一个菜单
    if str1 == '1':
        while True:
            print('二级菜单')
            for index, key in enumerate(menu['1_1'].keys()):
                print(index+1, key)
            str2 = input('数字？ "b"？ "q"？')
            if str2 == '1':
                while True:
                    print('三级菜单')
                    for index, key in enumerate(menu['1_1']['1_1_1'].keys()):
                        print(key)
                    print('这是最底层菜单')
                    str3 = input('返回 "b" 或退出 "q" ？')
                    if str3 == 'b':
                        break
                    elif str3 == 'q':
                        exit()
                    else:
                        print('\n请输入正确的字符！')
            elif str2 == '2':
                while True:
                    print('三级菜单')
                    for index, key in enumerate(menu['1_1']['1_1_2'].keys()):
                        print(key)
                    print('这是最底层菜单')
                    str3 = input('返回 "b" 或退出 "q" ？')
                    if str3 == 'b':
                        break
                    elif str3 == 'q':
                        exit()
                    else:
                        print('\n请输入正确的字符！')
            elif str2 == 'b':
                break
            elif str2 == 'q':
                exit()
            else:
                print('请输入正确的数字或标志！')
                continue
    # 如果是第二个菜单
    elif str1 == '2':
        while True:
            print('二级菜单')
            for index, key in enumerate(menu['1_2'].keys()):
                print(index+1, key)
            str2 = input('数字？ "b"？ "q"？')
            if str2 == '1':
                while True:
                    print('三级菜单')
                    for index, key in enumerate(menu['1_2']['1_2_1'].keys()):
                        print(key)
                    print('这是最底层菜单')
                    str3 = input('返回 "b" 或退出 "q" ？')
                    if str3 == 'b':
                        break
                    elif str3 == 'q':
                        exit()
                    else:
                        print('\n请输入正确的字符！')
            elif str2 == '2':
                while True:
                    print('三级菜单')
                    for index, key in enumerate(menu['1_2']['1_2_2'].keys()):
                        print(key)
                    print('这是最底层菜单')
                    str3 = input('返回 "b" 或退出 "q" ？')
                    if str3 == 'b':
                        break
                    elif str3 == 'q':
                        exit()
                    else:
                        print('\n请输入正确的字符！')
            elif str2 == 'b':
                break
            elif str2 == 'q':
                exit()
            else:
                print('请输入正确的数字或标志！')
                continue
   # 如果是第三个菜单
    elif str1 == '3':
        while True:
            print('二级菜单')
            for index, key in enumerate(menu['1_3'].keys()):
                print(index+1, key)
            str2 = input('数字？ "b"？ "q"？')
            if str2 == '1':
                while True:
                    print('三级菜单')
                    for index, key in enumerate(menu['1_3']['1_3_1'].keys()):
                        print(key)
                    print('这是最底层菜单')
                    str3 = input('返回 "b" 或退出 "q" ？')
                    if str3 == 'b':
                        break
                    elif str3 == 'q':
                        exit()
                    else:
                        print('\n请输入正确的字符！')
            elif str2 == '2':
                while True:
                    print('三级菜单')
                    for index, key in enumerate(menu['1_3']['1_3_2'].keys()):
                        print(key)
                    print('这是最底层菜单')
                    str3 = input('返回 "b" 或退出 "q" ？')
                    if str3 == 'b':
                        break
                    elif str3 == 'q':
                        exit()
                    else:
                        print('\n请输入正确的字符！')
            elif str2 == 'b':
                break
            elif str2 == 'q':
                exit()
            else:
                print('请输入正确的数字或标志！')
                continue
    elif str1 == 'b':
        print('这已经是第一级目录了！')
        continue
    elif str1 == 'q':
        print('祝你好运！')
        exit()
    else:
        print('请输入正确的数字或标志！')
        continue
