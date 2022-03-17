# リストをコピーする
print("\nリストをコピーする\n")

my_foods = ["ピザ", "だんご", "ケーキ"]
friend_foods = my_foods[:]

print("私が好きな食べ物")
print(my_foods)
print("友達が好きな食べ物")
print(my_foods)

# リストに追加
print("\nそれぞれのリストに食べ物を追加")
my_foods.append("チョコレート")
friend_foods.append("アイスクリーム")
print("私が好きな食べ物")
print(my_foods)
print("友達が好きな食べ物")
print(friend_foods)

# list_name = list_name1は
# 別々の変数名で同じリストに関連付けられる
# リストのコピーにはならない
print("\nlist_name = list_name1はリストのコピーではない\n")

my_foods = ["ピザ", "だんご", "ケーキ"]
friend_foods = my_foods
print(my_foods)
print(friend_foods)

my_foods.append("チョコレート")
friend_foods.append("アイスクリーム")

print("私が好きな食べ物")
print(my_foods)
print("友達が好きな食べ物")
print(friend_foods)
