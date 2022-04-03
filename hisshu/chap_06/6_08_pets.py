# 6-8.ペット
print("\n# 6-8.ペット\n")

# ペットの情報を格納する空のリストを作成する
pets = []

# ペットの情報を作成してリストに追加する
pet = {
    'animal type': 'フェレット',
    'name': 'igeey',
    'owner': 'mageey',
    'eats': 'ferret food',
}
pets.append(pet)
pet = {
    'animal type': 'うさぎ',
    'name': 'inaban',
    'owner': 'inaba',
    'eats': 'grass',
}
pets.append(pet)

# 各ペットの情報を出力する
for pet in pets:
    print(f"\n{pet['name']}についての情報です。")
    for key, value in pet.items():
        print(f"\t{key}: {value}")
