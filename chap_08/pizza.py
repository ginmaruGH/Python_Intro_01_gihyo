# Chapter.08 関数
# ## 任意の数の引数を渡す
# ###
print("\n## 任意の数の引数を渡す\n")

def make_pizza(*toppings):
    """注文されたトッピングの一覧を出力する"""
    print(toppings)

make_pizza('ペパロニ')
make_pizza('マッシュルーム', 'ピーマン', 'エクストラチーズ')
