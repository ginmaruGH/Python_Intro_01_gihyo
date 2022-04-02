# 10-12.好きな数字を記憶する

print("\n# 10-12.好きな数字を記憶する\n")

import json

filename = 'chap_10/10_12_favorite_number.json'

try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    number = input("好きな数字は何ですか？ >> ")
    with open(filename, 'w') as f:
        json.dump(number , f)
        print(f"ありがとうございます。{number}を覚えておきます。")
else:
    print(f"あなたの好きな数字を知っています！それは、{number}です。")
