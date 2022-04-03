# Chapter.08 関数
# ## 実引数を渡す
# ### キーワード引数
print("\n### キーワード引数\n")

def describe_pet(animal_type, pet_name):
    """ペットについての情報を出力する"""
    print(f"\n私は、{animal_type}を飼っています。")
    print(f"{animal_type}の名前は、{pet_name.title()}です。")

describe_pet(animal_type='フェレット', pet_name='えーす')
describe_pet(pet_name='ウィリー', animal_type='いぬ')
