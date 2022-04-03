## Chapter10 ファイルと例外
### データを保存する
#### json.dump()とjson.load()を使用する

print("\n#### json.dump()とjson.load()を使用する\n")

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'chap_10/numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
