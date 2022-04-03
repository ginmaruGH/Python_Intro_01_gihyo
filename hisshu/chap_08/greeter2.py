# Chapter.08 関数
# ## 関数を定義する
# ### 関数に情報を渡す
print("\n### 関数に情報を渡す\n")

def greet_user(username):
    """シンプルなあいさつメッセージを出力する"""
    print(f"こんにちは、{username.title()}！")

greet_user('jesse')
