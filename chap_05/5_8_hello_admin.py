# 5-8.Hello Admin
print("\n# 5-8.Hello Admin\n")

usernames = ['taro', 'keiko', 'kenji', 'daikichi', 'admin']
for username in usernames:
    if username == 'admin':
        print("こんにちは admin、状況のレポートを見ますか？")
    else:
        print(f"こんにちは {username}、またログインしてくれてありがとう。")
