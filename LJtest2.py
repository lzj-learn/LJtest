# # 元祖的基本处理方法
# # a = tuple(({1: 2, 3: 4}))     # 元祖里面放入字典
# # print(a)    # 打印出来的只有dict中的key值
# # print((1,), type((1,)))     # 元组类型
# # b = tuple(('哈哈', 'wa', 1, True, None))
# # print(b[3])     # 通过下标来找到元祖中的值
# # print(b.index(1))   # 通过值来找下标值
# # print(b.count('wa'))    # 统计'wa'一共在tuple中出现了多少次
# # print(b[0:3])   # 找出范围内对应下标的值
# # print(b[3:])    # 这样就是从下标3开始一直到最后一个下标的对应值
# # print(b[:])     # 表示从头开始到尾
# # c = tuple((b, ('哈哈', 1, 'was', True)))      # 二维元祖(元祖里面嵌套元祖)
# # print(c)    # 调用了上面b的元祖
# # print(c[0][1])  # 二维元祖通过下标来找值
# # print(c[1].index(1))
# # c2 = tuple((0, False, 1, True))
# # print(c2.count(1))


# # 数组的基本处理方法
# # print([2], type([2]))   # 数组(列表)类型
# # d1 = list([1, 2])
# # d = list(['哈哈', 'wa', 1, True, None])
# # print(d[0], d.index(1), d.count('wa'))
# # # list和tuple的区别:list写好后可以修改，而元祖不行
# # d.append('append')  # 追加一个元素(tuple没有这个方法)
# # print(d)
# # d.insert(0, 'insert')
# # print(d, d[0])
# # print(d.pop(1), d)     # 将下标为1的值剪切出数组
# # d.extend(d1)    # 插入数值并合并
# # print(d)
# # print(d+[3, 4])     # 效果同extend相同
# # d.remove(None)  # 将None这个值从list中剔除
# # print(d)
# d3 = list([0, False, 1, True])  # 0等价于false,1等价于true
# # print(d3.count(0))  # 这里统计的时候会把false也算上


# # 字典的基本处理方法
# print({1: 2}, type({1, 2}))     # 字典类型
# e = dict({'name': 'x', 'age': 12, (): []})
# print(e)
# print(e['name'])    # 通过key来找value
# print(e.get('age'))     # 效果同上通过key来找value
# e['high'] = '183cm'     # 如果这里的key不存在的话就是新增一组key-value值
# print(e)
# e['name'] = 'y'     # 如果存在就是修改key-value值
# print(e)
# print(e.pop(()))    # 通过key值来删除key-value值
# e.update(weight='85kg')     # 增加一组key-value值,如果key值存在就是修改key-value值
# print(e)

# # 数组和字典的删除(通用方法)
# del e['name']   # 通过key来删除value值
# print(e)
# del d3[1]   # 通过下标删除list中的元素
# print(d3)

# 作业
f = input('请输入你的姓名:')
f1 = input('请输入你的年龄:')
f2 = input('请输入你的性别:')
f3 = dict({})
f3.update(name=f, age=f1, sex=f2)
print(f3)
