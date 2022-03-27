# Chapter.09 クラス
# ## クラスとインスタンスを操作する
# ### 自動車のクラス

class Car:
    """自動車を表すシンプルな実装例"""

    def __init__(self, make, model, year):
        """自動車の特徴となる属性を初期化する"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """フォーマットされた名前を返す"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


my_new_car = Car('audi', 'a4', '2019')
print(my_new_car.get_descriptive_name())
