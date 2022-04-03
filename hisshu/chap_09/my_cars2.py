# Chapter.09 クラス
# ## クラスをインポートする
# ### モジュール全体をインポートする

import class_car2

print("\n### モジュール全体をインポートする\n")

my_beetle = class_car2.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = class_car2.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
