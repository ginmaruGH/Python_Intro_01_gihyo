# 7-9.パストラミ抜きで
print("\n# 7-9.パストラミ抜きで\n")

sandwich_orders = [
    'パストラミ', 'ベジー', 'グリルチーズ', 'パストラミ',
    'ターキー', 'ローストビーフ', 'パストラミ'
]
finished_sandwiches = []

print("あいにく今日は、パストラミは品切れです。")
while 'パストラミ' in sandwich_orders:
    sandwich_orders.remove('パストラミ')

print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"{current_sandwich}サンドを調理中です。")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"ご注文の{sandwich}サンドができました。")
