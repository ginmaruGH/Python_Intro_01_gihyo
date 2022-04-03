# 9-13.サイコロ

from random import randint


class Dice:
    """サイコロを表すクラス"""

    def __init__(self, sides=6):
        """サイコロを初期化する"""
        self.sides = sides

    def roll_dice(self):
        """サイコロの出た目（1~面の数）を返す"""
        return randint(1, self.sides)


print("\n# 9-13.サイコロ\n")

count = 10

# 6面のサイコロを作成して、10回振った結果を出力する
d6 = Dice()

results = []
for roll_num in range(count):
    result = d6.roll_dice()
    results.append(result)
print("- 6面のサイコロを10回振った結果")
print(results)

# 10面のサイコロを作成して、10回振った結果を出力する
d10 = Dice(sides=10)

results = []
for roll_num in range(count):
    result = d10.roll_dice()
    results.append(result)
print("\n- 10面のサイコロを10回振った結果")
print(results)

# 20面のサイコロを作成して、10回振った結果を出力する
d20 = Dice(sides=20)

results = []
for roll_num in range(count):
    result = d20.roll_dice()
    results.append(result)
print("\n- 20面のサイコロを10回振った結果")
print(results)
