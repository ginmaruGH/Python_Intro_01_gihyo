# 単純なif文
print("\n単純なif文\n")

age = 19
print(f"age: {age}")
if age >= 18:
    print("選挙権がある年齢です。")
    print("投票はしましたか？")

# if-else文
print("\nif-else文\n")

age = 17
print(f"age: {age}")
if age >= 18:
    print("選挙権がある年齢です。")
    print("投票はしましたか？")
else:
    print("もし訳ありません。投票するには若すぎるようです。")
    print("18歳になったら、投票してください。")
