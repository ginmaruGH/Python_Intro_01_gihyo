## Chapter10 ファイルと例外
### データを保存する
#### ユーザーが生成したデータを保存して読み込む

import json
print("\n#### ユーザーが生成したデータを保存して読み込む\n")

filename = 'chap_10/username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"おかえりなさい。{username}さん！")
