# Chapter.09 クラス
# ## クラスを作成して使用する
# ### イヌのクラスを作成する

class Dog:
    """イヌをモデル化したシンプルな実装例"""

    def __init__(self, name, age):
        """名前と年齢の属性を初期化する"""
        self.name = name
        self.age = age

    def sit(self):
        """イヌに「おすわり」の命令を実行する"""
        print(f"{self.name}は、おすわりしている。")

    def roll_over(self):
        """イヌに「ごろーん」の命令を実行する"""
        print(f"{self.name}は、ごろーんした！")
