# 私のピザ、あなたのピザ
print("\n私のピザ、あなたのピザ\n")
favorite_pizzas = ['マルゲリータ', 'クアトロ・フォルマッジ', 'マリナーラ']
friend_pizzas = favorite_pizzas[:]

print("私が好きなピザ")
print(favorite_pizzas)
print("友達が好きなピザ")
print(friend_pizzas)

print("\nそれぞれのリストにピザを追加")
favorite_pizzas.append('ビスマルク')
friend_pizzas.append('ペスカトーレ')

print("私が好きなピザ")
for pizza in favorite_pizzas:
    print(f"- {pizza}")

print("友達が好きなピザ")
for pizza in friend_pizzas:
    print(f"- {pizza}")
