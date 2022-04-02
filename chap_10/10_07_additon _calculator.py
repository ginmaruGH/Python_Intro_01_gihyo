# 10-07.足し算の計算機

print("\n# 10-07.足し算の計算機\n")

print("終了するには、いつでも'q'を入力してください。")

while True:
    try:
        x = input("何か数字を入力してください。>> ")
        if x == 'q':
            break
        x = int(x)

        y = input("別の数字を入力してください。>> ")
        if y == 'q':
            break
        y = int(y)

    except ValueError:
        print("すみません。数字を入力してください。")

    else:
        sum = x + y
        print(f"{x}と{y}の合計は{sum}です。")

