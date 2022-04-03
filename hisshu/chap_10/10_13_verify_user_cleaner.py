# 10-13.ユーザー名を確認

print("\n# 10-13.ユーザー名を確認\n")

import json
from tkinter import Y

def get_stored_username():
    """保存されたユーザー名があれば取得する。"""
    filename = 'chap_10/10_13_verify_user.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """新たなユーザー名の入力を促す。"""
    filename = 'chap_10/10_13_verify_user.json'
    username = input("あなたのお名前は？ >> ")
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """ユーザー名であいさつする。"""
    username = get_stored_username()
    if username:
        correct = input(f"あなたは、{username}さんですか？（y/n）")
        if correct == 'y':
            print(f"おかえりなさい。{username}さん！")
            return

    # usernameは取得できたが、前回と一致しないため、
    # 新たなusernameの入力を求める。
    username = get_new_username()
    print(f"戻ってきたときも名前を覚えておきます。{username}さん！")

greet_user()
