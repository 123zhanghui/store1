'''
任务：如果键盘输入大于随机数弹出友好提示信息“猜大了”，"猜小了"
'''
import random
#   随机生成数字  （开始int，结束int）  []
i=0
while i<=14:
    Ran = random.randint(1, 20)
    print(Ran)
    money = 5000
    num=input("请输入一个数字")
    num=int(num)

    if num > Ran:
        print("猜大了")
        money=money-100
        print(money)
        i=i+1
        print("猜错",i,"次")
    elif num<Ran:
        print("猜小了")
        money=money-100
        print(money)
        i=i+1
        print("猜错",i,"次")
    else:
        print("猜对了")
        money=money+300
        print(money)
