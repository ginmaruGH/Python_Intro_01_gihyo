# 9-14.くじ引き

from random import choice


print("\n# 9-14.くじ引き\n")

possibilities = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
    'a', 'b', 'c', 'd', 'e'
    ]

winning_ticket = []
print("くじに当選した番号は...")

# 同じ数字や文字を繰り返さないために、whileループを使用する
while len(winning_ticket) < 4:
    pulled_item = choice(possibilities)

    # 存在しない数字や文字の場合だけ、当選した番号リストに追加する
    if pulled_item not in winning_ticket:
        print(f" 「{pulled_item}」を引きました！")
        winning_ticket.append(pulled_item)

print(f"\n当選番号は、{winning_ticket} です！")
