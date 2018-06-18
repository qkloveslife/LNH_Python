#!/usr/bin/env python

# 提示用户可以输入的用户名和密码
print('请输入用户名和密码（用户 admin 的密码为：123456')
print('用户 orz 的密码为：654321）')

# 定义变量保存用户名和密码
username = ['admin', 'orz']
userpasswd = {'admin': '123456', 'orz': '654321'}

# 提示用户输入登录名
name = input('请输入你的用户名：')
# 如果登录名存在
if name in username:
    # 提示用户输入密码
    passwd = input('请输入你的密码：')
    # 判断密码是否正确
    if passwd == userpasswd[name]:
        print('恭喜你，登陆成功!')
    else:
        print('密码错误！')
# 如果用户名不存在
else:
    print('用户名不存在！')