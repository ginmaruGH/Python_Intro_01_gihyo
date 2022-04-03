# Chapter.09 クラス
# ## クラスをインポートする
# ### モジュールから複数のクラスをインポートする

from class_car2 import Car, ElectricCar

print("\n### モジュールから複数のクラスをインポートする\n")

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
