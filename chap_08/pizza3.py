# Chapter.08 関数
# ## 任意の数の引数を渡す
# ### 位置引数と可変長引数を同時に使う
print("\n### 位置引数と可変長引数を同時に使う\n")

def make_pizza(size, *toppings):
    """注文されたピザの要約を出力する"""
    print(f"\n{size}インチのピザを、以下のトッピングで作ります。")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'ペパロニ')
make_pizza(12, 'マッシュルーム', 'ピーマン', 'エクストラチーズ')
