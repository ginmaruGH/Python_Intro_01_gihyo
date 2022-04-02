# 10-11.好きな数字（書き込み）

print("\n# 10-11.好きな数字（書き込み）\n")

import json

filename = 'chap_10/10_11_favorite_number.json'

number = input("好きな数字は何ですか？ >> ")
with open(filename, 'w') as f:
    json.dump(number, f)
    print(f"ありがとうございます。{number}を覚えておきます。")
