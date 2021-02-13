# python的判断和循环
# a = 1
# a1 = 2
# if a == 1:
#     print('a是1')   # if-else中else是可以省略的
# if a > a1:
#     print('a大于a1')
# else:
#     print('a小于a1')

# 因为这里input出来的内容是字符串无法比较,所以这里要先转换字符再比较
# age = int(input('你的年龄:'))
# if age > 30 or age < 10:
#     print('三十而立')   # 可以使用or来判断两个条件满足一个即可运行代码
# elif age > 40:
#     print('四十不惑')
# elif age > 50 and age < 60:
#     print('知天命')     # 可以在if后面用and加上两个条件
# else:
#     print('太小')

# sex = '男'
# sex2 = '男'
# if id(sex) is id(sex2):
#     print('OK')
# elif id(sex) is not id(sex2):
#     print('not ok')

# b = dict({1: 2, 'wa': '你好'})
# b1 = '你好'     # 字典中的in看的只是key值
# if b1 in b:
#     print('在list里面')
# else:
#     print('不在list里面')
#     exit()

# c = 10
# if isinstance(c, int):
#     print('这是个数字')
# elif type(c) is str:    # 效果同上个判断条件一样
#     print('这是个字符串')
# else:
#     print('不明类型')

# d = 1
# while d < 10:
#     print('数字小于10', d)
#     d = d + 2   # 这个就是循环的退出条件

# 练习
# e = list(['x', 'y', 'z'])
# e1 = 0
# e2 = dict({})
# e3 = dict({})
# while e1 < len(e):
#     score = int(input('请输入'+e[e1]+'的成绩:'))
#     if score > 60:
#         e2[e[e1]] = score
#     else:
#         e3[e[e1]] = score
#     e1 = e1 + 1
# print(e2)
# print(e3)

# f = ['wa', '你好']
# for i in f:
#     print(i)
# f1 = list(range(0, 10))    # range的强制类型转换
# print(f1)
# f2 = list(range(0, 10, 2))  # 这里的2为布幅(每隔2个打印一次)
# print(f2)

# 九九乘法表
# for x in range(1, 10):
#     for y in range(1, x+1):
#         print(x, '*', y, '=', x*y, end='')
#         # end写在print里面的话print就不会换行了就直接以空格来结束
#     print()

# 作业1
for x1 in range(10, 0, -1):
    print('红灯还有', x1, '秒')
