# Chapter.07 ユーザー入力とwhileループ
# ## 剰余演算子 %
print("\n## 剰余演算子 %\n")

number = input("何か数を入力してください。奇数が偶数かを判定します。 >> ")
number = int(number)

if number % 2 == 0:
    print(f"\n数{number}は、偶数です。")
else:
    print(f"\n数{number}は、奇数です。")
