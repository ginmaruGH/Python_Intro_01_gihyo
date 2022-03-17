# 6-07.人々
print("\n# 6-07.\n")

# 空のリストを作成
people = []

# 人の辞書を作成してリストに追加する
person = {
    'first_name': 'せぶん',
    'last_name': '鈴木',
    'age': 49,
    'city': '東京',
    }
people.append(person)
person = {
    'first_name': 'いれぶん',
    'last_name': '鈴木',
    'age': 50,
    'city': '東京',
    }
people.append(person)
person = {
    'first_name': 'ふぁみま',
    'last_name': '鈴木',
    'age': 40,
    'city': '東京',
    }
people.append(person)

# 辞書の全情報を出力する
for person in people:
    name = f"{person['last_name']}{person['first_name']}"
    age = person['age']
    city = person['city'].title()
    print(f"{name}は、{city}に住んでおり{age}歳です。")
