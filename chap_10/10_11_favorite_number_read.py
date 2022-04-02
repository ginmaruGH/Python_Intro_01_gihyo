# 10-11.好きな数字（読み込み）

print("\n# 10-11.好きな数字（読み込み）\n")

import json

filename = 'chap_10/10_11_favorite_number.json'

with open(filename) as f:
    number = json.load(f)

print(f"あなたが好きな数字を知っています！それは、{number}です。")
