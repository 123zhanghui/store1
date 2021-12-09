import time

"""
分析一个水杯的属性和功能，使用类描述并创建对象
高度，容积，颜色，材质
能存放液体
"""
all_material = ["木材", "塑料", "不锈钢", "陶瓷", "玻璃"]


class Cup:
    __high = 0.0  # 1高度
    __volume = 0.0  # 容积
    __color = ""  # 颜色
    __material = ""  # 材质

    def set_high(self, high):  # 设定高度
        if high > 35 or high < 15:
            print("高度不合规")
        else:
            self.__high = high

    def get_high(self):  # 1获取高度
        return self.__high

    def set_volume(self, volume):  # 设定容积
        if volume > 800 or volume < 300:
            print("容积不合规")
        else:
            self.__volume = volume

    def get_volume(self):  # 获取容积
        return self.__volume

    def set_color(self, color):  # 设定颜色
        if color == "":
            print("颜色不能为空")
        else:
            self.__color = color

    def get_color(self):  # 获取颜色
        return self.__color

    def set_material(self, material):  # 设定材质
        if material in all_material:
            self.__material = material
        else:
            print("材质不合规")

    def get_material(self):  # 获取材质
        return self.__material

    def save(self):
        print("可以装", self.__volume, "ml的水")

    def show(self):
        print("高度：", self.__high, "，容积：", self.__volume, "ml，颜色：", self.__color, "，材质：", self.__material)


C = Cup()

C.set_high(20)
C.set_volume(500)
C.set_color("白色")
C.set_material("玻璃")

C.save()
C.show()
print(C.get_material())
