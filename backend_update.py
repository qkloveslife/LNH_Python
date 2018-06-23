import json

# 提示用户输入记录
record_str = input("请输入你的记录：")

# 将用户输入的字符串转换成字典
record = json.loads(record_str)

# 取得需要插入的字符串
backend_value = record['backend']
record_value = record['record']
insert_str = '    server 100.1.7.9 %s weight %d maxconn %d\n' %(record_value['server'], record_value['weight'], record_value['maxconn'])

with open('backend.txt', 'r+') as f:
    # 定义要寻找的字符串
    str_to_find = 'backend %s\n' %(backend_value)
    # 将文件内容读取到 contents 中
    contents = f.readlines()
    # 找到‘需要寻找’的字符串的位置
    index = contents.index(str_to_find)
    # 定位‘要插入字符串’的位置
    for i in range(len(contents)-index):
        if '\n' == contents[index+i+1]:
            insert_index = index+i+1
            break
    # 插入字符串
    contents.insert(insert_index, insert_str)
    # 将列表转化为字符串
    contents_str = ''.join(contents)
    # 将文件指针移动到开头
    f.seek(0)
    # 将处理过的字符串写进文件中
    f.write(contents_str)
