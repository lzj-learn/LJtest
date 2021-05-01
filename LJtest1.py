# 字符串及字符串的基本处理方法
print('hello world', type('hello world'))    # 字符串类型
print('嘻嘻'+'哈哈')    # 拼接字符串但是只能是相同类型的才可以拼接
print('你好'*3)     # 乘号就是打印多少遍字符串


# 整数类型和浮点型及整型和浮点型基本的处理方式
print(2, type(2))    # 整数类型
print(2.333, type(2.333))    # 浮点类型
print((1+2)*100-9.9/2)  # 主要进行四则运算(加减乘除)


# 布尔类型及布尔类型的基本处理方式
print(True, type(True))     # 布尔类型
print(2 > 3)  # 如果判断是正确的话就返回true,判断错误的话就返回false


a = input('请输入a:')     # 将输入的内容赋值给a
b = input('请输入b:')
print('input的内容是:', a)      # 将a的内容打印出来
print('a+b的结果是:', a+b)   # 这里显示的是a拼接b的效果因为只要是经过input处理的出来的都是字符串


# 强制类型转换
c = int('2333')
c1 = str(2333)
c2 = list('哈哈哈哈')
print(c2, type(c2))


# 作业
d = dict({1: 2, 3: 4})
d1 = 'str'
print((len(d)+len(d1)))   # 一组key-value为一个长度
# 也可以使用len(d+d1)效果是一样的

