# if-elif-else文
print("\nif-elif-else文\n")

age = 12
print(f"age: {age}")
if age < 4:
    print("入場料は無料です。")
elif age < 18:
    print("入場料は2,500円です。")
else:
    print("入場料は4,000円です。")

# コード修正
age = 18
print(f"age: {age}")
if age < 4:
    price = 0
elif age < 18:
    price = 2500
else:
    price = 4000
print(f"入場料は{price}円です。")

# 複数のelifブロックを使用する
print("\n複数のelifブロックを使用する\n")

age = 64
print(f"age: {age}")
if age < 4:
    price = 0
elif age < 18:
    price = 2500
elif age < 65:
    price = 4000
else:
    price = 2000
print(f"入場料は{price}円です。")

# elseブロックの省略
print("\nelseブロックの省略\n")

age = 65
print(f"age: {age}")
if age < 4:
    price = 0
elif age < 18:
    price = 2500
elif age < 65:
    price = 4000
elif age >= 65:
    price = 2000
print(f"入場料は{price}円です。")
