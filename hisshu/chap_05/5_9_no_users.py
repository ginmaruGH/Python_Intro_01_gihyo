# 5-9.no user
print("\n# 5-9.No User\n")

usernames = []
if usernames:
    for username in usernames:
        if username == 'admin':
            print("こんにちは admin、状況のレポートを見ますか？")
        else:
            print(f"こんにちは {username}、またログインしてくれてありがとう。")
else:
    print("ユーザー募集中です。")

