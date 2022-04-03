# 9-02.3軒のレストラン

class Restaurant:
    """レストランを表すクラス"""

    def __init__(self,name, cuisine_type):
        """レストランを初期化する"""
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """レストランについての情報を出力する"""
        msg = f"{self.name}は、素晴らしい{self.cuisine_type}を提供します。"
        print(f"\n{msg}")

    def open_restaurant(self):
        """レストランが開店したことを知らせるメッセージを出力する"""
        msg = f"{self.name}が開店しました。ぜひご来店ください!"
        print(f"\n{msg}")


print("\n# 9-02.3軒のレストラン\n")

restaurant = Restaurant('malaychan', '東南アジア料理')
restaurant.describe_restaurant()

restaurant = Restaurant('もうやん', 'カレーライス')
restaurant.describe_restaurant()

restaurant = Restaurant('かるかや', 'うどん')
restaurant.describe_restaurant()

