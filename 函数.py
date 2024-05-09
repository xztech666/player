# 函数
# 函数的定义和调用
# 作用:封装代码  (将代码用一个容器储存起来,即拿即用)
# 定义: def  函数名():
#             函数体
# 调用: 函数名()

# while True:
#    number = input("请输入手机号:")
#    if number[0] == '1' and len(number) == 11 and number.isdigit():
#        print(f"{number}是手机号")
#        break
#    else:
#        print(f'{number}不是手机号')

# def number():
#    number = input("请输入手机号:")
#    if number[0] == '1' and len(number) == 11 and number.isdigit():
#        print(f"{number}是手机号")
#    else:
#        print(f'{number}不是手机号')

# 函数的参数
# 函数名(x)  x称为必备参数 必须传入值
# 函数名(y = n) y称为默认参数  不传入值时值为n  传入值(m)时为m
# 不定长参数: (不传入值也不会报错)
#     *args:将多余的值保留  用元祖保留起来
#     **kwargs:将key = value的值 用字典保留起来

##def number(num,phone='华为'):
##    if str(num)[0] == '1' and len(str(num)) == 11 and str(num).isdigit():
##        print(f"{num}是手机号")
##        print(f'手机是{phone}')
##    else:
##        print(f'{num}不是手机号')
##        print(f'手机是{phone}')

# 获取参数的顺序
# 必备->默认参数->不定长参数(*args->**kwargs)
# 指定传参(关键字实参) func(y=n,x=m)

# return    返回值
# 返回什么   变量接收到的就是什么   没有返回值时  变量接受的是None
# 函数中   renturn后面的代码  不会执行(表示函数结束了)
# def func(number):
#    num = number + 5
#    return num
#    print(111222333666)

# 函数的作用域
# 函数外面定义的变量为全局变量   函数里面只能访问  不能修改(看得见摸不着)
# 不能修改不可变类型
# 不可变   只能通过重新赋值改变的  字符串,整形,浮点型,布尔型,元祖
# 可变    可以在原本的基础上进行增删改查的   列表,集合,字典
# 函数里面定义的变量叫做局部变量   只能在函数里面访问
# global 声明函数外部的变量为全局变量  声明之后  就可以对这个变量进行修改

# x = 10
# def func():
#    global x
#    print(x)
#    x += 1
#    print(x)

# 嵌套函数
# nonlocal  变量名 声明外层函数中的变量为局部变量   嵌套函数
# 作用: 里面函数可以修改外层函数中的不可变类型变量
##def funa():
##    x = 1
##    def funb():
##        nonlocal x
##        x += 1
##        print(x)
##    return funb()
##funa()

# 闭包
# 外层函数返回内层函数的函数体
# 作用:用来保护 重要的数据(变量)   防止篡改数据
# def funa():
#    live = 50
#    def funb():
#        nonlocal live
#        live += 1
#        print(live)
#    def func():
#        nonlocal live
#        live -= 1
#        print(live)
#    return funb,func   #返回元祖   a = funa()  拆包:jia,jian = a

# 递归函数(回调函数):    函数自己调用自己
# def func(n):
#    if n <= 1:
#        return 1
#    else:
#        return n*func(n-1)
# a = func(5)
# print(a)

# 匿名函数
# 需要通过一个变量接收
# 匿名函数   通常搭配内置函数进行使用
##a = lambda x:x+1

def func(x):
   if x > 5:
       return x
# 过滤器(filter)
li = [1,3,5,6,7,9]
a = filter(func,li)
print(list(a))

##li = [1,3,5,6,7,9]
##print(list(filter(lambda x:x>5,li)))

# 回调函数
# 将一个函数的函数体当做一个函数的参数来使用
# def func1(f):
#     f()
#     print(111)
# def func2():
#     print(222)
# a = func1(func2)
