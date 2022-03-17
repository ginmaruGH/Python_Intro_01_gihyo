# リストとif文を使用する
from zoneinfo import available_timezones


print("\nリストとif文を使用する\n")

# 特別な要素を確認する
print("\n# 特別な要素を確認する")
requested_toppings = ['マッシュルーム', 'ピーマン', 'エクストラチーズ']
for requested_topping in requested_toppings:
    print(f"ピザに{requested_topping}を追加します。")
print("ピザができました。")

# ピーマンが品切れの場合
print("\n# ピーマンが品切れの場合")
requested_toppings = ['マッシュルーム', 'ピーマン', 'エクストラチーズ']
for requested_topping in requested_toppings:
    if requested_topping == 'ピーマン':
        print("申し訳ありません。ピーマンは品切れです。")
    else:
        print(f"ピザに{requested_topping}を追加します。")
print("ピザができました。")

# リストが空でないことを確認する
print("\n# リストが空でないことを確認する")
requested_toppings = []
# requested_toppings = ['マッシュルーム', 'ピーマン', 'エクストラチーズ']
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"ピザに{requested_topping}を追加します。")
    print("ピザができました。")
else:
    print("プレーンピザでよろしいですか？")

# 複数のリストを使用する
print("\n# 複数のリストを使用する")
available_toppings = [
    'マッシュルーム', 'オリーブ', 'ピーマン',
    'ペパロニ', 'パイナップル', 'エクストレチーズ']
requested_toppings = ['マッシュルーム', 'フライドポテト', 'エクストレチーズ']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"ピザに{requested_topping}を追加します。")
    else:
        print(f"申し訳ありません。{requested_topping}はありません。")
print("ピザができました。")

