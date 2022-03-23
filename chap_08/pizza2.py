# Chapter.08 関数
# ## 任意の数の引数を渡す
# ###
print("\n## 任意の数の引数を渡す\n")

def make_pizza(*toppings):
    """注文されたピザの要約を出力する"""
    print("\n以下のトッピングのピザを作ります。")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('ペパロニ')
make_pizza('マッシュルーム', 'ピーマン', 'エクストラチーズ')
