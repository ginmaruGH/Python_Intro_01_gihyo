# 値がリストに存在しないことを確認する

print("\n値がリストに存在しないことを確認する\n")
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}はコメントを書き込めます。")

