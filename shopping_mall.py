#!/usr/bin/env python
#-*-coding:utf-8-*-

# 显示欢迎信息
print('欢迎来到 JUXER 网上商城')

# 从文件读取商品名称和价格并放入 goods 字典中
goods = {}
with open('goods.txt', 'r') as f:
    goods_list = f.readlines()
    for good in goods_list:
        name, price = good.strip('\n').split(': ')
        goods[name] = int(price)

# 展示可以购买的商品和相应的价格
print('你可以购买的商品有')
for name, price in goods.items():
    print('商品:', name, '价格', price)

# 提示用户输入需要购买的商品以及数量
print('\n选择商品和数量加入购物车，格式为（商品1 数量1，商品2 数量2）')
# 接收用户输入并将其存入购物车中
cart_str = input('比如 01 1, 02 2, 03 2: ')
cart_list = cart_str.strip().split(',')
cart_dir = {}
for good in cart_list:
    name, number = good.strip().split(' ')
    if name in cart_dir.keys():
        cart_dir[name] += int(number)
    else:
        cart_dir[name] = int(number)
# 显示购物车中的产品和数量并提示是否要去结算或退出
# 定义用户钱包余额
total = 100
# 记录购物车内物品总价格
sum = 0
print('您的购物车中有：')
for name, number in cart_dir.items():
    print('商品：', name, '数量：', number)
    sum += number * goods[name]
print('合计：', sum)
while sum > total:
    sign = input('抱歉：你的余额不足，您可以输入 c 充值或者 q 退出！')
    if sign == 'c':
        num = int(input('请输入充值金额：'))
        total += num
        print('充值成功！')
    if sign == 'q':
        exit()
total -= sum
print('\n购买成功！谢谢光临。')

