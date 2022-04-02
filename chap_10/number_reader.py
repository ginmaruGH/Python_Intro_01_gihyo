## Chapter10 ファイルと例外
### データを保存する
#### json.dump()とjson.load()を使用する

print("\n#### json.dump()とjson.load()を使用する\n")

import json

filename = 'chap_10/numbers.json'
with open(filename) as f:
    numbers = json.load(f)

print(numbers)
