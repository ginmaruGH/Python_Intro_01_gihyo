# 9-12.複数のモジュール

from admin import Admin

print("\n# 9-12.複数のモジュール\n")

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
