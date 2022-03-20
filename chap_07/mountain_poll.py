# Chapter.07 ユーザー入力とwhileループ
# ## ユーザーの入力から辞書を作る
print("\n## ユーザーの入力から辞書を作る\n")

responses = {}

# 投票がアクティブなことを示すフラグをセットする
polling_active = True

while polling_active:
    # 入力プロンプトで名前と回答を受け付ける
    name = input("\nあなたのお名前は？ >> ")
    response = input("いつか登りたい山はどこですか？ >> ")

    # 回答を辞書に保存する
    responses[name] = response

    # 誰かほかに投票する人がいるかどうか確認する
    repeat = input("誰かほかに回答してくれる人はいますか？（yes/no）>> ")
    if repeat == 'no':
        polling_active = False
# 投票を終了し、結果を表示する
print("\n--- 投票結果 ---\n")
for name, response in responses.items():
    print(f"{name}さんが登りたい山は、{response}です。")
