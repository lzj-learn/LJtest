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
