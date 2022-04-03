# 8-15.モデルを印刷する
from printing_functions import print_models, show_completed_models

print("\n# 8-15.モデルを印刷する\n")

# 印刷したいデザインのリストを作成する
unprinted_designs = ['iPhoneケース', 'ロボットのペンダント', '12面体']
completed_models = []

# 各関数を呼び出す
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
