## Chapter10 ファイルと例外
### データを保存する
#### ユーザーが生成したデータを保存して読み込む

print("\n#### ユーザーが生成したデータを保存して読み込む\n")

# 以前に保存されたユーザー名があれば読み込む
# 見つからない場合、ユーザー名の入力を促し保存する

import json


filename = 'chap_10/username.json'

try:
    with open(filename) as f:
        username = json.load(f)

except FileNotFoundError:
    username = input("あなたのお名前は？ >> ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"戻ってきたときも、名前を覚えていますよ。{username}さん！")

else:
    print(f"おかえりなさい。{username}さん！")
