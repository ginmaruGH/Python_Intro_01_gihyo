# Chapter.08 関数
# ## 実引数を渡す
# ### 位置引数
print("\n### 位置引数\n")

def describe_pet(animal_type, pet_name):
    """ペットについての情報を出力する"""
    print(f"\n私は、{animal_type}を飼っています。")
    print(f"{animal_type}の名前は、{pet_name.title()}です。")

describe_pet('フェレット', 'えーす')
describe_pet('いぬ', 'ウィリー')
