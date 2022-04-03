# 7-2.レストランの席
print("\n# 7-2.レストランの席\n")

party_size = input("今晩のディナーには、何人参加しますか？")
party_size = int(party_size)

if party_size >= 8:
    print("すみません。席につくまで少しお待ち下さい。")
else:
    print("テーブルの準備はできています。")

