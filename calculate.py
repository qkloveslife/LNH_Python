'''
思路：
    1，遍历公式字符串，如果字符不是“)”就将其放入列表中，如果是就在列表中向前找与其对应的“(”并计算它们之间的内容
    2，计算括号之间的内容并用其结果替换原来的内容
    3，计算没有括号的公式
'''

def calc(formula):
    # 用于标记负号出现的次数，这个负号是出现在“*()”或者“/()”的括号中的结果
    # 比如 *(-1) 则 sign 加 1 然后将 -1 变成 1，否则不加
    sign = 0

    # 用来存放 formula 中的字符
    list10 = []

    # 遍历 formula 中的字符
    for c in formula:
        # 如果不是“)”就将它放入列表中
        if c != ')':
            list10.append(c)
        # 如果是“)”就向前找与其对应的“(”
        else:
            # 用来存放括号内的内容
            short_formula = []
            # 反向寻找“(”
            for c1 in reversed(list10):
                # 找到“(”后弹出后跳出循环
                if c1 == '(':
                    list10.pop()
                    break
                # 如果不是“(”就将其标记为括号内的内容
                else:
                    short_formula.append(list10.pop())
            # 处理括号内的内容
            short_formula.reverse()
            short_formula = ''.join(short_formula)
            # 将括号内的内容交给相应函数处理
            result = calc_short(short_formula)

            # 处理结果为负数的情况
            if result.startswith('-'):
                # 如果括号前面的符号为“+”或“-”
                if list10[-1] == '-':
                    list10[-1] = '+'
                elif list10[-1] == '+':
                    list10[-1] = '-'
                # 如果括号前面的符号为“*”或“/”
                else:
                    # 用来标记是否找到并替换前面的“+”或“-”
                    change = False
                    # 向前找“+”或“-”并做相应处理
                    for ind, i in enumerate(reversed(list10)):
                        if i == '+':
                            list10[len(list10)-ind-1] = '-'
                            change = True
                        elif i == '-':
                            list10[len(list10)-ind-1] = '+'
                            change = True
                    # 如果没有找到“+”或“-”就将标志位加 1 ，后面根据 sign 判断整体结果的符号
                    if change == False:
                        sign += 1
                        # list10.append(result)
                # 将结果存放到原列表中起到替代原括号内容的效果
                list10.append(str(abs(float(result))))
            # 如果结果为正则不做处理直接加入元列表起到替代原括号内容的效果
            else:
                list10.append(result)
    # 根据 sign 来判断结果最终的符号
    if sign % 2 != 0:
        return abs(float(calc_short(''.join(list10))))
    else:
        return calc_short(''.join(list10))



# 用来计算加减乘除
def calc_short(short_formula):
    # 先根据“+”分割字符串
    list1 = short_formula.split('+')
    # 处理以“+”分割的字符串
    for index1, item1 in enumerate(list1):
        # 用来记录第一个数字是不是负号
        signal = 0
        # 处理第一个数字是负数的情况
        if item1.startswith('-'):
            list2 = item1[1:].split('-')
            signal += 1
        # 如果第一个不是负数就正常以“-”分割字符串
        else:
            list2 = item1.split('-')

        # 处理只剩下“*/”负号的字符串
        for index2, item2 in enumerate(list2):
            # 如果字符串中没有“*/”符号就直接跳过
            if ('*' not in item2) and ('/' not in item2):
                continue
            # 以“*”符号分割字符串使得它只剩下“/”运算
            list3 = item2.split('*')
            # 计算除法运算
            for index3, item3 in enumerate(list3):
                if '/' not in item3:
                    continue
                list4 = item3.split('/')
                sum1 = float(list4[0])
                for item4 in list4[1:]:
                    sum1 /= float(item4)
                # 用计算结果替代原来的内容
                list3[index3] = str(sum1)
            # 计算“*”运算
            sum2 = float(list3[0])
            for item5 in list3[1:]:
                sum2 *= float(item5)
            # 用结果替换掉原来的内容
            list2[index2] = str(sum2)

        # 如果第一个数字是负数就做负号处理
        if signal % 2 != 0:
            sum3 = -float(list2[0])
        else:
            sum3 = float(list2[0])
        # 计算“-”运算符
        for item6 in list2[1:]:
            sum3 -= float(item6)
        # 用计算结果替换原来的内容
        list1[index1] = str(sum3)

    # 计算“+”运算符
    sum4 = float(list1[0])
    for item7 in list1[1:]:
        sum4 += float(item7)
    short_formula = str(sum4)
    # 将结果以字符串的形式返回
    return short_formula

if __name__ == '__main__':
    formula = '1-2*(60-30+(-40/5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2)'
    print(calc(formula))