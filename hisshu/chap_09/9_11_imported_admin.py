# 9-11.インポートされた管理者

from user import Admin

print("\n# 9-11.インポートされた管理者\n")

tanji = Admin('tanjiro', 'kamado', 'tanji', 'tanji@example.com', 'chiyoda')
tanji.describe_user()

tanji.privileges.show_privileges()

print("\n権限を追加します。")
tanji_privileges = [
    "投稿を追加する",
    "投稿を削除する",
    "ユーザーを利用禁止にする",
]
tanji.privileges.privileges = tanji_privileges
tanji.privileges.show_privileges()
