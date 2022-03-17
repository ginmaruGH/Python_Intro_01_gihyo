# 5-1. 条件テスト
print("\n5-1. 条件テスト\n")

car = 'subaru'
print("car == 'subaru'の結果を True と予測します。")
print(car == 'subaru')

print("\ncar == 'audi'の結果を False と予測します。")
print(car == 'audi')

answer = 17
print("\nanswer == 17 の結果を True と予測します。")
print(answer == 17)
print("\nanswer == 42 の結果を False と予測します。")
print(answer == 42)

age = 35
print("\nage < 40 の結果を True と予測します。")
print(age < 40)
print("\nage >= 42 の結果を False と予測します。")
print(age >= 42)

print("\nage < 22 or age < 40 の結果を True と予測します。")
print(age < 20 or age < 40)
print("\nage < 22 and age < 40 の結果を False と予測します。")
print(age < 22 and age < 40)

pets = ['イヌ', 'ネコ', 'フェレット']
print("\n'フェレット' in pets の結果を True と予測します。")
print('フェレット' in pets)
print("\n'フェレット' not in pets の結果を False と予測します。")
print('フェレット' not in pets)
