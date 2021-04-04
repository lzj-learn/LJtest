import time
# 类的概念
"""
class后面声明类的名称,类的名称首字母必须大写
例子：class Test() 中Test为类的名称所以首字母必须大写
面向对象概念：类=对象
1.定义了一个对象后需要初始化一些默认值(使用函数def来定义,定义的def里面必须传一个self参数)
2.随后通过初始化self来完成对象的初始化(可以不写初始化函数)
3.初始化后可自定义函数来赋予这个对象的功能(自定义的函数也需要传一个self参数)
tips：若函数需多个参数,则第二个参数开始可以自定义(num为自定义参数)
4.初始化的参数可以在下面自定义的函数中被使用
5.类的特点：继承、重写/多态
    继承:可以继承被继承class的所有函数(继承的为子类 被继承的为父类)
    所有类都会默认继承object这个类的函数,而__init__为objcet中的函数
"""


class Test():
    def __init__(self):     # 对类进行基础属性的初始化,这个函数可以不写
        self.sex = "女"
        self.high = "170cm"
        self.weight = "60kg"
        self.hair = "大波浪"
        self.age = "30岁"

    def showtime(self, num):
        # 初始化的参数被使用
        print("你的身高"+self.high+"体重"+self.weight+"的"+self.age+"女朋友")
        if num == 1:
            print("活好")
        elif num == 2:
            print("多金")
        else:
            print("唱跳rap")

    def skill(self):
        print("你年龄"+self.age+"发型"+self.hair+"的"+self.age+"女朋友")
        print("快乐")

    def work(self):
        print("这是性别为"+self.sex+"朋友")
        print("挣钱")


# 完成类的定义后需要将类进行实例化
# ohashi = Test()     # 将类进行实体化,实例化后即可操作类
# ohashi.showtime(1)  # 调用类里面的函数
# ohashi.skill()
# print(ohashi.high)   # 查看基础设定时候需要使用print


"""
自定义初始化的默认值(在调用的时候填写默认值)
"""


class Test2:
    def __init__(self, sex2, high2, weight2, age2, hair2):
        self.sex = sex2
        self.high = high2
        self.weight = weight2
        self.age = age2
        self.hair = hair2


# 在实例化的时候填入默认值参数
# miku = Test2('男', '180cm', '75kg', '25岁', '短发')
# print(miku.sex)


class Testinherit(Test2):   # Testinherit继承了Test2,Test2为父类 Testinherit为子类
    def work(self):     # 可以给子类加上属于自己的函数,若何父类函数名相同则在子类中以子类函数为准
        print("修电脑")


jessica = Testinherit('人妖', '180cm', '70kg', '25岁', '黑长直')
print(jessica.sex)
jessica.work()


# 文件的读写改动
text = input("请输入内容：")    # 将text的内容写入测试.txt文件里
with open("测试.txt", "w", encoding="utf8") as f:
    f.write(text+"\n")   # 如果文件里面原来有内容的话w模式会将里面的内容清空后再写入

text2 = input("请输入追加的内容：")    # 将text的内容写入测试.txt文件里
with open("测试.txt", "a", encoding="utf8") as f2:
    f2.write(text2+"\n")   # 使用a模式就可以在文件里面追加内容,\n可以达到换行的效果

# 日记本功能
now = time.strftime("%y-%m-%d %H:%M:%S")    # 用time包获取当前时间(年月日时分秒)

text3 = input("请输入内容：")    # 将text的内容写入测试.txt文件里
with open("E:/测试.txt", "w", encoding="utf8") as f3:
    f3.write(now+"\n")      # 将时间写入txt中
    f3.write(text3+"\n")    # 这里同过写入绝对路径将测试.txt文件写入E盘中
    f3.write("-----------------\n")

with open("E:/测试.txt", "r", encoding="utf8") as f4:
    text4 = f4.read()
    print(text4)    # 这里显示出来的内容是list形式
for i in text4:
    print(i)    # list可以直接使用循环来遍历
