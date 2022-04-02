# 10-06.足し算

print("\n# 10-06.足し算\n")

try:
    x = input("何か数字を入力してください。>> ")
    x = int(x)

    y = input("別の数字を入力してください。>> ")
    y = int(y)
except ValueError:
    print("すみません。数字を入力してください。")
else:
    sum = x + y
    print(f"{x}と{y}の合計は{sum}です。")

