# Chapter.08 関数
# ## リストを受け渡す
# ###
print("\n## リストを受け渡す\n")

def greet_users(names):
    """リストの各ユーザーに対して、シンプルなあいさつを出力する"""
    for name in names:
        msg = f"こんにちは、{name.title()}！"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
