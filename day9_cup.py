import time

"""
有笔记本电脑（屏幕大小，价格，cpu型号，内存大小，待机时长），行为（打字，打游戏，看视频）
"""
all_screen_size = [14.1, 15, 17, 19, 21, 22.1, 23, 24, 27, 29]
all_memory_size = [2, 3, 4, 8]


class Computer:
    __screen_size = 0.0  # 1屏幕大小
    __money = 0.0  # 价格
    __cpu_type = ""  # cpu型号
    __memory_Size = 0  # 内存大小
    __stand_by_time = 0.0  # 待机时长

    def set_screen_size(self, screen_size):  # 屏幕大小
        if screen_size in all_screen_size:
            self.__screen_size = screen_size
        else:
            print("屏幕大小不合规")

    def get_screen_size(self):  # 1屏幕大小
        return self.__screen_size

    def set_money(self, money):  # 设定价格
        if money > 50000 or money < 300:
            print("价格不合规")
        else:
            self.__money = money

    def get_money(self):  # 获取价格
        return self.__money

    def set_cpu_type(self, cpu_type):  # 设定cpu型号
        if cpu_type == "":
            print("cpu型号不能为空")
        else:
            self.__cpu_type = cpu_type

    def get_cpu_type(self):  # 获取cpu型号
        return self.__cpu_type

    def set_memory_size(self, memory_size):  # 屏幕大小
        if memory_size in all_memory_size:
            self.__memory_size = memory_size
        else:
            print("屏幕大小不合规")
    def get_memory_size(self):  # 1屏幕大小
        return self.__memory_size

    def set_stand_by_time(self, stand_by_time):  # 设定待机时长
        if stand_by_time > 300 or stand_by_time < 1:
            print("待机时长不合规")
        else:
            self.__stand_by_time = stand_by_time

    def get_stand_by_time(self):  # 获取待机时长
        return self.__stand_by_time

    def write(self, software):  # 打字
        print("可以用", software, "进行打字")

    def play_game(self, game_name):  # 打游戏
        print("打游戏,例如：", game_name)

    def video(self, video_name):  # 看视频
        print("看视频,例如：", video_name)

    def show(self):
        print("屏幕大小：", self.__screen_size,
              "，价格", self.__money,
              "，cpu型号：", self.__cpu_type,
              "，内存大小：", self.__memory_Size,
              "，待机时长：", self.__stand_by_time)


C = Computer()

C.set_screen_size(15)
C.set_money(5000)
C.set_cpu_type("锐龙")
C.set_memory_size(4)
C.set_stand_by_time(10)

C.write("【金山打字】")
C.play_game("英雄联盟")
C.video("开国大典")
C.show()
print(C.get_stand_by_time())
