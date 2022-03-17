# 5-10.Cheking Usernames
print("\n# 5-10.ユーザー名を確認する\n")

current_users = ['taro', 'keiko', 'kenji', 'daikichi', 'admin']
new_users = ['chukichi', 'Keiko', 'perter', 'angela', 'naomi']
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:

        print(f"すみません。「{new_user}」は、すでに使用されています。")
    else:
        print(f"よかった。 「{new_user}」は、利用可能です。")
