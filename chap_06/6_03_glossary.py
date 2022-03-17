# 6-3.用語辞典
print("\n用語辞典\n")

glossary = {
    'string': '一連の文字',
    'comment': 'プログラム内のメモ、Pythonインタープリタは無視する',
    'list': '特定の順番のアイテムの集まり',
    'loop': 'アイテムの集まりを1つずつ処理すること',
    'dictionary': 'キーと値のペアの集まり',
    }
for word in glossary.items():
    print(f"{word[0].title()}: {word[1]}\n")
