# Chapter.09 クラス
# ## クラスをインポートする
# ### モジュールに複数のクラスを格納する

from class_car2 import ElectricCar

print("\n### モジュールに複数のクラスを格納する\n")

my_tesla = ElectricCar('tesla', 'model S', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
