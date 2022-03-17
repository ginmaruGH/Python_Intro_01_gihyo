guests = ["guido van rossum", "ewa jodlowska", "naomi ceder"]

name = guests[0].title()
print(f"{name}さん、ぜひ夕食に来てください。")
name = guests[1].title()
print(f"{name}さん、ぜひ夕食に来てください。")
name = guests[2].title()
print(f"{name}さん、ぜひ夕食に来てください。")

# 参加できなくたったゲストの表示
name = guests[1].title()
print(f"すみません。{name}さんが夕食に参加できなくなりました。")


# Ewaさんの替わりにCoryさんを招待します
del guests[1]
guests.insert(1, "cory altthoff")

# 彩度、招待メッセージを取得する
name = guests[0].title()
print(f"{name}さん、ぜひ夕食に来てください。")
name = guests[1].title()
print(f"{name}さん、ぜひ夕食に来てください。")
name = guests[2].title()
print(f"{name}さん、ぜひ夕食に来てください。")

# 大きなテーブルを見つけたので、追加のゲストを招待する
print("\n大きなテーブルを見つけた！")
guests.insert(0, 'iqbal abdullah')
guests.insert(2, 'younggun kim')
guests.append('jung yu cheng')

name = guests[0].title()
print(f"{name}さん、ぜひ夕食に来てください。")

name = guests[1].title()
print(f"{name}さん、ぜひ夕食に来てください。")

name = guests[2].title()
print(f"{name}さん、ぜひ夕食に来てください。")

name = guests[3].title()
print(f"{name}さん、ぜひ夕食に来てください。")

name = guests[4].title()
print(f"{name}さん、ぜひ夕食に来てください。")

name = guests[5].title()
print(f"{name}さん、ぜひ夕食に来てください。")
