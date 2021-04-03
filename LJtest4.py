import time
import random

# 循环的break和continue
for a in range(10):
    if a == 4:
        continue   # 这里使用continue就会跳过4的那次循环
    if a == 5:
        break   # 这里使用break表示到了5的那次循环后就会直接结束循环
    print(a)

# 九九乘法表的break
for x in range(1, 10):
    for y in range(1, x+1):
        if x == 3:
            break   # 这个break只会结束一层循环外面的循环还是会继续
        print(x, '*', y, '=', x*y, end=' ')
        # end写在print里面的话print就不会换行了就直接以空格来结束
    print()

# 函数
"""
例子: 自动判断是5-8位,且账号开头必须是小写字母
def:方法的声明   check:函数的名称(唯一的)     username:函数的参数(可以省略)    代码体:函数的逻辑       两行后的check:调用函数
return:可以拿到函数的返回值(可以进行后续的操作)
"""


def check(username):
    if 5 <= len(username) <= 8:
        if 'a' <= username[0] <= 'z':
            print('账号正确')
        else:
            print('首字母没小写')
    else:
        print('字数长度5-8')


check('a123456')


def add(c, d):
    if type(c) is int and type(d) is int:
        print(c+d)
    else:
        print('请输入整数')


add(12, 88)
print(add(12, 88))  # 因为函数里面没有return所以这里出来的是None


def add2(c1, d1):
    if type(c1) is int and type(d1) is int:
        return c1+d1
    else:
        return '请输入整数'


add2(12, 88)    # 用了return这个就没有效果了
print(add2(12, 88))


"""
异常:代码出错     异常捕获:try-except语句(必须成对出现)
流程:如果代码不是会报错的代码就会运行try的代码结果,如果try里面的代码会报错就会运行except里面的代码
异常类:Exception就是异常类然后通过as重命名给一个变量,然后错误信息就会返回给这个变量
"""
try:
    print('a'+1)
except Exception as e:
    print('上面代码出错', e)

# 当我们无法判断用户输入的内容是否是正确的情况下可以使用try-except
f = input('请输入你的姓名:')
f1 = input('请输入你的年龄:')
try:
    if int(f1) > 18:
        print(f1, '成年了')
    else:
        print(f1, '你还没成年')
except Exception():
    print('请输入正确的年龄')

# time包的效果
for x in range(10):
    time.sleep(1)   # 这个可以让这个循环没隔一秒跳出一个数字
    print(x)

# random包的效果
g = random.randint(10, 100)     # 随机生成一个10-100的随机数
print(g)


# test4作业：定义一个方法来判断用户输入的账号密码是否符合规范
def check():    # 将输入写进函数中
    username = input('请输入账号:')
    password = input('请输入密码:')
    if len(username) >= 5 and len(username) <= 8:
        if 'a' <= username[0] <= 'z':
            if 8 <= len(password) <= 16:
                return True
            else:
                return "密码长度不符合规范"
        else:
            return "账号首字母不是英文小写"
    else:
        return "账号长度不符合规范"


print(check())  # 函数中有return的时候需要用print来看到return
