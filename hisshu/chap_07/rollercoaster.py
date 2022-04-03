# Chapter.07 ユーザー入力とwhileループ
# ## int()関数を使用して数値を受け取る
print("\n## int()関数を使用して数値を受け取る\n")

height = input("身長は何cm？")
height = int(height)

if height >= 90:
    print("\n乗ってもよいですよ！")
else:
    print("\nもうちょっと大きくなったらね。")
