# 8-15.モデルを印刷する
# 8_15_printing_models.pyから呼び出される

def print_models(unprinted_designs, completed_models):
    """
    リストからなくなるまでデザインを3D印刷する
    各デザインは印刷後、completed_modelsに移動する
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"3D印刷中: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """3D印刷されたすべてのモデルの情報を出力する"""
    print("\n以下のモデルが3D印刷されました。")
    for completed_model in completed_models:
        print(completed_model)



