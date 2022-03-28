# Chapter.09 クラス
# ## クラスをインポートする
# ### モジュールの中にモジュールをインポートする

from class_car2 import Car
from class_electric_car import ElectricCar

print("\n### モジュールの中にモジュールをインポートする\n")

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
