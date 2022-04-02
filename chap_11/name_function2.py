## Chapter11 コードをテストする
### 関数をテストする
#### テストに失敗する

def get_formatted_name(first, middle, last):
    """フォーマットされたフルネームを返す"""
    full_name = f"{first} {middle} {last}"
    return full_name.title()
