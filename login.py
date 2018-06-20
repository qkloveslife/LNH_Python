#!/usr/bin/env python

# 定义变量保存用户名和密码
username = ['admin', 'orz']
userpasswd = {'admin': '123456', 'orz': '654321'}
dark_list = []
# 定义计数器
count = 0
while True:
    # 提示用户可以输入的用户名和密码
    print('请输入用户名和密码（用户 admin 的密码为：123456')
    print('用户 orz 的密码为：654321）')

    # 提示用户输入登录名
    name = input('请输入你的用户名：')
    # 检查用户是否在黑名单中
    if name in dark_list:
        print('\n你的账户已经被锁定了！！！')
        continue
    while count < 3:
        # 如果登录名存在
        if name in username:
            count += 1
            # 提示用户输入密码
            passwd = input('请输入你的密码：')
            # 判断密码是否正确
            if passwd == userpasswd[name]:
                print('恭喜你，登陆成功!')
                exit()
            else:
                print('密码错误！')
                if count == 3:
                    print('\n登录次数达到上限！！！')
                    dark_list.append(name)
                    count = 0
                    break
                continue
        # 如果用户名不存在
        else:
            print('用户名不存在！')
            if count == 3:
                print('登录次数达到上限')
            break