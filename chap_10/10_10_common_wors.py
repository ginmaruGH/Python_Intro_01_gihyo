# 10-10.一般的な単語

print("\n# 10-10.一般的な単語\n")

def count_common_words(filename, word):
    """テキスト内の単語の出現回数を数える。"""
    # 注意：単純な近似値。実際の出現回数より大きな数が返される。

    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words_count = contents.lower().count(word)
        msg = f"単語{word}は、{filename}内に約{words_count}回出現します。"
        print(msg)

filename = 'chap_10/alice.txt'
count_common_words(filename, 'the ')
