## Chapter10 ファイルと例外
### データを保存する
#### ユーザーが生成したデータを保存して読み込む

import json
print("\n#### ユーザーが生成したデータを保存して読み込む\n")

username = input("あなたのお名前は？ >> ")

filename = 'chap_10/username.json'

with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"戻ってきたときも、名前を覚えていますよ。{username}さん！")
