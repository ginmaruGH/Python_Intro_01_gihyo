# 8-04.大きなシャツ
print("\n# 8-04.大きなシャツ\n")

def make_shirt(size='L', message='I love Python'):
    """作成するTシャツの情報を出力する"""
    print(f"\n{size}サイズのTシャツを作ります。")
    print(f"プリントするメッセージは、「{message}」です。")

make_shirt()
make_shirt(size='XL')
make_shirt('S', 'バグを憎んで人を憎まず')
