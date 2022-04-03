# Chapter.08 関数
# ## 関数をモジュールに格納する
# ### モジュール全体をインポートする
# print("\n### モジュール全体をインポートする\n")

def make_pizza(size, *toppings):
    """注文されたピザの要約を出力する"""
    print(f"\n{size}インチのピザを、以下のトッピングで作ります。")
    for topping in toppings:
        print(f"- {topping}")
