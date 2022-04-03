# Chapter.09 クラス
# ## クラスをインポートする
# ### 1つのクラスをインポートする

from class_car import Car


print("\n### 1つのクラスをインポートする\n")

my_new_car = Car('audi', 'a4', '2019')
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
