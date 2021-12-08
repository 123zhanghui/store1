'''
字典开发
1.编程实现：仔细业务之间的包含关系，并完成以下编程需求，要适当提高代码的可复用性。
a)用户：账号（str：系统随机产生8位数字）、姓名(str)、密码(int:6位数字)、地址、存款余额(int)、开户行（银行的名称（str））写死的！
b)地址：国家(str)、省份(str)、街道(str)、门牌号(str)
c)银行：能存储100用户的库(字典)、本银行名称（比如：中国工商银行的昌平支行,str）

i.银行业务功能
1.添加用户（传入参数：用户的所有信息。返回值：整型值（1：成功，2：用户已存在，3：用户库已满））
a)业务逻辑：
先检查该用户的账号在库里是否存在。若不存在则在用户库里添加一个该用户并返回代号1
若存在则返回代号2。另外在添加用户的时候检测用户库是否已注册满，若已满则返回代号3
'''
# import random
from random import randint
from DBUtils import update
from DBUtils import select

bank={}
bank_name = "中国工商银行"
print("==================")
print("|   中国工商银行   |")
print("==================")
print("|1、开户          |")
print("|2、存钱          |")
print("|3、取钱          |")
print("|4、转账          |")
print("|5、查询          |")

# # bank={'Frank': {'account': 29073386, 'password': '123456', 'country': '中国', 'province': '山东', 'street': '1大街', 'door': '001', 'bank_name': '中国工商银行', 'money': 0}
def useradd():  # 定义方法————用来添加用户的
    account_number = randint(1000000, 99999999)
    username = input("请输入您的姓名")
    password = input("请输入您的密码")
    country = input("\t\t请输入您的国家")  # \t表示一个tab
    province = input("\t\t请输入您的省份")
    street = input("\t\t请输入你的街道")
    door = input("\t\t请输入您的门牌号")
    money=int(input("请输入您的初始金额"))
    gift = bankadd(username)  # 位置对应
    if gift == "1":
        sql2 = "insert into usermessage values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        param2 = [account_number,username,password,country,province,street,door,bank_name,money]
        update(sql2, param2)

        sql16 = "select * from usermessage where username= %s"
        param16 = [username]
        data = select(sql16, param16)
        for i in data:
            print(i)
        print("开户成功,以上是您的详细信息")
    elif gift == "2":
        print("用户已存在")
    elif gift == "3":
        print("数据库已满")


def bankadd(username):

    sql1 = "select * from usermessage where username = %s"# 姓名在不在bank的键里
    param1 = [username]#c参数
    data1 = select(sql1, param1)
    if len(data1) > 0:
        return "2"

    sql = "select count(*) from usermessage"  # (5)
    param = []#c参数
    data = select(sql, param)
    if len(data) >= 100:
        return "3"
    else:
        return "1"


'''2.存钱（传入值：用户的账号、存取的金额。返回值：布尔类型值）
a)业务逻辑：
先根据传入的账号信息查询用户库里是否有该用户。若没有则返回False
若有，则将该用户的金额存进去。
'''
def save():
    username = input("请输入用户名")
    savemoney = int(input("请输入存款金额"))
    gift = saveadd(username)  # 位置对应
    if gift == "True":
        sql3 = "update usermessage set money = money + %s where username = %s  "
        param3 = [savemoney, username]
        update(sql3, param3)
        print("存款",savemoney)
    elif gift == "False":
        print("用户不存在")

def saveadd(username):
    sql2 = "select * from usermessage where username = %s"
    param2 = [username]
    data2 = select(sql2, param2)
    if len(data2) > 0:
        return "True"
    else:
        return "False"

'''
3.取钱（传入值：用户的账号，用户密码，取钱金额。返回值：整型值（0：正常，1：账号不存在，2：密码不对，3：钱不够））
a)业务逻辑：
先根据账号信息来查询该用户是否存在，若不存在，则返回代号1，
若存在，则继续判断密码是否正确，若不正确，则返回代号2。
若账号密码都正确，则继续判断当前用户的金额是否满足要取出的钱，若不满足，则返回代号3，
若满足，则将该用户的金额减去。
'''
def get():
    username = input("请输入用户名")
    password = input("请输入密码")
    getmoney = int(input("请输入取款金额"))
    gift = gets(username, password, getmoney)  # 位置对应
    if gift == "0":
        print("取款成功")
    elif gift == "1":
        print("账户不存在")
    elif gift == "2":
        print("密码不对")
    elif gift == "3":
        print("钱不够")


def gets(username, password, getmoney):
    sql6 = "select * from usermessage where username = %s"
    param6 = [username]
    data6 = select(sql6, param6)
    if len(data6) > 0:#用户是否存在
        sql7 = "select * from usermessage where password = %s and username = %s "
        param7 = [password, username]
        data7 = select(sql7, param7)
        if len(data7) > 0:#用户、密码是否存在
            sql8 = "select * from usermessage where money > %s and username = %s"
            param8 = [getmoney, username]
            data8 = select(sql8, param8)
            if len(data8) > 0:#金额条件满足
                sql9 = "update usermessage  set money = money - %s  where username = %s"
                param9 = [getmoney, username]
                data=update(sql9, param9)
                # print(data.cell_value(1, 1))
                return "0"
            else:
                return "3"
        else:
            return "2"
    else:  # 姓名在不在bank的键里
        return "1"


'''
4.转账（传入值：转出的账号，转入的账号，转出账号的密码，转出的金额。返回值：0：正常，1：账号不对，2密码不对，3钱不够）
a)业务逻辑：
先查询用户库是否存在转出和转入的账号，若不存在则返回代号,1，
若账号都存在则继续判断转出账号的密码是否正确，若不正确，则返回2，
若正确则继续判断要转出的金额是否足够，若不够则返回3，
否则正常转出，转出的账号用户金额要相对应的减少，转入的金额相对应的增加。
'''
def transfer():
    username_in = input("请输入转入的用户名")
    username_out = input("请输入转出的用户名")
    password_out = input("请输入转出的密码")
    money_out = int(input("请输入转出的金额"))
    gift = transfers(username_in, username_out, password_out, money_out)  # 位置对应

    if gift == "0":
        sql14 = "update usermessage set money = money - %s where username = %s"
        param14 = [money_out, username_out]
        update(sql14, param14)

        sql15 = "update usermessage set money = money + %s where username = %s"
        param15 = [money_out, username_in]
        update(sql15, param15)
       # bank[username_out]["money"] = bank[username_out]["money"] - money_out
       # information_out = '''转出账户余额：%s'''
       # print(information_out % (bank[username_out]["money"]))
       #
       # bank[username_in]["money"] = bank[username_in]["money"] + money_out
       # information_in = '''转入账户余额：%s'''
       # print(information_in % (bank[username_in]["money"]))
    elif gift == "1":
        print("账户不存在")
    elif gift == "2":
        print("密码不对")
    elif gift == "3":
        print("钱不够")


def transfers(username_in, username_out, password_out, money_out):
    sql10="select * from usermessage where username = %s "
    param10=[username_out]
    data10=select(sql10,param10)
    if len(data10)>0:#用户名
        sql11 = "select * from usermessage where username = %s "
        param11 = [username_in]
        data11 = select(sql11, param11)
        if len(data11) > 0:#用户名
            sql12="select * from usermessage where password = %s and username = %s "
            param12=[password_out,username_out]
            data12=select(sql12,param12)
            if len(data12) > 0:#用户名、密码
                sql13 = "select * from usermessage where money > %s and username = %s"
                param13 = [money_out, username_out]
                data13 = select(sql13, param13)
                if len(data13) > 0:#金额
                    return "0"
                else:
                    return "3"
            else :
                return "2"
        else:
            return "1"
    else:
        return "1"

'''5.查询账户功能（传入值：账号，账号密码，返回值：空）
a)业务逻辑：
先根据账号判断用户库是否存在该用户，若不存在则打印提示信息：该用户不存在。
否则继续判断密码是否正确。若不正确则打印相对应的错误信息。
若账号和密码都正确，则将该用户的信息都打印出来，比如：当前账号：xxxx,密码:xxxxxx,余额：xxxx元，用户居住地址：xxxxxxxxxxxxx，当前账户的开户行：xxxxxxxxxx.
d)界面类：在执行该入口程序时，就打印银行业务选择菜单：比如：
i.
ii.然后就开始处理各种输入操作，直到业务处理完成!'''
def query():
    username = input("请输入用户名")
    password = input("请输入密码")
    gift = querys(username, password)  # 位置对应
    if gift == "0":
        print("查询成功,以上是您的详细信息")
        # information = '''
        #         --------工商银行-------
        #             1、账号：%s
        #             2、姓名：%s
        #             3、密码：******
        #             4、国家：%s
        #             5、省份：%s
        #             6、街道：%s
        #             7、门牌：%s
        #             8、余额：%s
        #         '''
        # print(information % (bank[username]["account_number"], username, bank[username]["country"], bank[username]["province"], bank[username]["street"],bank[username]["door"] , bank[username]["money"]))
    elif gift == "1":
        print("账户不存在")
    elif gift == "2":
        print("密码不对")

def querys(username, password):
    sql4 = "select * from usermessage where username = %s "
    param4 = [username]
    data4 = select(sql4, param4)#账户
    if len(data4) > 0:
        sql5 = "select * from usermessage where password = %s "
        param5 = [password]
        data5 = select(sql5, param5)
        if len(data5) > 0:#账户、密码
            for i in data4:
                print(i)
                return "0"
        else:
            return "2"
    else:
        return "1"



while True:
    business = input("请输入业务编号")
    if business == "1":
        print("1、开户")
        useradd()
    elif business == "2":
        print("2、存钱")
        save()
    elif business == "3":
        print("3、取钱")
        get()
    elif business == "4":
        print("4、转账")
        transfer()
    elif business == "5":
        print("5、查询")
        query()
