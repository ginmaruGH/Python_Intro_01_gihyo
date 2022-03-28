# 9-15.くじ引きの分析
print("\n# 9-15.くじ引きの分析\n")


from random import choice


def get_winning_ticket(possibilities):
    """当選番号を作成して返す"""
    winning_ticket = []

    # 同じ数字や文字を繰り返さないために、whileループを使用する
    while len(winning_ticket) < 4:
        pulled_item = choice(possibilities)

        # 存在しない数字や文字の場合だけ、当選した番号リストに追加する
        if pulled_item not in winning_ticket:
            winning_ticket.append(pulled_item)

    return winning_ticket


def make_random_ticket(possibilities):
    """ランダムにくじを作成して返す"""
    ticket = []
    # 同じ数字や文字を繰り返さないために、whileループを使用する
    while len(ticket) < 4:
        pulled_item = choice(possibilities)

        # 存在しない数字や文字の場合だけ、選択した番号リストに追加する
        if pulled_item not in ticket:
            ticket.append(pulled_item)

    return ticket


def check_ticket(played_ticket, winning_ticket):
    """
    プレイヤーのくじが当選しているかをチェックする
    """
    # 当選番号の中にない番号が
    # played_ticketにあればFalseを返す
    for element in played_ticket:
        if element not in winning_ticket:
            return False

    # くじが当たっている
    return True


possibilities = [
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
    'a', 'b', 'c', 'd', 'e'
]
winning_ticket = get_winning_ticket(possibilities)

plays = 0
won = False

# くじの最大試行回数を設定する
max_tries = 10_000

while not won:
    new_ticket = make_random_ticket(possibilities)
    won = check_ticket(new_ticket, winning_ticket)
    plays += 1
    if plays >= max_tries:
        break

if won:
    print("くじに当選しました！")
    print(f"あなたのくじ: {new_ticket}")
    print(f"当選番号: {winning_ticket}")
    print(f"{plays}回目のくじで当選しました！")
else:
    print(f"{plays}回、くじを引きましたが、当選しませんでした...")
    print(f"あなたのくじ: {new_ticket}")
    print(f"当選番号: {winning_ticket}")
