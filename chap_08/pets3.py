# Chapter.08 関数
# ## 実引数を渡す
# ### デフォルト値
print("\n### デフォルト値\n")

def describe_pet(pet_name, animal_type='イヌ'):
    """ペットについての情報を出力する"""
    print(f"\n私は、{animal_type}を飼っています。")
    print(f"{animal_type}の名前は、{pet_name.title()}です。")

describe_pet(pet_name='ウィリー')
describe_pet(animal_type='フェレット', pet_name='えーす')
