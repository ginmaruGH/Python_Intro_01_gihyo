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


my_dog = Dog('ウィリー', 6)

# 属性にアクセスする
print("\n# 属性にアクセスする")
print(f"私のイヌの名前は、{my_dog.name}です。")
print(f"私のイヌは、{my_dog.age}歳です。")

# メソッドを呼び出す
print("\n# メソッドを呼び出す")
my_dog.sit()
my_dog.roll_over()
