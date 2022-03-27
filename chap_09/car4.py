# Chapter.09 クラス
# ## クラスとインスタンスを操作する
# ### 属性にデフォルト値を設定する

class Car:
    """自動車を表すシンプルな実装例"""

    def __init__(self, make, model, year):
        """自動車の特徴となる属性を初期化する"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """フォーマットされた名前を返す"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """自動車の走行距離を出力する"""
        print(f"走行距離は、{self.odometer_reading}kmです。")

    def update_odometer(self, km):
        """
        指定された値に走行距離を更新する。
        走行距離を減らそうとする処理は拒否します。
        """
        if km >= self.odometer_reading:
            self.odometer_reading = km
        else:
            print("走行距離は減らせません！")


my_new_car = Car('audi', 'a4', '2019')
print(my_new_car.get_descriptive_name())

# メソッドを通して、値を変更する
my_new_car.update_odometer(24)
my_new_car.read_odometer()
