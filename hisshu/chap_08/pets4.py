# Chapter.08 関数
# ## 実引数を渡す
# ### 関数を同じように呼び出す
print("\n### 関数を同じように呼び出す\n")

def describe_pet(pet_name, animal_type='イヌ'):
    """ペットについての情報を出力する"""
    print(f"\n私は、{animal_type}を飼っています。")
    print(f"{animal_type}の名前は、{pet_name.title()}です。")

# イヌの名前はウィリー
describe_pet('ウィリー')
describe_pet(pet_name='ウィリー')

# フェレットの名前はえーす
describe_pet('えーす', 'フェレット')
describe_pet(pet_name='えーす', animal_type='フェレット')
describe_pet(animal_type='フェレット', pet_name='えーす')

# describe_pet()
