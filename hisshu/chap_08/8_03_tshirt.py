# 8-03.Tシャツ
print("\n# 8-03.Tシャツ\n")

def make_shirt(size, message):
    """作成するTシャツの情報を出力する"""
    print(f"\n{size}サイズのTシャツを作ります。")
    print(f"プリントするメッセージは、「{message}」です。")

make_shirt('XL', 'Challenge Python!')
make_shirt(message='Spam, Ham, Eggs', size='G-L')
